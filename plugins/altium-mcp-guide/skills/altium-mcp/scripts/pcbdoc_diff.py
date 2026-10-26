import sys, re, olefile
from collections import Counter

# usage: pcbdoc_diff.py old.PcbDoc new.PcbDoc
# Compares streams as multisets of records (order-insensitive).
#  - Tracks6/Arcs6/ComponentBodies6/ShapeBasedComponentBodies6/...: [type 1][len 4][data]
#  - Pads6: [type 1] + 6 x ([len 4][data])
#  - Texts6: [type 1][len 4][data][len 4][string]; font-name padding and the WideStrings index are masked,
#            the index is replaced by the Unicode string it points to
#  - WideStrings6: multiset of strings
#  - ComponentBodies6: OVERALLHEIGHT / MODEL.EXTRUDED.MAXZ reported separately
a, b = olefile.OleFileIO(sys.argv[1]), olefile.OleFileIO(sys.argv[2])
rd = lambda o, s: o.openstream(s.split('/')).read()


def generic(d):
    out, p = [], 0
    while p < len(d):
        n = int.from_bytes(d[p + 1:p + 5], 'little')
        out.append(d[p:p + 5 + n])
        p += 5 + n
    return out


def pads(d):
    out, p = [], 0
    while p < len(d):
        s = p
        p += 1
        for _ in range(6):
            n = int.from_bytes(d[p:p + 4], 'little')
            p += 4 + n
        out.append(d[s:p])
    return out


def widestrings(d):
    # binary records: [index 4][len 4][utf16]
    out, p = {}, 0
    while p + 8 <= len(d):
        idx = int.from_bytes(d[p:p + 4], 'little')
        n = int.from_bytes(d[p + 4:p + 8], 'little')
        out[idx] = d[p + 8:p + 8 + n].decode('utf-16-le', 'replace').rstrip('\x00')
        p += 8 + n
    return out


def mask_font(body):
    bb = bytearray(body)
    for m in re.finditer(rb'(?:[A-Za-z0-9 ]\x00){2,31}\x00\x00', body):
        for i in range(m.end(), min(m.start() + 64, len(bb))):
            bb[i] = 0
    return bytes(bb)


def texts(d, ws):
    out, p = [], 0
    while p < len(d):
        n = int.from_bytes(d[p + 1:p + 5], 'little')
        body = bytearray(mask_font(d[p + 5:p + 5 + n]))
        p += 5 + n
        n2 = int.from_bytes(d[p:p + 4], 'little')
        s = d[p + 4:p + 4 + n2]
        p += 4 + n2
        # WideStrings index: u32 at offset 115, present when the record is >= 123 bytes;
        # replace it by the string it points to
        if len(body) >= 123:
            idx = int.from_bytes(body[115:119], 'little')
            body[115:119] = b'\0\0\0\0'
            out.append((bytes(body), s, ws.get(idx, '?%d' % idx)))
        else:
            out.append((bytes(body), s, None))
    return out


bad = 0
names = sorted(set('/'.join(e) for e in a.listdir()) & set('/'.join(e) for e in b.listdir()))
wsa, wsb = widestrings(rd(a, 'WideStrings6/Data')), widestrings(rd(b, 'WideStrings6/Data'))
for s in names:
    da, db = rd(a, s), rd(b, s)
    if da == db:
        continue
    if s.startswith('T') and 'Violation' in s:
        print(f'{s}: differs (DRC/online-DRC results, not design data)')
        continue
    if s in ('FileHeaderSix', 'LayerKindMapping/Data', 'Board6/Data', 'Components6/Data', 'UnionNames/Data'):
        print(f'{s}: differs (checked separately)')
        continue
    if s == 'WideStrings6/Data':
        ok = Counter(wsa.values()) == Counter(wsb.values())
        print(f'{s}: multiset of strings equal: {ok}')
        bad += not ok
        continue
    if s == 'Texts6/Data':
        ra, rb = texts(da, wsa), texts(db, wsb)
    elif s == 'Pads6/Data':
        ra, rb = pads(da), pads(db)
    elif s.endswith('/Data'):
        ra, rb = generic(da), generic(db)
    else:
        print(f'{s}: differs, no parser'); bad += 1
        continue
    if s == 'ComponentBodies6/Data':
        strip = lambda r: re.sub(rb'\|(OVERALLHEIGHT|MODEL\.EXTRUDED\.MAXZ)=[^|]*', b'', r)
        ca, cb = Counter(map(strip, ra)), Counter(map(strip, rb))
        nh = sum((Counter(ra) - Counter(rb)).values())
        ok = ca == cb
        print(f'{s}: records {len(ra)}/{len(rb)}, records with changed heights {nh}, equal after removing OVERALLHEIGHT/MAXZ: {ok}')
        for r in (Counter(ra) - Counter(rb)):
            t = r.decode('latin-1')
            o = re.findall(r'OVERALLHEIGHT=[^|]*|MODEL\.EXTRUDED\.MAXZ=[^|]*|STANDOFFHEIGHT=[^|]*', t)
            print('    old', o)
        for r in (Counter(rb) - Counter(ra)):
            t = r.decode('latin-1')
            o = re.findall(r'OVERALLHEIGHT=[^|]*|MODEL\.EXTRUDED\.MAXZ=[^|]*|STANDOFFHEIGHT=[^|]*', t)
            print('    new', o)
        bad += not ok
        continue
    ok = Counter(ra) == Counter(rb)
    print(f'{s}: records {len(ra)}/{len(rb)}, same multiset (only order differs): {ok}')
    if not ok:
        bad += 1
        print('   only old', len(list((Counter(ra) - Counter(rb)).elements())), 'only new', len(list((Counter(rb) - Counter(ra)).elements())))
print('streams with real differences:', bad)
