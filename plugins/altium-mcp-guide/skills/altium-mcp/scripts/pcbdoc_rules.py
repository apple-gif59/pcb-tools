"""Dump Rules6 / Classes6 / DRC options from a PcbDoc on disk.

usage: pcbdoc_rules.py <PcbDoc> <out.txt> [--full]
Each rule: NAME, RULEKIND, PRIORITY, ENABLED, DRC/online flags, scopes, all other fields.
"""
import sys
import olefile

src, out = sys.argv[1], sys.argv[2]
full = '--full' in sys.argv
o = olefile.OleFileIO(src)


def records(stream, hdr=2):
    d = o.openstream(stream).read()
    p, res = 0, []
    while p < len(d):
        p += hdr  # record type
        n = int.from_bytes(d[p:p + 4], 'little')
        p += 4
        s = d[p:p + n].rstrip(b'\x00')
        p += n
        res.append(s)
    return res


def parse(s):
    t = s.decode('latin1')
    kv = {}
    for part in t.split('|'):
        if '=' in part:
            k, v = part.split('=', 1)
            kv[k] = v
    # Non-ASCII text (e.g. a Chinese COMMENT) is stored mangled in COMMENT and as
    # comma-separated code points in UNICODE__COMMENT: decode it back over the plain field.
    for k in [k for k in kv if k.startswith('UNICODE__')]:
        kv[k[len('UNICODE__'):]] = ''.join(chr(int(c)) for c in kv.pop(k).split(',') if c)
    return kv


rules = [parse(r) for r in records(['Rules6', 'Data'])]
skip = {'SELECTION', 'LAYER', 'LOCKED', 'POLYGONOUTLINE', 'USERROUTED', 'KEEPOUT', 'UNIONINDEX', 'UNICODE',
        'UNIQUEID', 'DEFINEDBYLOGICALDOCUMENT'}
main = ['NAME', 'RULEKIND', 'PRIORITY', 'ENABLED', 'SCOPE1EXPRESSION', 'SCOPE2EXPRESSION', 'NETSCOPE', 'LAYERKIND']
lines = []
for r in sorted(rules, key=lambda r: (r.get('RULEKIND', ''), int(r.get('PRIORITY', '0')))):
    head = '\t'.join(r.get(k, '') for k in main)
    rest = ' '.join(f'{k}={v}' for k, v in r.items() if k not in main and (full or k not in skip))
    lines.append(head + '\t' + rest)
with open(out, 'w', encoding='utf-8') as f:
    f.write(f'# rules: {len(rules)}  source: {src}\n')
    f.write('# NAME\tRULEKIND\tPRIORITY\tENABLED\tSCOPE1\tSCOPE2\tNETSCOPE\tLAYERKIND\tOTHER\n')
    for l in lines:
        f.write(l + '\n')
    # DRC options
    f.write('\n# Design Rule Checker Options6\n')
    d = o.openstream(['Design Rule Checker Options6', 'Data']).read()
    f.write(d[4:].rstrip(b'\x00').decode('latin1') + '\n')
    # classes
    f.write('\n# Classes6\n')
    for c in records(['Classes6', 'Data'], hdr=0):
        kv = parse(c)
        mem = [v for k, v in kv.items() if k.startswith('M') and k[1:].isdigit()]
        f.write(f"{kv.get('NAME','')}\tKIND={kv.get('KIND','')}\tSUPERCLASS={kv.get('SUPERCLASS','')}\tSELECTED={kv.get('SELECTED','')}\tmembers={len(mem)}\t{','.join(mem)}\n")
print(len(rules))
