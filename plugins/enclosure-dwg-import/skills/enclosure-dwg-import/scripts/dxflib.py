"""Minimal DXF reader: flattens model space (with INSERT expansion) into primitives, parses HATCH boundaries.

Primitive kinds (world coords, drawing units):
  ('line', layer, color, x1, y1, x2, y2)
  ('arc',  layer, color, cx, cy, r, a0, a1)   # CCW from a0 to a1 (degrees)
  ('poly', layer, color, [(x,y),...], closed)
  ('text', layer, color, x, y, string)
color is the resolved ACI number (BYLAYER -> layer color, sign dropped).
"""
import math, re, collections


def read_pairs(path):
    raw = open(path, 'rb').read().decode('utf-8', errors='replace')
    L = raw.splitlines()
    return [(int(L[i].strip()), L[i + 1]) for i in range(0, len(L) - 1, 2)]


def split_entities(pairs, start, end):
    ents, cur = [], None
    for c, v in pairs[start:end]:
        if c == 0:
            if cur: ents.append(cur)
            cur = [(0, v)]
        elif cur is not None:
            cur.append((c, v))
    if cur: ents.append(cur)
    return ents


def sections(pairs):
    out, i = {}, 0
    while i < len(pairs):
        if pairs[i] == (0, 'SECTION'):
            name = pairs[i + 1][1]
            j = i + 2
            while pairs[j] != (0, 'ENDSEC'): j += 1
            out[name] = (i + 2, j)
            i = j
        i += 1
    return out


def load(path):
    """Returns (model-space entities, {block name: (base point, entities)}, {layer: ACI color})."""
    pairs = read_pairs(path)
    sec = sections(pairs)
    layer_color = {}
    t0, t1 = sec['TABLES']
    for e in split_entities(pairs, t0, t1):
        if e[0][1] == 'LAYER':
            d = dict((c, v) for c, v in e if c in (2, 62))
            if 2 in d: layer_color[d[2]] = abs(int(d.get(62, 7)))
    blocks = {}
    b0, b1 = sec['BLOCKS']
    cur_name, cur_base, cur = None, (0, 0), []
    for e in split_entities(pairs, b0, b1):
        t = e[0][1]
        if t == 'BLOCK':
            d = dict(e)
            cur_name = d.get(2); cur_base = (float(d.get(10, 0)), float(d.get(20, 0))); cur = []
        elif t == 'ENDBLK':
            blocks[cur_name] = (cur_base, cur); cur_name = None
        elif cur_name is not None:
            cur.append(e)
    e0, e1 = sec['ENTITIES']
    model = split_entities(pairs, e0, e1)
    return model, blocks, layer_color


def g(e, code, default=None, cast=float):
    for c, v in e:
        if c == code: return cast(v)
    return default


def gall(e, code, cast=float):
    return [cast(v) for c, v in e if c == code]


def color_of(e, layer_color, layer):
    col = g(e, 62, None, int)
    if col is None or col == 256: col = layer_color.get(layer, 7)
    return abs(col)


def bspline(degree, knots, ctrl, weights, n_per_span=24):
    """Evaluate a (rational) B-spline by de Boor; returns points."""
    p = degree
    if not weights: weights = [1.0] * len(ctrl)
    pts = []
    lo, hi = knots[p], knots[len(knots) - p - 1]
    spans = max(1, len(ctrl) - p)
    N = spans * n_per_span
    for k in range(N + 1):
        u = lo + (hi - lo) * k / N
        s = p
        while s < len(knots) - p - 2 and u >= knots[s + 1]: s += 1
        d = [(ctrl[j][0] * weights[j], ctrl[j][1] * weights[j], weights[j]) for j in range(s - p, s + 1)]
        for r in range(1, p + 1):
            for j in range(p, r - 1, -1):
                i = j + s - p
                den = knots[i + p - r + 1] - knots[i]
                a = 0 if den == 0 else (u - knots[i]) / den
                d[j] = tuple((1 - a) * d[j - 1][m] + a * d[j][m] for m in range(3))
        x, y, w = d[p]
        pts.append((x / w, y / w))
    return pts


class Xf:
    """2D affine: world = M * local + t."""
    def __init__(self, a=1, b=0, c=0, d=1, tx=0, ty=0):
        self.a, self.b, self.c, self.d, self.tx, self.ty = a, b, c, d, tx, ty

    def __call__(self, x, y):
        return (self.a * x + self.b * y + self.tx, self.c * x + self.d * y + self.ty)

    def compose(self, o):  # self after o
        return Xf(self.a * o.a + self.b * o.c, self.a * o.b + self.b * o.d,
                  self.c * o.a + self.d * o.c, self.c * o.b + self.d * o.d,
                  self.a * o.tx + self.b * o.ty + self.tx, self.c * o.tx + self.d * o.ty + self.ty)

    def det(self): return self.a * self.d - self.b * self.c

    def is_similar(self):
        s1 = math.hypot(self.a, self.c); s2 = math.hypot(self.b, self.d)
        dot = self.a * self.b + self.c * self.d
        return abs(s1 - s2) < 1e-9 * max(1, s1) and abs(dot) < 1e-9 * max(1, s1 * s2)

    def scale(self): return math.sqrt(abs(self.det()))

    def angle(self, deg):
        """Map a direction angle (degrees) through the linear part."""
        r = math.radians(deg)
        x, y = self.a * math.cos(r) + self.b * math.sin(r), self.c * math.cos(r) + self.d * math.sin(r)
        return math.degrees(math.atan2(y, x))


def ocs(e):
    """Xf for the entity's OCS (only extrusion (0,0,+-1) is handled)."""
    z = g(e, 230, 1.0)
    return Xf(-1, 0, 0, 1) if z < 0 else Xf()


def arc_pts(cx, cy, r, a0, a1, step=3.0):
    while a1 <= a0: a1 += 360
    n = max(2, int((a1 - a0) / step) + 1)
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * k / n)),
             cy + r * math.sin(math.radians(a0 + (a1 - a0) * k / n))) for k in range(n + 1)]


def emit_arc(out, xf, lay, col, cx, cy, r, a0, a1):
    if xf.is_similar():
        c = xf(cx, cy); s = xf.scale()
        b0, b1 = xf.angle(a0), xf.angle(a1)
        if xf.det() < 0: b0, b1 = b1, b0
        out.append(('arc', lay, col, c[0], c[1], r * s, b0 % 360, b1 % 360))
    else:
        out.append(('poly', lay, col, [xf(*p) for p in arc_pts(cx, cy, r, a0, a1)], False))


def text_of(e):
    s = ''.join(v for c, v in e if c == 3) + g(e, 1, '', str) if e[0][1] == 'MTEXT' else g(e, 1, '', str)
    s = s.replace('\\P', '\n').replace('^J', '\n')
    return re.sub(r'\{\\[^;]*;|\\[A-Za-z][^;\\{}]*;|[{}]', '', s)


def flatten(ents, blocks, layer_color, xf=None, inh_layer=None, depth=0, out=None):
    """Model-space entities -> primitives. HATCH is skipped (see parse_hatch)."""
    if out is None: out = []
    if xf is None: xf = Xf()
    for e in ents:
        t = e[0][1]
        lay = g(e, 8, '0', str)
        if lay == '0' and inh_layer: lay = inh_layer
        col = color_of(e, layer_color, lay)
        if t == 'LINE':
            p1 = xf(g(e, 10), g(e, 20)); p2 = xf(g(e, 11), g(e, 21))
            out.append(('line', lay, col, *p1, *p2))
        elif t in ('ARC', 'CIRCLE'):
            o = xf.compose(ocs(e))
            cx, cy, r = g(e, 10), g(e, 20), g(e, 40)
            if t == 'CIRCLE':
                emit_arc(out, o, lay, col, cx, cy, r, 0, 180); emit_arc(out, o, lay, col, cx, cy, r, 180, 360)
            else:
                emit_arc(out, o, lay, col, cx, cy, r, g(e, 50), g(e, 51))
        elif t == 'LWPOLYLINE':
            o = xf.compose(ocs(e))
            closed = bool(g(e, 70, 0, int) & 1)
            verts, cur = [], None
            for c, v in e:
                if c == 10: cur = [float(v), 0.0, 0.0]; verts.append(cur)
                elif c == 20 and cur: cur[1] = float(v)
                elif c == 42 and cur: cur[2] = float(v)
            n = len(verts)
            segs = n if closed else n - 1
            for k in range(segs):
                x1, y1, bulge = verts[k]; x2, y2, _ = verts[(k + 1) % n]
                if abs(bulge) < 1e-12:
                    out.append(('line', lay, col, *o(x1, y1), *o(x2, y2)))
                else:
                    th = 4 * math.atan(bulge)
                    ch = math.hypot(x2 - x1, y2 - y1)
                    r = ch / (2 * math.sin(abs(th) / 2))
                    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
                    h = math.sqrt(max(0, r * r - (ch / 2) ** 2))
                    ux, uy = (x2 - x1) / ch, (y2 - y1) / ch
                    sgn = 1 if (bulge > 0) == (abs(th) < math.pi) else -1
                    cx, cy = mx - uy * h * sgn, my + ux * h * sgn
                    a_s = math.degrees(math.atan2(y1 - cy, x1 - cx)); a_e = math.degrees(math.atan2(y2 - cy, x2 - cx))
                    if bulge > 0: emit_arc(out, o, lay, col, cx, cy, r, a_s, a_e)
                    else: emit_arc(out, o, lay, col, cx, cy, r, a_e, a_s)
        elif t == 'SPLINE':
            deg = g(e, 71, 3, int)
            knots = gall(e, 40); w = gall(e, 41)
            ctrl = list(zip(gall(e, 10), gall(e, 20)))
            if len(ctrl) >= deg + 1 and len(knots) == len(ctrl) + deg + 1:
                pts = bspline(deg, knots, ctrl, w if len(w) == len(ctrl) else None)
            else:
                pts = list(zip(gall(e, 11), gall(e, 21)))
            if len(pts) >= 2:
                out.append(('poly', lay, col, [xf(*p) for p in pts], bool(g(e, 70, 0, int) & 1)))
        elif t == 'ELLIPSE':
            cx, cy, mx, my, ratio = g(e, 10), g(e, 20), g(e, 11), g(e, 21), g(e, 40)
            s, en = g(e, 41, 0.0), g(e, 42, 2 * math.pi)
            while en <= s: en += 2 * math.pi
            n = max(8, int((en - s) / math.radians(3)))
            mnx, mny = -my * ratio, mx * ratio
            if g(e, 230, 1.0) < 0: mnx, mny = -mnx, -mny
            pts = [(cx + mx * math.cos(s + (en - s) * k / n) + mnx * math.sin(s + (en - s) * k / n),
                    cy + my * math.cos(s + (en - s) * k / n) + mny * math.sin(s + (en - s) * k / n)) for k in range(n + 1)]
            out.append(('poly', lay, col, [xf(*p) for p in pts], False))
        elif t in ('TEXT', 'MTEXT'):
            out.append(('text', lay, col, *xf(g(e, 10, 0), g(e, 20, 0)), text_of(e)))
        elif t == 'INSERT' and depth < 8:
            name = g(e, 2, '', str)
            if name not in blocks: continue
            base, bents = blocks[name]
            sx, sy, rot = g(e, 41, 1.0), g(e, 42, 1.0), math.radians(g(e, 50, 0.0))
            ix, iy = g(e, 10, 0.0), g(e, 20, 0.0)
            cr, sr = math.cos(rot), math.sin(rot)
            local = Xf(cr * sx, -sr * sy, sr * sx, cr * sy, 0, 0)
            local.tx, local.ty = ix - (local.a * base[0] + local.b * base[1]), iy - (local.c * base[0] + local.d * base[1])
            local = ocs(e).compose(local)
            flatten(bents, blocks, layer_color, xf.compose(local), lay, depth + 1, out)
    return out


def bbox_of(p):
    k = p[0]
    if k == 'line': return (min(p[3], p[5]), min(p[4], p[6]), max(p[3], p[5]), max(p[4], p[6]))
    if k == 'arc':
        pts = arc_pts(p[3], p[4], p[5], p[6], p[7], 10)
    elif k == 'poly': pts = p[3]
    else: return (p[3], p[4], p[3], p[4])
    xs = [q[0] for q in pts]; ys = [q[1] for q in pts]
    return (min(xs), min(ys), max(xs), max(ys))


def to_segments(p, step=2.0):
    k = p[0]
    if k == 'line': return [((p[3], p[4]), (p[5], p[6]))]
    if k == 'arc': pts = arc_pts(p[3], p[4], p[5], p[6], p[7], step)
    elif k == 'poly': pts = p[3] + ([p[3][0]] if p[4] else [])
    else: return []
    return list(zip(pts, pts[1:]))


# ---------------- HATCH boundaries ----------------

def _arc_seq(cx, cy, r, s, e, ccw, step=5.0):
    """Points from start to end, in the edge's travel direction."""
    if ccw:
        return arc_pts(cx, cy, r, s, e, step)
    # clockwise edge: DXF stores the angles negated
    return arc_pts(cx, cy, r, 360 - e, 360 - s, step)[::-1]


def _ell_seq(cx, cy, mx, my, ratio, s, e, ccw, n=48):
    if not ccw: s, e = 360 - e, 360 - s
    while e <= s: e += 360
    a = math.hypot(mx, my); ux, uy = mx / a, my / a; vx, vy = -uy, ux; b = a * ratio
    pts = []
    for k in range(n + 1):
        t = math.radians(s + (e - s) * k / n)
        pts.append((cx + a * math.cos(t) * ux + b * math.sin(t) * vx, cy + a * math.cos(t) * uy + b * math.sin(t) * vy))
    return pts if ccw else pts[::-1]


def _bulge_pts(p0, p1, bulge):
    if abs(bulge) < 1e-9: return [p0]
    th = 4 * math.atan(bulge); dx, dy = p1[0] - p0[0], p1[1] - p0[1]; c = math.hypot(dx, dy)
    r = c / (2 * math.sin(th / 2)); mx, my = (p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2
    h = r * math.cos(th / 2); nx, ny = -dy / c, dx / c
    cx, cy = mx + nx * h, my + ny * h
    a0 = math.atan2(p0[1] - cy, p0[0] - cx); n = max(2, int(abs(math.degrees(th)) / 5))
    return [(cx + abs(r) * math.cos(a0 + th * k / n), cy + abs(r) * math.sin(a0 + th * k / n)) for k in range(n)]


def parse_hatch(e):
    """HATCH entity -> (solid flag, pattern name, [(boundary flag, [pts in OCS])]).
    The loops are not guaranteed to be closed; use them only as extra boundaries."""
    E = e; i = 0
    solid = g(e, 70, 0, int); pattern = g(e, 2, '', str)
    while E[i][0] != 91: i += 1
    nloops = int(E[i][1]); i += 1
    loops = []
    for _ in range(nloops):
        while E[i][0] != 92: i += 1
        flag = int(E[i][1]); i += 1
        if flag & 2:   # polyline
            has_b = 0
            while E[i][0] != 93:
                if E[i][0] == 72: has_b = int(E[i][1])
                i += 1
            nv = int(E[i][1]); i += 1
            vs = []
            while len(vs) < nv:
                if E[i][0] == 10:
                    x = float(E[i][1]); y = float(E[i + 1][1]); i += 2; b = 0.0
                    if has_b and E[i][0] == 42: b = float(E[i][1]); i += 1
                    vs.append((x, y, b))
                else: i += 1
            pts = []
            for k, (x, y, b) in enumerate(vs):
                nx_, ny_, _ = vs[(k + 1) % len(vs)]
                pts += _bulge_pts((x, y), (nx_, ny_), b)
            loops.append((flag, pts))
        else:
            while E[i][0] != 93: i += 1
            ne = int(E[i][1]); i += 1
            edges = []
            for _ in range(ne):
                while E[i][0] != 72: i += 1
                et = int(E[i][1]); i += 1
                vals = collections.defaultdict(list)
                while i < len(E) and E[i][0] not in (72, 92, 97, 75):
                    vals[E[i][0]].append(float(E[i][1])); i += 1
                ccw = int(vals[73][0]) if vals[73] else 1
                if et == 1:
                    edges.append([(vals[10][0], vals[20][0]), (vals[11][0], vals[21][0])])
                elif et == 2:
                    edges.append(_arc_seq(vals[10][0], vals[20][0], vals[40][0], vals[50][0], vals[51][0], ccw))
                elif et == 3:
                    edges.append(_ell_seq(vals[10][0], vals[20][0], vals[11][0], vals[21][0], vals[40][0], vals[50][0], vals[51][0], ccw))
                elif et == 4:
                    if vals[11]:
                        edges.append(list(zip(vals[11], vals[21])))
                    else:
                        deg = int(vals[94][0]); kn = vals[40]; ctrl = list(zip(vals[10], vals[20]))
                        edges.append(bspline(deg, kn, ctrl, vals[42] if len(vals[42]) == len(ctrl) else None, 12))
            # chain edges greedily: always take the remaining edge whose endpoint is nearest the tail
            rest = [ed for ed in edges if ed]
            pts = list(rest.pop(0)) if rest else []
            while rest:
                t = pts[-1]; best = None
                for k, ed in enumerate(rest):
                    for rev in (0, 1):
                        q = ed[-1] if rev else ed[0]
                        d = math.hypot(q[0] - t[0], q[1] - t[1])
                        if best is None or d < best[0]: best = (d, k, rev)
                ed = rest.pop(best[1])
                if best[2]: ed = ed[::-1]
                pts += ed[1:] if best[0] < 1e-6 else ed
            loops.append((flag, pts))
    return solid, pattern, loops
