"""Rebuild filled areas as hole-free polygons.

Boundary = the category's own lines (plus the hatch's boundary loops); seeds = the pattern lines
AutoCAD actually draws (exploded hatches). Raster flood fill -> absorb boundary pixels -> join
diagonal-only contacts -> cut slits from every hole to the outside -> trace pixel edges ->
Douglas-Peucker. Pure functions; no file I/O.
"""
import math, collections

RES = 0.025          # mm per pixel


def solid_hatch_lines(loop, spacing=0.635, ang=135):
    """Synthesize pattern lines inside a closed loop (SOLID hatches have no pattern to explode)."""
    th = math.radians(ang); ux, uy = math.cos(th), math.sin(th); nx, ny = -uy, ux
    offs = [p[0] * nx + p[1] * ny for p in loop]
    lines = []
    o = min(offs) + spacing / 2
    while o < max(offs):
        ts = []
        for a, b in zip(loop, loop[1:] + loop[:1]):
            da = a[0] * nx + a[1] * ny - o; db = b[0] * nx + b[1] * ny - o
            if (da < 0) != (db < 0):
                t = da / (da - db)
                q = (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)
                ts.append((q[0] * ux + q[1] * uy, q))
        ts.sort()
        for k in range(0, len(ts) - 1, 2): lines.append((ts[k][1], ts[k + 1][1]))
        o += spacing
    return lines


class Grid:
    def __init__(self, box):
        self.x0, self.y0 = box[0], box[1]
        self.W = int((box[2] - box[0]) / RES) + 2
        self.H = int((box[3] - box[1]) / RES) + 2
        self.m = bytearray(self.W * self.H)     # 0 empty, 1 boundary, 2 filled
        self.dup = 0

    def mark_seg(self, a, b, val=1):
        W, Hh, m = self.W, self.H, self.m
        fx0 = (a[0] - self.x0) / RES; fy0 = (a[1] - self.y0) / RES
        fx1 = (b[0] - self.x0) / RES; fy1 = (b[1] - self.y0) / RES
        i, j = int(math.floor(fx0)), int(math.floor(fy0))
        ie, je = int(math.floor(fx1)), int(math.floor(fy1))
        dx, dy = fx1 - fx0, fy1 - fy0
        sx = 1 if dx > 0 else -1; sy = 1 if dy > 0 else -1
        tdx = abs(1 / dx) if dx else 1e30; tdy = abs(1 / dy) if dy else 1e30
        tmx = ((i + 1 - fx0) if dx > 0 else (fx0 - i)) * tdx if dx else 1e30
        tmy = ((j + 1 - fy0) if dy > 0 else (fy0 - j)) * tdy if dy else 1e30
        n = abs(ie - i) + abs(je - j) + 2
        for _ in range(n):
            if 0 <= i < W and 0 <= j < Hh: m[j * W + i] = val
            if i == ie and j == je: break
            if tmx < tmy: tmx += tdx; i += sx
            else: tmy += tdy; j += sy

    def pix(self, p):
        return int((p[0] - self.x0) / RES), int((p[1] - self.y0) / RES)

    def flood(self, seeds):
        W, m = self.W, self.m
        st = [j * W + i for i, j in seeds if 0 <= i < W and 0 <= j < self.H and m[j * W + i] == 0]
        for q in st: m[q] = 2
        N = len(m)
        while st:
            q = st.pop()
            i = q % W
            for r in (q - 1 if i > 0 else -1, q + 1 if i < W - 1 else -1, q - W, q + W):
                if 0 <= r < N and m[r] == 0:
                    m[r] = 2; st.append(r)

    def absorb_boundary(self):
        W, m = self.W, self.m
        add = [q for q in range(W, len(m) - W) if m[q] == 1 and (m[q - 1] == 2 or m[q + 1] == 2 or m[q - W] == 2 or m[q + W] == 2)]
        for q in add: m[q] = 2
        for q in range(len(m)):
            if m[q] == 1: m[q] = 0

    def fix_saddles(self):
        W, m = self.W, self.m
        n = 0
        for j in range(self.H - 1):
            base = j * W
            for i in range(W - 1):
                a = m[base + i] == 2; b = m[base + i + 1] == 2; c = m[base + W + i] == 2; d = m[base + W + i + 1] == 2
                if a == d and b == c and a != b:
                    # diagonal-only contact: fill one empty pixel so the pieces join
                    if a: m[base + i + 1] = 2
                    else: m[base + i] = 2
                    n += 1
        return n

    def trace(self):
        """Directed pixel-edge loops with filled area on the left (y up)."""
        W, Hh, m = self.W, self.H, self.m
        nxt = {}
        for j in range(Hh):
            row = j * W
            for i in range(W):
                if m[row + i] != 2: continue
                if j == 0 or m[row - W + i] != 2: self.dup += (i, j) in nxt; nxt[(i, j)] = (i + 1, j)
                if i == W - 1 or m[row + i + 1] != 2: self.dup += (i + 1, j) in nxt; nxt[(i + 1, j)] = (i + 1, j + 1)
                if j == Hh - 1 or m[row + W + i] != 2: self.dup += (i + 1, j + 1) in nxt; nxt[(i + 1, j + 1)] = (i, j + 1)
                if i == 0 or m[row + i - 1] != 2: self.dup += (i, j + 1) in nxt; nxt[(i, j + 1)] = (i, j)
        loops = []
        while nxt:
            s, v = nxt.popitem()
            loop = [s]
            while v != s:
                loop.append(v)
                v = nxt.pop(v)
            loops.append(loop)
        return loops

    def to_mm(self, v):
        return (self.x0 + v[0] * RES, self.y0 + v[1] * RES)


def area(P):
    return sum(P[k - 1][0] * P[k][1] - P[k][0] * P[k - 1][1] for k in range(len(P))) / 2


def corners(loop):
    """Drop collinear lattice points."""
    out = []
    n = len(loop)
    for k in range(n):
        a, b, c = loop[k - 1], loop[k], loop[(k + 1) % n]
        if (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0]) != 0: out.append(b)
    return out


def dp(pts, tol):
    keep = [False] * len(pts); keep[0] = keep[-1] = True
    st = [(0, len(pts) - 1)]
    while st:
        a, b = st.pop()
        ax, ay = pts[a]; bx, by = pts[b]; L = math.hypot(bx - ax, by - ay)
        best, bi = -1, -1
        for k in range(a + 1, b):
            px, py = pts[k]
            d = abs((bx - ax) * (ay - py) - (ax - px) * (by - ay)) / L if L else math.hypot(px - ax, py - ay)
            if d > best: best, bi = d, k
        if best > tol:
            keep[bi] = True; st += [(a, bi), (bi, b)]
    return [p for p, k in zip(pts, keep) if k]


def simplify_loop(P, tol):
    # split the closed loop at two far-apart points so DP has fixed anchors
    i0 = min(range(len(P)), key=lambda k: (P[k][0], P[k][1]))
    P = P[i0:] + P[:i0]
    i1 = max(range(len(P)), key=lambda k: (P[k][0] - P[0][0]) ** 2 + (P[k][1] - P[0][1]) ** 2)
    a = dp(P[:i1 + 1], tol); b = dp(P[i1:] + [P[0]], tol)
    return a[:-1] + b[:-1]


def seg_intersections(P):
    """Count proper crossings between non-adjacent edges (bucketed)."""
    n = len(P); E = [(P[k], P[(k + 1) % n]) for k in range(n)]
    B = collections.defaultdict(list); cell = 2.0
    for k, (a, b) in enumerate(E):
        for gx in range(int(math.floor(min(a[0], b[0]) / cell)), int(math.floor(max(a[0], b[0]) / cell)) + 1):
            for gy in range(int(math.floor(min(a[1], b[1]) / cell)), int(math.floor(max(a[1], b[1]) / cell)) + 1):
                B[(gx, gy)].append(k)

    def cr(o, a, b): return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    bad = set()
    for ks in B.values():
        for x in range(len(ks)):
            for y in range(x + 1, len(ks)):
                i, j = ks[x], ks[y]
                if abs(i - j) <= 1 or abs(i - j) == n - 1: continue
                (p1, p2), (p3, p4) = E[i], E[j]
                d1, d2, d3, d4 = cr(p3, p4, p1), cr(p3, p4, p2), cr(p1, p2, p3), cr(p1, p2, p4)
                if ((d1 > 0) != (d2 > 0)) and ((d3 > 0) != (d4 > 0)) and d1 and d2 and d3 and d4: bad.add((min(i, j), max(i, j)))
    return len(bad)


def fill_regions(boundary, pattern):
    """boundary, pattern: lists of ((x,y),(x,y)) segments in mm.
    Returns (polygons sorted by area, largest first: [{'pts','area','raw_area','x'}], stats dict)."""
    pxs = [p[0] for s in pattern for p in s]; pys = [p[1] for s in pattern for p in s]
    box = (min(pxs) - 1, min(pys) - 1, max(pxs) + 1, max(pys) + 1)
    g = Grid(box)
    for a, b in boundary: g.mark_seg(a, b)
    seeds = []
    for a, b in pattern:
        L = math.hypot(b[0] - a[0], b[1] - a[1]); n = max(1, int(L / (RES * 0.7)))
        for k in range(1, n):
            t = k / n
            seeds.append(g.pix((a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)))
    g.flood(seeds)
    g.absorb_boundary()
    ns = 0
    while True:
        k = g.fix_saddles(); ns += k
        if not k: break
    # cut 2-px slits from every hole up to the outside, until no hole is left
    for it in range(20):
        loops = g.trace()
        holes = [L for L in loops if area(L) < 0]
        if not holes: break
        for L in holes:
            top = max(L, key=lambda v: (v[1], -v[0]))
            i, j = top[0], top[1]          # lattice point; pixels above are (i-1..i, j..)
            jj = j
            while jj < g.H and (g.m[jj * g.W + i] == 2 or g.m[jj * g.W + i - 1] == 2):
                g.m[jj * g.W + i] = 0; g.m[jj * g.W + i - 1] = 0; jj += 1
    polys = []
    for L in loops:
        # edge midpoints halve the pixel staircase before simplifying
        M = [((L[k][0] + L[(k + 1) % len(L)][0]) / 2, (L[k][1] + L[(k + 1) % len(L)][1]) / 2) for k in range(len(L))]
        P = [g.to_mm(v) for v in corners(M)]
        A = area(P)
        Q = simplify_loop(P, RES * 0.8)
        polys.append({'pts': Q, 'area': area(Q), 'raw_area': A, 'x': seg_intersections(Q)})
    polys.sort(key=lambda d: -d['area'])
    return polys, {'grid': (g.W, g.H), 'saddles': ns, 'iterations': it, 'holes_left': len(holes), 'dupvertex': g.dup}


def point_in_poly(p, P):
    x, y = p; inside = False
    for k in range(len(P)):
        (x1, y1), (x2, y2) = P[k - 1], P[k]
        if (y1 > y) != (y2 > y) and x < x1 + (y - y1) * (x2 - x1) / (y2 - y1): inside = not inside
    return inside
