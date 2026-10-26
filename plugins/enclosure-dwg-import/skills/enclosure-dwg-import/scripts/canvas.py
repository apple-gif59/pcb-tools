"""Tiny RGB canvas: lines, even-odd polygon fill with alpha, PNG output."""
import zlib, struct, math


class Canvas:
    def __init__(self, box, width=2000):
        self.x0, self.y0, self.x1, self.y1 = box
        self.sc = width / (self.x1 - self.x0)
        self.W, self.H = width, int((self.y1 - self.y0) * self.sc)
        self.buf = bytearray(b'\xff' * (self.W * self.H * 3))

    def px(self, x, y):
        return ((x - self.x0) * self.sc, (self.y1 - y) * self.sc)

    def blend(self, X, Y, rgb, a):
        if 0 <= X < self.W and 0 <= Y < self.H:
            i = (Y * self.W + X) * 3
            for k in range(3): self.buf[i + k] = int(self.buf[i + k] * (1 - a) + rgb[k] * a)

    def line(self, a, b, rgb, thick=1, alpha=1.0):
        X0, Y0 = self.px(*a); X1, Y1 = self.px(*b)
        n = int(max(abs(X1 - X0), abs(Y1 - Y0))) + 1
        for k in range(n + 1):
            X = int(X0 + (X1 - X0) * k / n); Y = int(Y0 + (Y1 - Y0) * k / n)
            for dx in range(-(thick // 2), thick - thick // 2):
                for dy in range(-(thick // 2), thick - thick // 2):
                    self.blend(X + dx, Y + dy, rgb, alpha)

    def poly(self, P, rgb, thick=1, closed=True, alpha=1.0):
        segs = list(zip(P, P[1:] + ([P[0]] if closed else [])))
        for a, b in segs: self.line(a, b, rgb, thick, alpha)

    def fill(self, loops, rgb, alpha=0.35):
        """Even-odd fill of several loops (each implicitly closed)."""
        edges = []
        for P in loops:
            Q = [self.px(*p) for p in P]
            for a, b in zip(Q, Q[1:] + Q[:1]):
                if a[1] != b[1]: edges.append((a, b))
        if not edges: return
        ymin = max(0, int(min(min(a[1], b[1]) for a, b in edges)))
        ymax = min(self.H - 1, int(max(max(a[1], b[1]) for a, b in edges)) + 1)
        for Y in range(ymin, ymax + 1):
            yc = Y + 0.5; xs = []
            for a, b in edges:
                if (a[1] <= yc < b[1]) or (b[1] <= yc < a[1]):
                    xs.append(a[0] + (yc - a[1]) * (b[0] - a[0]) / (b[1] - a[1]))
            xs.sort()
            for k in range(0, len(xs) - 1, 2):
                for X in range(max(0, int(xs[k] + 0.5)), min(self.W, int(xs[k + 1] + 0.5))):
                    self.blend(X, Y, rgb, alpha)

    def save(self, path):
        W, H = self.W, self.H
        raw = b''.join(b'\x00' + bytes(self.buf[y * W * 3:(y + 1) * W * 3]) for y in range(H))
        def chunk(t, d): return struct.pack('>I', len(d)) + t + d + struct.pack('>I', zlib.crc32(t + d) & 0xffffffff)
        open(path, 'wb').write(b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', W, H, 8, 2, 0, 0, 0))
                               + chunk(b'IDAT', zlib.compress(raw, 6)) + chunk(b'IEND', b''))
