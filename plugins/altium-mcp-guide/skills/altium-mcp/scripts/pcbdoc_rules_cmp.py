"""Compare two pcbdoc_rules.py outputs: lists DELETED / NEW rule names and per-field MOD lines.

usage: pcbdoc_rules_cmp.py before.txt after.txt [FIELD,FIELD,...]   (fields to ignore, e.g. UNIQUEID)
A rule touched by any modify moves to priority 1, so PRIORITY changes are expected noise.
"""
import sys, re
def load(f):
    R = {}
    for l in open(f, encoding='utf-8', errors='replace'):
        if l.startswith('#') or '\t' not in l: continue
        p = l.rstrip('\n').split('\t')
        if len(p) < 9: continue
        if p[1].startswith('KIND='): continue  # Classes6 section, not a rule
        other = {}
        for m in re.finditer(r'(\S+?)=((?:(?! \S+?=).)*)', p[8]):
            other[m.group(1)] = m.group(2)
        R[p[0]] = dict(KIND=p[1], PRIORITY=p[2], ENABLED=p[3], SCOPE1=p[4], SCOPE2=p[5], NETSCOPE=p[6], LAYERKIND=p[7], **other)
    return R
a, b = load(sys.argv[1]), load(sys.argv[2])
skip = set(sys.argv[3].split(',')) if len(sys.argv) > 3 else set()
print('before', len(a), 'after', len(b))
print('DELETED:', sorted(set(a) - set(b)))
print('NEW:', sorted(set(b) - set(a)))
for n in sorted(set(a) & set(b)):
    x, y = a[n], b[n]
    d = [(k, x.get(k), y.get(k)) for k in sorted(set(x) | set(y)) if x.get(k) != y.get(k) and k not in skip]
    if d: print('MOD', n, d)
