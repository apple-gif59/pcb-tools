"""Compare shell_import.py output with a PcbDoc on disk (read-only, needs olefile).

usage: python compare_pcbdoc.py <workdir> <PcbDoc> [out.txt]
Checks, each as "same" or a list of differences:
  rules.txt   rooms: present, LAYER, ENABLED (= DRC on), CONFINEMENTSTYLE ConfineOut, scope, comment, vertices
              height rules: scope, comment, min/max/preferred
              rules in the PcbDoc that a D prefix would delete but rules.txt does not recreate (manual additions!)
              P order: the listed rules' priorities in the PcbDoc
  drawing.txt layer names; free tracks/arcs on the L layers (multiset, 0.001 mm / 0.01 deg)
  cutouts.txt free Board Cutout regions (vertex lists, 0.001 mm); free non-plated pads named as in H lines
A git revision is compared by first writing it out: git show <rev>:<file>.PcbDoc > copy.PcbDoc
"""
import sys, os, re, struct, collections
import olefile

MIL = 0.0254
IU = MIL / 10000          # internal unit -> mm


def rd(path):
    return [l.rstrip('\n').split('\t') for l in open(path, encoding='utf-8-sig')]


class Doc:
    def __init__(self, path):
        self.o = olefile.OleFileIO(path)
        b6 = self.stream('Board6').decode('latin1')
        self.ox = float(re.search(r'\|ORIGINX=([-\d.]+)mil', b6).group(1)) * MIL
        self.oy = float(re.search(r'\|ORIGINY=([-\d.]+)mil', b6).group(1)) * MIL
        ids = dict(re.findall(r'LAYER_V8_(\d+)LAYERID=(\d+)', b6))
        names = dict(re.findall(r'LAYER_V8_(\d+)NAME=([^|]*)', b6))
        self.mech_names = {}
        for k, lid in ids.items():
            n = int(lid) - 0x1020000
            if 1 <= n <= 16 and k in names:
                s = names[k]          # non-ASCII names are stored as comma-separated code points
                self.mech_names[n] = ''.join(chr(int(c)) for c in s.split(',')) if re.fullmatch(r'\d+(,\d+)+', s) else s

    def stream(self, name):
        return self.o.openstream([name, 'Data']).read()

    def records(self, name):
        d = self.stream(name); p = 0; out = []
        while p < len(d):
            n = int.from_bytes(d[p + 1:p + 5], 'little'); out.append(d[p + 5:p + 5 + n]); p += 5 + n
        return out

    def rules(self):
        d = self.stream('Rules6'); p = 0; out = {}
        while p < len(d):
            n = int.from_bytes(d[p + 2:p + 6], 'little'); t = d[p + 6:p + 6 + n].rstrip(b'\x00').decode('latin1'); p += 6 + n
            kv = {}
            for part in t.split('|'):
                if '=' in part:
                    k, v = part.split('=', 1); kv[k] = v
            for k in [k for k in kv if k.startswith('UNICODE__')]:
                kv[k[9:]] = ''.join(chr(int(c)) for c in kv.pop(k).split(',') if c)
            out[kv.get('NAME', '')] = kv
        return out

    def pads(self):
        d = self.stream('Pads6'); p = 0; out = []
        while p < len(d):
            p += 1; blocks = []
            for _ in range(6):
                n = int.from_bytes(d[p:p + 4], 'little'); blocks.append(d[p + 4:p + 4 + n]); p += 4 + n
            out.append((blocks[0][1:].decode('latin1'), blocks[4]))
        return out


def mil_mm(v):
    return float(v.replace('mil', '')) * MIL


def match(gen, pcb, tol):
    """Multiset match of tuples: strings/ints exactly, floats within tol (exact pass on values rounded
    to 0.001, then the leftovers pair up within tol). Returns (only in gen, only in pcb)."""
    def key(t): return tuple(round(v, 3) + 0.0 if isinstance(v, float) else v for v in t)
    left = collections.defaultdict(list)
    for t in pcb: left[key(t)].append(t)
    rest_g = []
    for t in gen:
        if left[key(t)]: left[key(t)].pop()
        else: rest_g.append(t)
    rest_p = [t for v in left.values() for t in v]
    only_g = []
    for t in rest_g:
        for j, u in enumerate(rest_p):
            if all((abs(x - y) <= tol if isinstance(x, float) else x == y) for x, y in zip(t, u)):
                del rest_p[j]; break
        else: only_g.append(t)
    return only_g, rest_p


def track(mech, x1, y1, x2, y2, wd):
    """AD may store a track with its ends swapped."""
    p, q = sorted([(x1, y1), (x2, y2)])
    if abs(p[0] - q[0]) < 0.002: p, q = sorted([(x1, y1), (x2, y2)], key=lambda v: v[1])
    return ('T', mech, p[0], p[1], q[0], q[1], wd)


def ang(a):
    a = float(a) % 360
    return a - 360 if a > 359.999 else a


def main(work, pcbdoc, outp=None):
    D = Doc(pcbdoc)
    lines = []
    w = lines.append
    nbad = 0

    # ---------------- rules
    rows = rd(os.path.join(work, 'rules.txt'))
    PR = D.rules()
    gen, prefixes, porder = {}, [], []
    i = 0
    while i < len(rows):
        t = rows[i]
        if t[0] == 'D': prefixes.append(t[1])
        elif t[0] == 'P': porder.append(t[1])
        elif t[0] == 'R':
            n = int(t[8]); gen[t[1]] = ('R', t, [(float(v[1]), float(v[2])) for v in rows[i + 1:i + 1 + n]]); i += n
        elif t[0] == 'H': gen[t[1]] = ('H', t, None)
        i += 1
    w('== rules: %d generated, %d in the PcbDoc' % (len(gen), len(PR)))
    for nm, (kind, t, pts) in gen.items():
        r = PR.get(nm)
        if r is None: w('  MISSING in PcbDoc: %s' % nm); nbad += 1; continue
        diffs = []
        if kind == 'R':
            if r.get('RULEKIND') != 'RoomDefinition': diffs.append('RULEKIND=%s' % r.get('RULEKIND'))
            if r.get('LAYER') != ('TOP' if t[2] == '1' else 'BOTTOM'): diffs.append('LAYER %s vs %s' % (r.get('LAYER'), t[2]))
            if r.get('ENABLED') != ('TRUE' if t[3] == '1' else 'FALSE'): diffs.append('ENABLED %s vs drc %s' % (r.get('ENABLED'), t[3]))
            if r.get('CONFINEMENTSTYLE') != 'ConfineOut': diffs.append('CONFINEMENTSTYLE=%s' % r.get('CONFINEMENTSTYLE'))
            if r.get('SCOPE1EXPRESSION') != t[4]: diffs.append('scope\n      pcb: %s\n      gen: %s' % (r.get('SCOPE1EXPRESSION'), t[4]))
            if r.get('COMMENT') != t[5]: diffs.append('comment pcb %r gen %r' % (r.get('COMMENT'), t[5]))
            k = 0; q = []
            while 'VX%d' % k in r:
                q.append((mil_mm(r['VX%d' % k]) - D.ox, mil_mm(r['VY%d' % k]) - D.oy)); k += 1
            if len(q) > 1 and abs(q[0][0] - q[-1][0]) < 0.001 and abs(q[0][1] - q[-1][1]) < 0.001: q.pop()   # stored closed
            if len(q) != len(pts): diffs.append('vertices %d vs %d' % (len(q), len(pts)))
            else:
                dmax = max(max(abs(a[0] - b[0]), abs(a[1] - b[1])) for a, b in zip(q, pts))
                if dmax > 0.001: diffs.append('vertices differ, max %.4f mm' % dmax)
        else:
            if r.get('RULEKIND') != 'Height': diffs.append('RULEKIND=%s' % r.get('RULEKIND'))
            if r.get('SCOPE1EXPRESSION') != t[4]: diffs.append('scope\n      pcb: %s\n      gen: %s' % (r.get('SCOPE1EXPRESSION'), t[4]))
            if r.get('COMMENT') != t[5]: diffs.append('comment pcb %r gen %r' % (r.get('COMMENT'), t[5]))
            for key, v in (('MAXHEIGHT', t[2]), ('PREFHEIGHT', t[2]), ('MINHEIGHT', t[3])):
                if abs(mil_mm(r.get(key, '0mil')) - float(v)) > 0.0005: diffs.append('%s pcb %.4f gen %s' % (key, mil_mm(r.get(key, '0mil')), v))
        if diffs:
            nbad += 1; w('  DIFF %s: %s' % (nm, '; '.join(diffs)))
    extra = sorted(n for n in PR if any(n.startswith(p) for p in prefixes) and n not in gen)
    w('  rules the D prefixes would delete without recreating: %s' % (extra or 'none'))
    nbad += bool(extra)
    if porder:
        kinds = collections.defaultdict(list)
        for n in porder:
            if n in PR: kinds[PR[n]['RULEKIND']].append((int(PR[n]['PRIORITY']), n))
            else: w('  P %s: not in the PcbDoc' % n)
        for k, v in kinds.items():
            order = [n for _, n in sorted(v, reverse=True)]
            ok = order == [n for n in porder if n in dict((x[1], 1) for x in v)]
            w('  priority %s (%s): %s' % (k, 'same order as P lines' if ok else 'DIFFERENT order', ', '.join('%s=%d' % (n, p) for p, n in sorted(v))))
            nbad += not ok

    # ---------------- drawing
    rows = rd(os.path.join(work, 'drawing.txt'))
    L = {int(t[1]): t[2] for t in rows if t[0] == 'L'}
    w('== drawing layers')
    for n, name in sorted(L.items()):
        if D.mech_names.get(n) != name: w('  M%d name pcb %r gen %r' % (n, D.mech_names.get(n), name)); nbad += 1
    lid = {56 + n: n for n in L}
    G, P = [], []
    for t in rows:
        if t[0] == 'T': G.append(track(int(t[1]), *map(float, t[2:7])))
        elif t[0] == 'A': G.append(('A', int(t[1]), *map(float, t[2:5]), ang(t[5]), ang(t[6]), float(t[7])))
    for d in D.records('Tracks6'):
        if d[0] in lid and int.from_bytes(d[7:9], 'little') == 0xFFFF:
            x1, y1, x2, y2, wd = struct.unpack('<5i', d[13:33])
            P.append(track(lid[d[0]], x1 * IU - D.ox, y1 * IU - D.oy, x2 * IU - D.ox, y2 * IU - D.oy, wd * IU))
    for d in D.records('Arcs6'):
        if d[0] in lid and int.from_bytes(d[7:9], 'little') == 0xFFFF:
            x, y, r = struct.unpack('<3i', d[13:25]); a0, a1 = struct.unpack('<2d', d[25:41]); wd = struct.unpack('<i', d[41:45])[0]
            P.append(('A', lid[d[0]], x * IU - D.ox, y * IU - D.oy, r * IU, ang(a0), ang(a1), wd * IU))
    d = D.stream('Texts6'); p = 0; ntext = 0
    while p < len(d):
        n = int.from_bytes(d[p + 1:p + 5], 'little'); body = d[p + 5:p + 5 + n]; p += 5 + n
        p += 4 + int.from_bytes(d[p:p + 4], 'little')
        ntext += body[0] in lid and int.from_bytes(body[7:9], 'little') == 0xFFFF
    w('  free texts on those layers (import_drawing.pas deletes them): %d' % ntext)
    only_g, only_p = match(G, P, 0.002)
    w('== drawing: %d generated, %d free tracks/arcs on those layers in the PcbDoc; only generated %d, only PcbDoc %d' % (
        len(G), len(P), len(only_g), len(only_p)))
    fmt = lambda t: '%s M%d ' % t[:2] + ' '.join('%.4f' % v for v in t[2:])
    for t in only_g[:10]: w('  only generated %s' % fmt(t))
    for t in only_p[:10]: w('  only PcbDoc    %s' % fmt(t))
    nbad += bool(only_g or only_p)

    # ---------------- cutouts and holes
    rows = rd(os.path.join(work, 'cutouts.txt'))
    gl, gh, i = [], [], 0
    while i < len(rows):
        t = rows[i]
        if t[0] == 'C':
            n = int(t[1]); gl.append([(float(v[1]), float(v[2])) for v in rows[i + 1:i + 1 + n]]); i += n
        elif t[0] == 'H': gh.append((t[4], float(t[1]), float(t[2]), float(t[3])))
        i += 1
    pl = []
    for d in D.records('Regions6'):
        if int.from_bytes(d[7:9], 'little') != 0xFFFF: continue
        ln = int.from_bytes(d[18:22], 'little'); txt = d[22:22 + ln]
        if b'ISBOARDCUTOUT=TRUE' not in txt: continue
        rest = d[22 + ln:]; nv = int.from_bytes(rest[:4], 'little')
        pl.append([(x * IU - D.ox, y * IU - D.oy) for x, y in (struct.unpack('<2d', rest[4 + 16 * k:20 + 16 * k]) for k in range(nv))])
    # a cutout matches when its vertex multiset matches one PcbDoc cutout (AD may start the contour elsewhere)
    left = list(pl); unmatched = []
    for c in gl:
        for j, q in enumerate(left):
            if len(q) == len(c) and match(c, q, 0.002) == ([], []): del left[j]; break
        else: unmatched.append(c)
    w('== cutouts: %d generated, %d free Board Cutouts in the PcbDoc; generated without a match: %d, PcbDoc without a match: %d' % (
        len(gl), len(pl), len(unmatched), len(left)))
    for c in unmatched + left:
        w('  unmatched cutout, %d vertices, bbox (%.4f, %.4f)-(%.4f, %.4f)' % (len(c), min(p[0] for p in c), min(p[1] for p in c), max(p[0] for p in c), max(p[1] for p in c)))
    nbad += bool(unmatched or left)
    names = {k[0] for k in gh}
    ph = []
    for name, b in D.pads():
        if name in names and int.from_bytes(b[7:9], 'little') == 0xFFFF:
            x, y = struct.unpack('<2i', b[13:21]); hole = struct.unpack('<i', b[45:49])[0]
            ph.append((name, x * IU - D.ox, y * IU - D.oy, hole * IU))
    og, op = match(gh, ph, 0.002)
    w('== holes: %d generated, %d free pads with those names in the PcbDoc; only generated %s; only PcbDoc %s' % (len(gh), len(ph), og or 'none', op or 'none'))
    nbad += bool(og or op)
    w('== %s' % ('no differences' if not nbad else '%d difference groups' % nbad))
    text = '\n'.join(lines) + '\n'
    if outp: open(outp, 'w', encoding='utf-8').write(text)
    print(text)


if __name__ == '__main__':
    if len(sys.argv) not in (3, 4): sys.exit(__doc__)
    main(*sys.argv[1:])
