"""Enclosure DWG -> Altium import data, driven by a per-project config (TOML, format in SKILL.md).

usage: python shell_import.py <config.toml> <workdir>
input : <workdir>/outline.dxf, <workdir>/hatchlines.txt          (from dwg2dxf.ps1)
output: <workdir>/report.txt      views, per-view layer/colour counts, hatches, rooms, cutouts, texts, warnings
        <workdir>/drawing.txt     L/T/A  mechanical-layer drawing (outlines, hatch pattern lines, side views)
        <workdir>/cutouts.txt     C/V board cutouts, H holes
        <workdir>/rules.txt       D/R/V/H/P rooms and height rules
        <workdir>/import_drawing.pas, import_cutouts.pas, import_rules.pas   (templates filled with paths)
        <workdir>/front.png, back.png   previews in PCB coordinates
All coordinates written are mm relative to the PCB origin.
"""
import sys, os, math, collections, tomllib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import dxflib, regions, canvas

warnings = []


def warn(msg):
    warnings.append(msg)


def fail(msg):
    sys.exit('ERROR: ' + msg)


# ------------------------------------------------------------------ config

def load_config(path):
    with open(path, 'rb') as f:
        c = tomllib.load(f)
    base = os.path.dirname(os.path.abspath(path))
    for k in ('pcbdoc', 'dwg', 'views', 'layers', 'mech', 'widths', 'region'):
        if k not in c: fail('config has no "%s"' % k)
    c['pcbdoc'] = os.path.normpath(os.path.join(base, c['pcbdoc']))
    d = c['dwg']
    d.setdefault('skip_layers', [])
    d.setdefault('legend_default', 'comp')
    d['legend'] = {int(k): v for k, v in d.get('legend', {}).items()}
    v = c['views']
    v.setdefault('margin', 12.0)
    v.setdefault('group_gap', 3.0)
    v.setdefault('sides', [])
    for face in ('front', 'back'):
        if face not in v: fail('views.%s missing' % face)
        v[face].setdefault('mirror', False)
    c['layers'] = {int(k): x for k, x in c['layers'].items()}
    for n, x in c['layers'].items():
        col = x.get('color')
        if col is not None and not (isinstance(col, str) and col.startswith('$') and len(col) == 9):
            fail('layers.%d.color must look like "$00BBGGRR"' % n)
    for r in c['region']:
        r.setdefault('min_area', 0.05)
        r.setdefault('suffix', '')
        if r['face'] not in ('front', 'back'): fail('region %s: face must be front/back' % r['room'])
        if r['layer'] not in ('top', 'bottom'): fail('region %s: layer must be top/bottom' % r['room'])
    for h in c.get('height', []):
        h.setdefault('min', 0.0); h.setdefault('exclude', []); h.setdefault('suffix', '')
    c.setdefault('exempt', [])
    c.setdefault('cutouts', {}); c.setdefault('holes', {}); c.setdefault('rules', {})
    cu = c['cutouts']
    cu.setdefault('boxes', []); cu.setdefault('margin', 0.1); cu.setdefault('arc_tol', 0.002); cu.setdefault('chain_tol', 0.005)
    ho = c['holes']
    ho.setdefault('min_radius', 0.0); ho.setdefault('name', 'NPTH')
    return c


# ------------------------------------------------------------------ geometry helpers

def inside(b, V, m):
    return b[0] >= V[0] - m and b[2] <= V[2] + m and b[1] >= V[1] - m and b[3] <= V[3] + m


def touches(b, V, m):
    return b[0] < V[2] + m and b[2] > V[0] - m and b[1] < V[3] + m and b[3] > V[1] - m


def outline_groups(prims, layer, gap):
    """Cluster the outline layer by bounding-box proximity: one group per drawn view of the board."""
    groups = []
    for p in prims:
        if p[1] != layer or p[0] == 'text': continue
        b = dxflib.bbox_of(p)
        for gr in groups:
            if touches(b, gr['box'], gap):
                B = gr['box']; gr['box'] = (min(B[0], b[0]), min(B[1], b[1]), max(B[2], b[2]), max(B[3], b[3])); gr['p'].append(p); break
        else:
            groups.append({'box': b, 'p': [p]})
    changed = True
    while changed:
        changed = False
        for i in range(len(groups)):
            for j in range(i + 1, len(groups)):
                A, B = groups[i]['box'], groups[j]['box']
                if touches(A, B, gap):
                    groups[i]['box'] = (min(A[0], B[0]), min(A[1], B[1]), max(A[2], B[2]), max(A[3], B[3]))
                    groups[i]['p'] += groups[j]['p']; del groups[j]; changed = True; break
            if changed: break
    return groups


class View:
    """Maps one drawn view onto the PCB: the outline group's bbox min goes to pcb_outline_min;
    a mirrored (back) view is flipped left-right about its own bbox."""
    def __init__(self, name, group, pcb_min, mirror):
        self.name, self.group, self.box, self.mirror = name, group, group['box'], mirror
        self.px0, self.py0 = pcb_min

    def __call__(self, x, y):
        B = self.box
        if self.mirror: return (B[2] - x + self.px0, y - B[1] + self.py0)
        return (x - B[0] + self.px0, y - B[1] + self.py0)

    def arc_angles(self, a0, a1):
        return ((180 - a1) % 360, (180 - a0) % 360) if self.mirror else (a0, a1)


def poly_points(xf, p):
    pts = [xf(*q) for q in p[3]] + ([xf(*p[3][0])] if p[4] else [])
    keep = [pts[0]]                      # drop tiny steps to keep the primitive count sane
    for q in pts[1:]:
        if math.hypot(q[0] - keep[-1][0], q[1] - keep[-1][1]) >= 0.05: keep.append(q)
    if keep[-1] != pts[-1]: keep.append(pts[-1])
    return keep


def emit_prim(out, mech, xf, p, width, angles=None):
    """Append T/A records ('T', mech, x1, y1, x2, y2, w) / ('A', mech, cx, cy, r, a0, a1, w)."""
    if p[0] == 'line':
        a, b = xf(p[3], p[4]), xf(p[5], p[6])
        if math.hypot(b[0] - a[0], b[1] - a[1]) >= 1e-4: out.append(('T', mech, *a, *b, width))
    elif p[0] == 'arc':
        c = xf(p[3], p[4]); a0, a1 = angles(p[6], p[7]) if angles else (p[6], p[7])
        out.append(('A', mech, c[0], c[1], p[5], a0, a1, width))
    elif p[0] == 'poly':
        keep = poly_points(xf, p)
        for a, b in zip(keep, keep[1:]):
            if math.hypot(b[0] - a[0], b[1] - a[1]) >= 1e-4: out.append(('T', mech, *a, *b, width))


def rec_segments(r):
    if r[0] == 'T': return [((r[2], r[3]), (r[4], r[5]))]
    pts = dxflib.arc_pts(r[2], r[3], r[4], r[5], r[6], 2.0)
    return list(zip(pts, pts[1:]))


def bgr_to_rgb(col):
    v = int(col[1:], 16)
    return (v & 0xFF, (v >> 8) & 0xFF, (v >> 16) & 0xFF)


# ------------------------------------------------------------------ cutouts

def arc_points_tol(cx, cy, r, a0, a1, tol):
    while a1 <= a0: a1 += 360
    step = math.degrees(2 * math.acos(max(-1, 1 - tol / r))) if r > tol else 90
    n = max(1, int(math.ceil((a1 - a0) / step)))
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * k / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * k / n))) for k in range(n + 1)]


def cutout_pieces(view, box, cfg):
    m, tol = cfg['margin'], cfg['arc_tol']
    out, seen = [], set()
    for p in view.group['p']:
        b = dxflib.bbox_of(p)
        q0 = view(b[0], b[1]); q1 = view(b[2], b[3])
        lo = (min(q0[0], q1[0]), min(q0[1], q1[1])); hi = (max(q0[0], q1[0]), max(q0[1], q1[1]))
        if not (box[0] - m <= lo[0] and hi[0] <= box[2] + m and box[1] - m <= lo[1] and hi[1] <= box[3] + m): continue
        if p[0] == 'line': pts = [view(p[3], p[4]), view(p[5], p[6])]
        elif p[0] == 'arc':
            c = view(p[3], p[4]); a0, a1 = view.arc_angles(p[6], p[7]); pts = arc_points_tol(c[0], c[1], p[5], a0, a1, tol)
        elif p[0] == 'poly':
            pts = [view(*q) for q in p[3]] + ([view(*p[3][0])] if p[4] else [])
        else: continue
        key = tuple(sorted([tuple(round(v, 3) for v in pts[0]), tuple(round(v, 3) for v in pts[-1])])) + (p[0], round(len(pts), -1))
        if key in seen: continue        # some drawings have edges twice
        seen.add(key); out.append(pts)
    # drop dangling pieces (an endpoint nobody else shares), e.g. outline notches that fall in the box
    k = lambda q: (round(q[0], 3), round(q[1], 3))
    while True:
        deg = collections.Counter()
        for pts in out: deg[k(pts[0])] += 1; deg[k(pts[-1])] += 1
        keep = [pts for pts in out if deg[k(pts[0])] > 1 and deg[k(pts[-1])] > 1]
        if len(keep) == len(out): return out
        out = keep


def chain(ps, tol):
    if not ps: raise ValueError('no closed outline found in the box')
    rest = list(ps); loop = list(rest.pop(0))
    while rest:
        t = loop[-1]; best = None
        for k, pc in enumerate(rest):
            for rev in (0, 1):
                q = pc[-1] if rev else pc[0]
                d = math.hypot(q[0] - t[0], q[1] - t[1])
                if best is None or d < best[0]: best = (d, k, rev)
        if best[0] > tol: raise ValueError('gap %.4f at (%.4f, %.4f)' % (best[0], t[0], t[1]))
        pc = rest.pop(best[1])
        if best[2]: pc = pc[::-1]
        loop += pc[1:]
    gap = math.hypot(loop[0][0] - loop[-1][0], loop[0][1] - loop[-1][1])
    if gap > tol: raise ValueError('loop not closed, gap %.4f' % gap)
    loop.pop()
    out = [loop[0]]
    for q in loop[1:]:
        if math.hypot(q[0] - out[-1][0], q[1] - out[-1][1]) > 1e-4: out.append(q)
    return out


# ------------------------------------------------------------------ main

def main(cfg_path, work):
    cfg = load_config(cfg_path)
    D, VW = cfg['dwg'], cfg['views']
    rep = []
    w = rep.append
    model, blocks, lc = dxflib.load(os.path.join(work, 'outline.dxf'))
    prims = dxflib.flatten(model, blocks, lc)
    nblk = sum(1 for b in blocks.values() for e in b[1] if e[0][1] == 'HATCH')
    if nblk: warn('%d HATCH entities are inside blocks: they are not exploded or imported' % nblk)
    w('== DXF: %d model entities %s, %d primitives after INSERT expansion' % (
        len(model), dict(collections.Counter(e[0][1] for e in model)), len(prims)))

    # ---- views
    groups = outline_groups(prims, D['outline_layer'], VW['group_gap'])
    w('== outline layer groups (DWG coords)')
    for i, gr in enumerate(groups):
        B = gr['box']
        w('  [%d] box=(%.3f, %.3f)-(%.3f, %.3f) size=%.3f x %.3f prims=%d' % (i, *B, B[2] - B[0], B[3] - B[1], len(gr['p'])))
    views = {}
    for face in ('front', 'back'):
        box = VW[face]['box']
        hit = [gr for gr in groups if inside(gr['box'], box, 0)]
        if len(hit) != 1: fail('views.%s.box %s contains %d outline groups (need exactly 1); see the group list above:\n%s' % (face, box, len(hit), '\n'.join(rep)))
        views[face] = View(face, hit[0], VW['pcb_outline_min'], VW[face]['mirror'])
        w('  %s = group %d%s' % (face, groups.index(hit[0]), ' (mirrored)' if VW[face]['mirror'] else ''))
    sf, sb = views['front'].box, views['back'].box
    if abs((sf[2] - sf[0]) - (sb[2] - sb[0])) > 0.01 or abs((sf[3] - sf[1]) - (sb[3] - sb[1])) > 0.01:
        warn('front and back outline bboxes differ in size: %.3f x %.3f vs %.3f x %.3f (an edge missing in one view?)' % (
            sf[2] - sf[0], sf[3] - sf[1], sb[2] - sb[0], sb[3] - sb[1]))

    def category(col):
        return D['legend'].get(col, D['legend_default'])

    def mech_of(face, cat):
        mp = cfg['mech'].get(face, {})
        if cat not in mp: fail('mech.%s has no layer for category "%s"' % (face, cat))
        return mp[cat]

    # ---- drawing (outlines, per face)
    WD = cfg['widths']
    drawing = []
    face_recs = {}        # face -> its outline records (for the previews)
    margin = VW['margin']
    for face, V in views.items():
        start = len(drawing)
        inc, part = collections.Counter(), collections.Counter()
        for p in prims:
            if p[0] == 'text': continue
            b = dxflib.bbox_of(p)
            if not inside(b, V.box, margin):
                if touches(b, V.box, margin): part[(p[1], p[2], p[0])] += 1
                continue
            inc[(p[1], p[2], p[0])] += 1
            if p[1] in D['skip_layers']: continue
            emit_prim(drawing, mech_of(face, category(p[2])), V, p, WD['line'], V.arc_angles)
        face_recs[face] = drawing[start:]
        w('== %s view: primitives inside (layer, colour, kind): count -> category / mech layer' % face)
        for (lay, col, kind), n in sorted(inc.items()):
            dest = 'skipped' if lay in D['skip_layers'] else '%s / M%d' % (category(col), mech_of(face, category(col)))
            w('  %s c%d %s: %d -> %s' % (lay, col, kind, n, dest))
        for (lay, col, kind), n in sorted(part.items()):
            w('  partly outside, not imported: %s c%d %s: %d' % (lay, col, kind, n))

    # ---- hatches
    pattern = collections.defaultdict(list); other = collections.Counter()
    for ln in open(os.path.join(work, 'hatchlines.txt'), encoding='utf-8', errors='replace'):
        t = ln.split()
        if not t: continue
        if t[0] == 'L': pattern[t[1]].append(tuple(map(float, t[2:6])))
        else: other[(t[1], t[2])] += 1
    if other: w('== exploded pieces that are not LINE (ignored): %s' % dict(other))
    hatches = []
    for e in model:
        if e[0][1] != 'HATCH': continue
        lay = dxflib.g(e, 8, '0', str); col = dxflib.color_of(e, lc, lay)
        solid, pat, loops = dxflib.parse_hatch(e)
        o = dxflib.ocs(e)
        allp = [o(*p) for _, P in loops for p in P]
        handle = dxflib.g(e, 5, '', str)
        if not allp: continue
        cx = sum(p[0] for p in allp) / len(allp); cy = sum(p[1] for p in allp) / len(allp)
        face = None
        for name, V in views.items():
            if V.box[0] - margin <= cx <= V.box[2] + margin and V.box[1] - margin <= cy <= V.box[3] + margin: face = name
        h = {'handle': handle, 'face': face, 'layer': lay, 'col': col, 'solid': solid, 'pattern': pat, 'cat': category(col), 'loops': [], 'lines': []}
        hatches.append(h)
        if not face: continue
        V = views[face]
        for flag, P in loops:
            Q = [V(*o(*p)) for p in P]
            R = [Q[0]]
            for q in Q[1:]:
                if math.hypot(q[0] - R[-1][0], q[1] - R[-1][1]) > 1e-4: R.append(q)
            if len(R) > 2 and math.hypot(R[0][0] - R[-1][0], R[0][1] - R[-1][1]) < 1e-4: R.pop()
            h['loops'].append((flag, R))
        h['lines'] = [(V(a, b), V(c, d)) for a, b, c, d in pattern.get(handle, [])]

    # ---- regions -> rooms
    REG = cfg['region']
    rooms = {}            # room prefix -> [(name, pts)]
    used = set()
    w('== regions')
    for r in REG:
        face, cat = r['face'], r['category']
        mech = mech_of(face, cat)
        hs = [h for h in hatches if h['face'] == face and h['cat'] == cat]
        used.update(id(h) for h in hs)
        rooms[r['room']] = []
        if not hs:
            warn('region %s: no %s hatch with category "%s"' % (r['room'], face, cat)); continue
        # boundary: this face's lines of this category, plus the hatches' own loops
        bnd = []
        V = views[face]
        for p in prims:
            if p[0] == 'text' or p[1] in D['skip_layers'] or category(p[2]) != cat: continue
            if not inside(dxflib.bbox_of(p), V.box, margin): continue
            tmp = []
            emit_prim(tmp, mech, V, p, WD['line'], V.arc_angles)
            for x in tmp: bnd += rec_segments(x)
        pat = []
        for h in hs:
            if h['lines']: pat += h['lines']
            else:
                for _, P in h['loops']: pat += regions.solid_hatch_lines(P)
            for _, P in h['loops']:
                bnd += list(zip(P, P[1:]))
                if math.hypot(P[0][0] - P[-1][0], P[0][1] - P[-1][1]) < 0.5: bnd.append((P[-1], P[0]))
        polys, st = regions.fill_regions(bnd, pat)
        if st['holes_left']: warn('region %s: %d holes left after slitting' % (r['room'], st['holes_left']))
        w('  %s (%s %s, M%d): hatches=%d grid=%dx%d saddles=%d slit-iterations=%d pieces=%d' % (
            r['room'], face, cat, mech, len(hs), *st['grid'], st['saddles'], st['iterations'], len(polys)))
        k = 0
        for d in polys:
            P = d['pts']
            if regions.area(P) < 0: P = P[::-1]
            if abs(d['area']) < r['min_area']:
                w('    dropped (area %.4f < min_area): box=(%.2f, %.2f)' % (d['area'], min(p[0] for p in P), min(p[1] for p in P))); continue
            k += 1
            nm = '%s%02d' % (r['room'], k)
            rooms[r['room']].append((nm, P))
            if d['x']: warn('room %s: outline has %d self-crossings' % (nm, d['x']))
    # hatches not used by any region
    for h in hatches:
        if id(h) not in used:
            w('  hatch %s (%s, layer %s, c%d, category %s) is not used by any region' % (h['handle'], h['face'] or 'outside views', h['layer'], h['col'], h['cat']))

    # ---- exemptions (anchored by a point inside the region)
    exempt = collections.defaultdict(list)
    for x in cfg['exempt']:
        pref = [r['room'] for r in REG if x['room'].startswith(r['room'])]
        if not pref: fail('exempt %s: no region with a matching room prefix' % x['room'])
        hit = [nm for nm, P in rooms[max(pref, key=len)] if regions.point_in_poly(x['at'], P)]
        if len(hit) != 1: fail('exempt %s: point %s lies in %d rooms of that region' % (x['room'], x['at'], len(hit)))
        if hit[0] != x['room']:
            fail('exempt: the room at %s is now %s, config says %s (room numbering changed; rules that reference room names must be checked)' % (x['at'], hit[0], x['room']))
        exempt[hit[0]] += x['parts']

    def excl(scope, des):
        if not des: return scope
        return scope + ' and Not (%s)' % ' or '.join("InComponent('%s')" % d for d in sorted(des))

    # ---- rules.txt
    rules = []
    for r in REG: rules.append('D\t%s' % r['room'])
    for h in cfg.get('height', []): rules.append('D\t%s' % h['name'])
    w('== rooms')
    for r in REG:
        for nm, P in rooms[r['room']]:
            xs = [p[0] for p in P]; ys = [p[1] for p in P]
            scope = excl(r['scope'], exempt.get(nm)) + r['suffix']
            rules.append('R\t%s\t%d\t%d\t%s\t%s\t%.5f\t%.5f\t%d' % (nm, 1 if r['layer'] == 'top' else 32, 1 if r['drc'] else 0, scope, r['comment'], min(xs), min(ys), len(P)))
            rules += ['V\t%.5f\t%.5f' % p for p in P]
            w('  %s area=%.3f box=(%.2f, %.2f)-(%.2f, %.2f) n=%d%s' % (nm, regions.area(P), min(xs), min(ys), max(xs), max(ys), len(P),
                                                                     '  exempt: ' + ' '.join(sorted(exempt[nm])) if nm in exempt else ''))
    for h in cfg.get('height', []):
        names = [nm for nm, _ in rooms.get(h['rooms'], [])]
        if not names: fail('height %s: region %s produced no rooms' % (h['name'], h['rooms']))
        scope = '%s and (%s)' % (h['scope'], ' or '.join("TouchesRoom('%s')" % n for n in names))
        scope = excl(scope, h['exclude']) + h['suffix']
        rules.append('H\t%s\t%.4f\t%.4f\t%s\t%s' % (h['name'], h['max'], h['min'], scope, h['comment']))
    for n in cfg['rules'].get('priority_order', []): rules.append('P\t%s' % n)

    # ---- drawing: hatch pattern lines and side views
    for r in REG:
        mech = mech_of(r['face'], r['category'])
        for h in hatches:
            if h['face'] != r['face'] or h['cat'] != r['category']: continue
            pat = h['lines']
            if not pat:   # SOLID hatch: synthesize lines and draw its outline too
                pat = [l for _, P in h['loops'] for l in regions.solid_hatch_lines(P)]
                for _, P in h['loops']:
                    for a, b in zip(P, P[1:] + P[:1]): drawing.append(('T', mech, *a, *b, WD['solid_edge']))
            for a, b in pat:
                if math.hypot(b[0] - a[0], b[1] - a[1]) < 0.01: continue
                drawing.append(('T', mech, *a, *b, WD['pattern']))
    side = cfg['mech'].get('side')
    if VW['sides'] and side is None: fail('views.sides given but mech.side is missing')
    for box in VW['sides']:
        for p in prims:
            if p[0] == 'text' or p[1] in D['skip_layers']: continue
            if inside(dxflib.bbox_of(p), box, 0): emit_prim(drawing, side, views['front'], p, WD['side'])

    # ---- cutouts and holes (front view outline group)
    CU, HO = cfg['cutouts'], cfg['holes']
    cut = []
    w('== cutouts')
    for box in CU['boxes']:
        ps = cutout_pieces(views['front'], box, CU)
        try:
            L = chain(ps, CU['chain_tol'])
        except ValueError as ex:
            fail('cutout box %s: %s' % (box, ex))
        if regions.area(L) < 0: L = L[::-1]
        xs = [p[0] for p in L]; ys = [p[1] for p in L]
        w('  box %s: pieces=%d pts=%d area=%.3f bbox=(%.4f, %.4f)-(%.4f, %.4f) size=%.4f x %.4f' % (
            box, len(ps), len(L), regions.area(L), min(xs), min(ys), max(xs), max(ys), max(xs) - min(xs), max(ys) - min(ys)))
        cut.append('C\t%d' % len(L)); cut += ['V\t%.5f\t%.5f' % p for p in L]
    arcs = collections.defaultdict(float)
    for p in views['front'].group['p']:
        if p[0] != 'arc': continue
        c = views['front'](p[3], p[4]); key = (round(c[0], 4), round(c[1], 4), round(p[5], 4))
        arcs[key] += (p[7] - p[6]) % 360 or 360
    m = CU['margin']
    for (cx, cy, r), span in sorted(arcs.items()):
        in_cut = any(b[0] - m <= cx <= b[2] + m and b[1] - m <= cy <= b[3] + m for b in CU['boxes'])
        if span >= 359.9 and not in_cut and r > HO['min_radius']:
            cut.append('H\t%.5f\t%.5f\t%.4f\t%s' % (cx, cy, 2 * r, HO['name']))
            w('  hole d=%.4f at (%.4f, %.4f)' % (2 * r, cx, cy))

    # ---- texts (for reading; never imported)
    w('== texts per view (PCB coords)')
    for p in prims:
        if p[0] != 'text': continue
        for face, V in views.items():
            if V.box[0] - 30 <= p[3] <= V.box[2] + 30 and V.box[1] - 30 <= p[4] <= V.box[3] + 30:
                q = V(p[3], p[4])
                w('  %s %s c%d (%.1f, %.1f): %s' % (face, p[1], p[2], q[0], q[1], p[5].replace('\n', ' ')[:100]))

    # ---- write
    def write(name, lines):
        with open(os.path.join(work, name), 'w', encoding='utf-8-sig', newline='\r\n') as f:
            f.write('\n'.join(lines) + '\n')
    dl = []
    for n, x in sorted(cfg['layers'].items()):
        dl.append('L\t%d\t%s\t%s' % (n, x['name'], int(x['color'][1:], 16) if x.get('color') else ''))
    for r in drawing:
        if r[0] == 'T': dl.append('T\t%d\t%.5f\t%.5f\t%.5f\t%.5f\t%.4f' % r[1:])
        else: dl.append('A\t%d\t%.5f\t%.5f\t%.5f\t%.4f\t%.4f\t%.4f' % r[1:])
    undeclared = sorted({r[1] for r in drawing} - set(cfg['layers']))
    if undeclared: fail('mechanical layers used but not declared in [layers]: %s' % undeclared)
    write('drawing.txt', dl); write('cutouts.txt', cut); write('rules.txt', rules)
    for name, data in (('import_drawing.pas', 'drawing.txt'), ('import_cutouts.pas', 'cutouts.txt'), ('import_rules.pas', 'rules.txt')):
        src = open(os.path.join(HERE, 'pas', name), encoding='utf-8').read()
        src = src.replace('@@PCBDOC@@', cfg['pcbdoc'].replace("'", "''")).replace('@@DATA@@', os.path.abspath(os.path.join(work, data)).replace("'", "''"))
        with open(os.path.join(work, name), 'w', encoding='utf-8') as f: f.write(src)
    cnt = collections.Counter((r[0], r[1], r[-1]) for r in drawing)
    w('== drawing records (kind, mech, width): count')
    for k, v in sorted(cnt.items()): w('  %s M%d w=%.3f: %d' % (*k, v))

    # ---- previews
    for face, V in views.items():
        B = V.box; px0, py0 = VW['pcb_outline_min']
        cv = canvas.Canvas((px0 - 5, py0 - 5, px0 + B[2] - B[0] + 5, py0 + B[3] - B[1] + 5), 2000)
        for r in face_recs[face]:
            col = cfg['layers'].get(r[1], {}).get('color')
            for a, b in rec_segments(r): cv.line(a, b, bgr_to_rgb(col) if col else (0, 0, 0))
        for reg in REG:
            if reg['face'] != face: continue
            col = cfg['layers'].get(mech_of(face, reg['category']), {}).get('color')
            rgb = bgr_to_rgb(col) if col else (255, 0, 0)
            for nm, P in rooms[reg['room']]:
                cv.fill([P], rgb, 0.35); cv.poly(P, rgb, 2)
        cv.save(os.path.join(work, face + '.png'))

    w('== warnings')
    rep += ['  ' + x for x in warnings] or ['  none']
    with open(os.path.join(work, 'report.txt'), 'w', encoding='utf-8') as f: f.write('\n'.join(rep) + '\n')
    print('rooms %d, height rules %d, drawing records %d, cutouts %d, holes %d, warnings %d -> %s' % (
        sum(len(v) for v in rooms.values()), len(cfg.get('height', [])), len(drawing),
        sum(1 for l in cut if l[0] == 'C'), sum(1 for l in cut if l[0] == 'H'), len(warnings), os.path.join(work, 'report.txt')))


if __name__ == '__main__':
    if len(sys.argv) != 3: sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
