"""First look at a converted drawing, before writing the project config.

usage: python survey.py <workdir> [outline layer]
reads <workdir>/outline.dxf; writes <workdir>/survey.txt and <workdir>/survey.png (whole drawing, coloured by ACI)
Lists: layers with ACI colours, primitive counts and bboxes; hatches (layer, colour, pattern, centre);
texts (legend and notes); with an outline layer, its groups = the drawn views of the board.
"""
import sys, os, collections, colorsys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import dxflib, canvas
from shell_import import outline_groups

ACI = {1: (230, 0, 0), 2: (200, 180, 0), 3: (0, 170, 0), 4: (0, 170, 200), 5: (0, 0, 230), 6: (200, 0, 200), 7: (0, 0, 0)}


def aci_rgb(c):
    if c in ACI: return ACI[c]
    r, g, b = colorsys.hsv_to_rgb(((c * 47) % 360) / 360, 0.9, 0.8)
    return (int(r * 255), int(g * 255), int(b * 255))


def main(work, outline=None):
    model, blocks, lc = dxflib.load(os.path.join(work, 'outline.dxf'))
    prims = dxflib.flatten(model, blocks, lc)
    out = []
    w = out.append
    w('== entities %s' % dict(collections.Counter(e[0][1] for e in model)))
    w('== layer colours (ACI) %s' % lc)
    by = collections.defaultdict(lambda: [1e18, 1e18, -1e18, -1e18, 0])
    for p in prims:
        if p[0] == 'text': continue
        b = dxflib.bbox_of(p); r = by[(p[1], p[2])]
        r[0] = min(r[0], b[0]); r[1] = min(r[1], b[1]); r[2] = max(r[2], b[2]); r[3] = max(r[3], b[3]); r[4] += 1
    w('== (layer, colour): primitives, bbox')
    for k, v in sorted(by.items()): w('  %s c%d: %d  (%.1f, %.1f)-(%.1f, %.1f)' % (*k, v[4], *v[:4]))
    w('== hatches: handle layer colour pattern solid centre')
    for e in model:
        if e[0][1] != 'HATCH': continue
        lay = dxflib.g(e, 8, '0', str)
        solid, pat, loops = dxflib.parse_hatch(e)
        pts = [p for _, P in loops for p in P]
        if not pts: continue
        o = dxflib.ocs(e); pts = [o(*p) for p in pts]
        w('  %s %s c%d %s solid=%d (%.1f, %.1f)' % (dxflib.g(e, 5, '', str), lay, dxflib.color_of(e, lc, lay), pat, solid,
                                                   sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts)))
    nblk = sum(1 for b in blocks.values() for e in b[1] if e[0][1] == 'HATCH')
    if nblk: w('  + %d hatches inside blocks (not exploded by dwg2dxf.ps1)' % nblk)
    w('== texts')
    for p in prims:
        if p[0] == 'text': w('  %s c%d (%.1f, %.1f): %s' % (p[1], p[2], p[3], p[4], p[5].replace('\n', ' ')))
    if outline:
        w('== groups of layer %s (one per drawn view of the board)' % outline)
        for i, gr in enumerate(outline_groups(prims, outline, 3.0)):
            B = gr['box']
            w('  [%d] box=(%.3f, %.3f)-(%.3f, %.3f) size=%.3f x %.3f prims=%d' % (i, *B, B[2] - B[0], B[3] - B[1], len(gr['p'])))
    geo = [p for p in prims if p[0] != 'text']
    xs = [v for p in geo for v in (dxflib.bbox_of(p)[0], dxflib.bbox_of(p)[2])]
    ys = [v for p in geo for v in (dxflib.bbox_of(p)[1], dxflib.bbox_of(p)[3])]
    cv = canvas.Canvas((min(xs) - 5, min(ys) - 5, max(xs) + 5, max(ys) + 5), 3000)
    for p in geo:
        for a, b in dxflib.to_segments(p, 2.0): cv.line(a, b, aci_rgb(p[2]))
    cv.save(os.path.join(work, 'survey.png'))
    open(os.path.join(work, 'survey.txt'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print('-> %s, survey.png' % os.path.join(work, 'survey.txt'))


if __name__ == '__main__':
    if len(sys.argv) not in (2, 3): sys.exit(__doc__)
    main(*sys.argv[1:])
