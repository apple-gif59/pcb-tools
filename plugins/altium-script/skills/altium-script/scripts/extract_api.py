"""Extract the DelphiScript API registry compiled into Altium's ScriptingSystem.dll.

Usage: python -X utf8 extract_api.py <AD install dir or ScriptingSystem.dll> <out api.json>

The script engine registers every interface, method, property, global routine, class and
constant through a few registrar functions. We linear-sweep every .pdata function with a small
x64 decoder, keep the argument values at each call, find the registrars by their argument
shapes, and resolve names, owners (interface GUID / class VMT), signatures (method RTTI _Tnnn)
and constant values.
"""
import sys, os, struct, json, collections, datetime, hashlib, uuid, re

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pe_lite import PE
from x64lite import trace_function
from extract_processes import altium_build

REGN = {1: 'rcx', 2: 'rdx', 8: 'r8', 9: 'r9'}
PF = [(1, 'var'), (2, 'const'), (32, 'out')]
# Delphi x64 VMT slots used here (this compiler: vmtSelfPtr = -200)
VMT_TYPEINFO, VMT_CLASSNAME, VMT_PARENT = -168, -136, -120


def addm(store, name, m):
    lst = store.setdefault(name, [])
    if all(x['decl'] != m['decl'] for x in lst):
        lst.append(m)


class Extractor:
    def __init__(self, path):
        self.pe = PE(path)
        self.d = self.pe.d

    # ---------- argument values ----------
    def val(self, v):
        pe = self.pe
        if v is None:
            return None
        k = v[0]
        if k == 'addr':
            r = v[1]
            s = pe.ustr(r)
            if s is not None:
                return ('STR', s)
            ti = pe.typeinfo(r)
            if ti:
                return ('TI', ti[0], ti[1], r)
            return ('ADDR', r)
        if k == 'mem':
            r = v[1]
            q = pe.q(r)
            if q is None:
                return ('MEM', r)
            if pe.base <= q < pe.base + 0x10000000:
                t = q - pe.base
                ti = pe.typeinfo(t)
                if ti:
                    return ('PTI', ti[0], ti[1], t)
                s = pe.ustr(t)
                if s is not None:
                    return ('PSTR', s)
                return ('PADDR', t, r)
            return ('IMM', q)
        if k == 'mem32':
            o = pe.r2o(v[1])
            return ('IMM', struct.unpack_from('<i', self.d, o)[0]) if o is not None else None
        if k == 'smem':
            o = pe.r2o(v[1])
            return ('SMEM', struct.unpack_from('<i', self.d, o)[0] if o is not None else None)
        if k == 'imm':
            return ('IMM', v[1])
        if k == 'local':
            return ('LOCAL', v[1])
        return None

    def collect(self):
        pe = self.pe
        pdir = pe.pe.OPTIONAL_HEADER.DATA_DIRECTORY[3]
        po = pe.r2o(pdir.VirtualAddress)
        funcs = []
        for k in range(pdir.Size // 12):
            b, e, u = struct.unpack_from('<III', self.d, po + 12 * k)
            if pe.text_rva <= b < pe.text_rva + pe.text_size:
                funcs.append((b, e))
        funcs.sort()
        recs = []
        for fb, fe in funcs:
            g = trace_function(pe, fb, fe, lambda t: True)
            try:
                while True:
                    a, tgt, regs, stack, xmm, locals_w = next(g)
                    args = {n: self.val(regs.get(r)) for r, n in REGN.items()}
                    for sd, sv in stack.items():
                        if isinstance(sd, int) and 0x20 <= sd <= 0x60:
                            args['s%x' % sd] = self.val(sv)
                    named = any(x and x[0] in ('STR', 'PSTR', 'PTI', 'TI') for x in args.values())
                    arr = (args['rcx'] and args['rcx'][0] == 'ADDR' and args['rdx'] and args['rdx'][0] == 'IMM'
                           and args['r8'] is None)
                    if not (named or arr):
                        continue
                    extra = None
                    v = regs.get(2)
                    if v and v[0] == 'local' and v[1] in locals_w:
                        ca, ct, cregs, cxmm = locals_w[v[1]]
                        extra = (ct, {n: self.val(cregs.get(r)) for r, n in REGN.items()}, dict(cxmm))
                    recs.append((a, tgt, args, extra))
            except StopIteration:
                pass
        self.recs = recs

    # ---------- classes / RTTI ----------
    def class_name(self, vmt):
        q = self.pe.deref(vmt + VMT_CLASSNAME)
        if q is None:
            return None
        o = self.pe.r2o(q)
        if o is None:
            return None
        n, _ = self.pe.ss(o)
        return n if re.fullmatch(r'[A-Za-z_][A-Za-z0-9_.<>,]*', n or '') else None

    def class_array(self, r, hi):
        """RegisterClasses(array of TClass): rva of first element, high index -> [vmt]"""
        out = []
        for i in range(hi + 1):
            v = self.pe.deref(r + 8 * i)
            if v is None:
                return None
            if self.class_name(v) is None:
                v2 = self.pe.deref(v)   # element may be a pointer to the class variable
                if v2 is None or self.class_name(v2) is None:
                    return None
                v = v2
            out.append(v)
        return out

    def class_info(self, vmt):
        pe = self.pe
        name = self.class_name(vmt)
        parent = None
        slot = pe.deref(vmt + VMT_PARENT)
        if slot is not None:
            pv = pe.deref(slot)
            if pv is not None:
                parent = self.class_name(pv)
        unit, props = None, {}
        ti = pe.deref(vmt + VMT_TYPEINFO)
        if ti is not None:
            o = pe.r2o(ti)
            if o is not None and self.d[o] == 7:
                _, o = pe.ss(o + 1)
                o += 8 + 8 + 2
                unit, o = pe.ss(o)
                cnt = struct.unpack_from('<H', self.d, o)[0]
                o += 2
                for _ in range(cnt):
                    ptype, getp, setp = struct.unpack_from('<QQQ', self.d, o)
                    o += 8 * 4 + 4 + 4 + 2
                    pname, o = pe.ss(o)
                    tname = None
                    if ptype:
                        t = pe.deref(ptype - pe.base)
                        if t is not None:
                            tt = pe.typeinfo(t)
                            tname = tt[1] if tt else None
                    props[pname] = {'type': tname, 'readonly': setp == 0, 'published': True}
        return name, parent, unit, props

    def method_sig(self, t):
        """tkMethod typeinfo at rva t -> (methodkind, [(flags, name, type)], result)"""
        o = self.pe.r2o(t)
        if o is None or self.d[o] != 8:
            return None
        _, o = self.pe.ss(o + 1)
        mk, pc = self.d[o], self.d[o + 1]
        o += 2
        ps = []
        for _ in range(pc):
            fl = self.d[o]
            pn, o = self.pe.ss(o + 1)
            tn, o = self.pe.ss(o)
            ps.append((fl, pn, tn))
        res = None
        if mk in (1, 3, 9):
            res, o = self.pe.ss(o)
        return mk, ps, res

    def intf_info(self, t):
        pe = self.pe
        o = pe.r2o(t)
        name, o = pe.ss(o + 1)
        pp = struct.unpack_from('<Q', self.d, o)[0]
        o += 8 + 1
        guid = bytes(self.d[o:o + 16])
        o += 16
        unit, o = pe.ss(o)
        parent = None
        if pp:
            q = pe.deref(pp - pe.base)
            if q is not None:
                ti = pe.typeinfo(q)
                parent = ti[1] if ti else None
        return name, parent, unit, guid

    def guid_at(self, r):
        o = self.pe.r2o(r)
        return bytes(self.d[o:o + 16]) if o is not None else None

    def enums(self):
        """all tkEnumeration typeinfos: 'Name (Unit)' -> {name, unit, values{name: ord}}"""
        d = self.d
        res = {}
        for m in re.finditer(rb'\x03([\x02-\x40])', d):
            o = m.start()
            n = d[o + 1]
            name = d[o + 2:o + 2 + n]
            if not re.fullmatch(rb'[A-Za-z_][A-Za-z0-9_]*', name):
                continue
            p = o + 2 + n
            ordt = d[p]
            if ordt > 5:
                continue
            mn, mx = struct.unpack_from('<ii', d, p + 1)
            if not (0 <= mn <= mx < 2000):
                continue
            base = struct.unpack_from('<Q', d, p + 9)[0]
            if not (self.pe.base <= base < self.pe.base + 0x10000000):
                continue
            # only real enums list their own names (BaseType points back to this typeinfo)
            bt = self.pe.deref(base - self.pe.base)
            o_rva = self.pe_rva(o)
            if bt != o_rva:
                continue
            q = p + 17
            vals = {}
            ok = True
            for i in range(mn, mx + 1):
                ln = d[q]
                s = d[q + 1:q + 1 + ln]
                if not ln or not re.fullmatch(rb'[A-Za-z_][A-Za-z0-9_]*', s):
                    ok = False
                    break
                vals[s.decode('latin-1')] = i
                q += 1 + ln
            if not ok:
                continue
            ul = d[q]
            unit = d[q + 1:q + 1 + ul].decode('latin-1') if 0 < ul < 64 else None
            nm = name.decode('latin-1')
            if nm in ('Boolean', 'ByteBool', 'WordBool', 'LongBool'):
                continue
            res.setdefault('%s (%s)' % (nm, unit), {'name': nm, 'unit': unit, 'values': vals})
        return res

    def pe_rva(self, o):
        for va, sz, po, _ in self.pe.secs:
            if po <= o < po + sz:
                return o - po + va
        return None

    # ---------- registrar detection ----------
    def detect(self):
        def sh(a, k):
            x = a.get(k)
            return x[0] if x else None

        def meth(a, k):
            x = a.get(k)
            return bool(x) and x[0] == 'PTI' and x[1] == 'Method'

        preds = {
            'intf': lambda a, e: sh(a, 'rcx') == 'ADDR' and sh(a, 'rdx') == 'PTI' and a['rdx'][1] == 'Interface' and a.get('r8') is None,
            'imeth': lambda a, e: sh(a, 'rcx') == 'ADDR' and sh(a, 'rdx') == 'STR' and meth(a, 'r8'),
            'iprop': lambda a, e: sh(a, 'rcx') == 'ADDR' and sh(a, 'rdx') == 'STR' and sh(a, 'r8') == 'STR' and sh(a, 's20') == 'STR',
            'iidx': lambda a, e: sh(a, 'rcx') == 'ADDR' and sh(a, 'rdx') == 'STR' and sh(a, 'r8') == 'IMM' and sh(a, 's20') == 'STR' and sh(a, 's30') == 'STR',
            'cmeth': lambda a, e: sh(a, 'rcx') == 'PADDR' and sh(a, 'rdx') == 'STR' and meth(a, 'r8'),
            'proc': lambda a, e: sh(a, 'rdx') in ('STR', 'PSTR') and meth(a, 'r9'),
            'cprop': lambda a, e: sh(a, 'rcx') == 'PADDR' and sh(a, 'rdx') == 'STR' and sh(a, 'r8') == 'ADDR' and sh(a, 's20') == 'STR' and 's30' not in a,
            'cidx': lambda a, e: sh(a, 'rcx') == 'PADDR' and sh(a, 'rdx') == 'STR' and sh(a, 'r8') == 'IMM' and sh(a, 's30') == 'STR',
            'const': lambda a, e: sh(a, 'rcx') in ('PSTR', 'STR') and sh(a, 'rdx') == 'LOCAL' and e is not None,
            'var': lambda a, e: sh(a, 'rcx') == 'STR' and sh(a, 'rdx') == 'ADDR' and sh(a, 'r8') in ('ADDR', 'IMM') and a.get('r9') is None and 's20' not in a,
            'field': lambda a, e: sh(a, 'rcx') == 'PADDR' and sh(a, 'rdx') == 'STR' and sh(a, 'r8') == 'IMM' and a.get('r9') is None and 's20' not in a,
            'record': lambda a, e: sh(a, 'rcx') == 'PSTR' and sh(a, 'rdx') == 'ADDR' and a.get('r8') is None and a.get('r9') is None,
        }
        cnt = {k: collections.Counter() for k in preds}
        cnt['classes'] = collections.Counter()
        arrs = {}
        for a, t, args, e in self.recs:
            for k, p in preds.items():
                if p(args, e):
                    cnt[k][t] += 1
            if sh(args, 'rcx') == 'ADDR' and sh(args, 'rdx') == 'IMM' and args.get('r8') is None and 0 <= args['rdx'][1] < 5000:
                ca = self.class_array(args['rcx'][1], args['rdx'][1])
                if ca:
                    cnt['classes'][t] += len(ca)
                    arrs[a] = ca
        self.class_arrays = arrs
        roles = {}
        used = set()
        for k in ['imeth', 'intf', 'iprop', 'iidx', 'cmeth', 'proc', 'cprop', 'cidx', 'const', 'classes', 'record',
                  'var', 'field']:
            for t, n in cnt[k].most_common():
                if t not in used:
                    roles[k] = (t, n)
                    used.add(t)
                    break
        base = roles['imeth'][0]
        for k, (t, n) in list(roles.items()):
            if abs(t - base) > 0x8000:   # every registrar sits in the same unit
                print('warning: registrar %s at %x is far from %x (n=%d), ignored' % (k, t, base, n))
                del roles[k]
        self.roles = {k: t for k, (t, n) in roles.items()}
        return roles

    # ---------- signatures ----------
    @staticmethod
    def fmt_params(ps):
        out = []
        for fl, pn, tn in ps:
            pre = ''
            for bit, word in PF:
                if fl & bit:
                    pre = word + ' '
            ty = ('array of ' + tn) if fl & 4 else tn
            out.append('%s%s: %s' % (pre, pn, ty) if ty else pre + pn)
        return '; '.join(out)

    def sig_of(self, name, ti):
        ms = self.method_sig(ti) if ti is not None else None
        if not ms:
            return {'kind': 'method', 'params': None, 'result': None,
                    'decl': 'procedure %s; { signature not recoverable }' % name}
        mk, ps, res = ms
        p = self.fmt_params(ps)
        kind = 'function' if res is not None else 'procedure'
        decl = '%s %s%s%s;' % (kind, name, '(%s)' % p if p else '', ': ' + res if res is not None else '')
        return {'kind': kind, 'params': [[fl, pn, tn] for fl, pn, tn in ps], 'result': res, 'decl': decl}

    # ---------- constants ----------
    def const_value(self, e, bkind):
        if not e:
            return None, 'unknown'
        bt, bargs, bx = e
        kind = bkind.get(bt)
        rdx = bargs.get('rdx')
        r8 = bargs.get('r8')
        imm = rdx[1] if rdx and rdx[0] == 'IMM' else None
        if kind == 'int' and imm is not None:
            rng = r8[1] if r8 and r8[0] == 'IMM' else None
            v = imm
            if rng is not None and rng > 0:           # unsigned Byte/Word/Cardinal
                v &= (1 << (8 * rng)) - 1
            else:
                bits = 8 * abs(rng) if rng else 32
                v &= (1 << bits) - 1
                if v >= 1 << (bits - 1):
                    v -= 1 << bits
            return v, 'int'
        if kind == 'str':
            if rdx and rdx[0] in ('STR', 'PSTR'):
                return rdx[1], 'str'
            if imm == 0:
                return '', 'str'
        if kind == 'set' and rdx and rdx[0] in ('ADDR', 'PADDR') and r8 and r8[0] == 'IMM':
            o = self.pe.r2o(rdx[1])
            bs = self.d[o:o + r8[1]]
            return [i for i in range(r8[1] * 8) if bs[i // 8] >> (i % 8) & 1], 'set'
        if kind in ('float', 'date') and bx.get(1):
            x = bx[1]
            if x[0] == 'fmem':
                o = self.pe.r2o(x[1])
                return struct.unpack_from('<d' if x[2] == 8 else '<f', self.d, o)[0], kind
            if x[0] == 'fimm':
                return struct.unpack('<d', struct.pack('<Q', x[1] & (2 ** 64 - 1)))[0], kind
        if kind == 'bool' and imm is not None:
            return bool(imm & 0xFF), 'bool'
        if kind == 'int64' and imm is not None:
            v = imm & (2 ** 64 - 1)
            return (v - 2 ** 64 if v >= 2 ** 63 else v), 'int64'
        if kind == 'currency' and imm is not None:
            v = imm & (2 ** 64 - 1)
            v = v - 2 ** 64 if v >= 2 ** 63 else v
            return v / 10000, 'currency'
        return None, 'unknown'

    # ---------- build ----------
    def build(self):
        R = self.roles
        by = collections.defaultdict(list)
        for rec in self.recs:
            by[rec[1]].append(rec)
        g = lambda a, k: a.get(k)
        s_ = lambda a, k: a[k][1] if a.get(k) and a[k][0] in ('STR', 'PSTR') else None

        # interfaces
        guid2intf, intfs = {}, {}
        for a, t, args, e in by[R['intf']]:
            name, parent, unit, guid = self.intf_info(args['rdx'][3])
            guid2intf[self.guid_at(args['rcx'][1])] = name
            intfs.setdefault(name, {'unit': unit, 'parent': parent,
                                    'guid': '{%s}' % str(uuid.UUID(bytes_le=guid)).upper(),
                                    'methods': {}, 'props': {}})
        self.unresolved = collections.Counter()

        def owner(args):
            r = args.get('rcx')
            n = guid2intf.get(self.guid_at(r[1])) if r and r[0] == 'ADDR' else None
            if n is None:
                self.unresolved['interface owner'] += 1
            return n

        for a, t, args, e in by[R['imeth']]:
            n = owner(args)
            if n and s_(args, 'rdx'):
                r8 = args.get('r8')
                addm(intfs[n]['methods'], args['rdx'][1], self.sig_of(args['rdx'][1], r8[3] if r8 and r8[0] == 'PTI' else None))
        for a, t, args, e in by[R['iprop']]:
            n = owner(args)
            if n:
                intfs[n]['props'][args['rdx'][1]] = {'type': s_(args, 's20'), 'getter': s_(args, 'r8'),
                                                     'setter': s_(args, 'r9')}
        for a, t, args, e in by[R['iidx']]:
            n = owner(args)
            if n:
                intfs[n]['props'][args['rdx'][1]] = {
                    'type': s_(args, 's30'), 'getter': s_(args, 's20'), 'setter': s_(args, 's28'),
                    'nindex': args['r8'][1], 'default': bool(g(args, 'r9') and args['r9'][0] == 'IMM' and args['r9'][1])}
        # index parameters of indexed properties come from the getter's signature (searched up the chain)

        def find_method(iname, mname):
            seen = set()
            while iname in intfs and iname not in seen:
                seen.add(iname)
                if mname in intfs[iname]['methods']:
                    return intfs[iname]['methods'][mname][0]
                iname = intfs[iname]['parent']
            return None

        for n, it in intfs.items():
            for pn, p in it['props'].items():
                if 'nindex' in p:
                    gm = find_method(n, p['getter']) if p['getter'] else None
                    if gm and gm.get('params') is not None:
                        p['index'] = gm['params'][:p['nindex']]

        # classes
        classes = {}

        def cls_vmt(vmt):
            name, parent, unit, props = self.class_info(vmt)
            if not name:
                return None
            if name not in classes:
                classes[name] = {'unit': unit, 'parent': parent, 'registered': False, 'methods': {},
                                 'props': dict(props), 'fields': {}}
            return classes[name]

        def cls(args):
            r = args.get('rcx')
            return cls_vmt(r[1]) if r and r[0] == 'PADDR' else None

        if 'classes' in R:
            for a, t, args, e in by[R['classes']]:
                for vmt in self.class_arrays.get(a, []):
                    c = cls_vmt(vmt)
                    if c is not None:
                        c['registered'] = True
        for a, t, args, e in by[R['cmeth']]:
            c = cls(args)
            if c is not None and s_(args, 'rdx'):
                r8 = args.get('r8')
                addm(c['methods'], args['rdx'][1], self.sig_of(args['rdx'][1], r8[3] if r8 and r8[0] == 'PTI' else None))
        for a, t, args, e in by[R['cprop']]:
            c = cls(args)
            if c is not None:
                c['props'][args['rdx'][1]] = {'type': s_(args, 's20'),
                                              'readonly': not (g(args, 'r9') and args['r9'][0] == 'ADDR')}
        for a, t, args, e in by[R['cidx']]:
            c = cls(args)
            if c is not None:
                c['props'][args['rdx'][1]] = {'type': s_(args, 's30'), 'nindex': args['r8'][1],
                                              'readonly': not (g(args, 's28') and args['s28'][0] == 'ADDR'),
                                              'default': bool(g(args, 'r9') and args['r9'][0] == 'IMM' and args['r9'][1])}
        if 'field' in R:
            for a, t, args, e in by[R['field']]:
                c = cls(args)
                if c is not None:
                    c['fields'][args['rdx'][1]] = {'offset': args['r8'][1]}

        # global routines; the same registrar also takes class-level routines (constructors etc.)
        globs = {}
        for a, t, args, e in by[R['proc']]:
            nm = s_(args, 'rdx')
            if not nm:
                continue
            r9 = args.get('r9')
            m = self.sig_of(nm, r9[3] if r9 and r9[0] == 'PTI' else None)
            r = args.get('rcx')
            if r and r[0] == 'PADDR':
                c = cls(args)
                if c is not None:
                    addm(c['methods'], nm, m)
                    continue
            addm(globs, nm, m)
        records = sorted({s_(args, 'rcx') for a, t, args, e in by.get(R.get('record'), []) if s_(args, 'rcx')})

        # constants: builders of the Variant value are classified by majority shape, plus a few
        # RTL constants whose type is known (System/SysUtils) as anchors for the rare builders
        bcount = collections.defaultdict(collections.Counter)
        anchor = {'False': 'bool', 'True': 'bool', 'MaxComp': 'int64', 'EpochAsUnixDate': 'int64',
                  'MaxCurrency': 'currency', 'EpochAsJulianDate': 'currency', 'MaxDateTime': 'date',
                  'MinDateTime': 'date'}
        anchored = {}
        for a, t, args, e in by[R['const']]:
            if not e:
                continue
            bt, bargs, bx = e
            rdx, r8 = bargs.get('rdx'), bargs.get('r8')
            bcount[bt]['str'] += bool(rdx and rdx[0] in ('STR', 'PSTR'))
            bcount[bt]['int'] += bool(rdx and rdx[0] == 'IMM' and r8 and r8[0] == 'IMM')
            bcount[bt]['set'] += bool(rdx and rdx[0] in ('ADDR', 'PADDR') and r8 and r8[0] == 'IMM')
            bcount[bt]['float'] += bool(bx.get(1))
            nm = s_(args, 'rcx')
            if nm in anchor:
                anchored[bt] = anchor[nm]
        bkind = {}
        for kind in ('int', 'str', 'set', 'float'):
            best = max(bcount, key=lambda b: bcount[b][kind])
            if bcount[best][kind]:
                bkind[best] = kind
        for bt, kind in anchored.items():
            bkind.setdefault(bt, kind)
        creg = collections.defaultdict(list)
        for a, t, args, e in sorted(by[R['const']], key=lambda r: r[0]):
            nm = s_(args, 'rcx')
            if nm:
                creg[nm].append(self.const_value(e, bkind))
        # enumerations: tie each constant value to the enum types (name + unit) that define it
        enums = self.enums()
        owner_enum = collections.defaultdict(list)
        for en, info in enums.items():
            for vn, ov in info['values'].items():
                owner_enum[vn].append((en, ov))
        used_enums = {}

        def enum_of(nm, v):
            if v[1] != 'int':
                return []
            ens = sorted(en for en, ov in owner_enum.get(nm, []) if ov == v[0])
            for en in ens:
                used_enums.setdefault(en, enums[en])
            return ens

        # the first registration (lowest address) is the one scripts see: checked in AD23 on all
        # 18 names registered with different values
        consts = {}
        for nm, vals in creg.items():
            uniq = []
            for v in vals:
                if v not in uniq:
                    uniq.append(v)
            c = {'value': uniq[0][0], 'vkind': uniq[0][1], 'enum': enum_of(nm, uniq[0])}
            if len(uniq) > 1:
                c['other_values'] = [{'value': v[0], 'enum': enum_of(nm, v)} for v in uniq[1:]]
            consts[nm] = c

        vars_ = {}
        for a, t, args, e in by.get(R.get('var'), []):
            nm = s_(args, 'rcx')
            if nm:
                vars_[nm] = {'readonly': not (args.get('r8') and args['r8'][0] == 'ADDR')}

        return {'interfaces': intfs, 'classes': classes, 'globals': globs, 'records': records,
                'constants': consts, 'enums': used_enums, 'variables': vars_}



def main():
    src, out = sys.argv[1], sys.argv[2]
    dll = os.path.join(src, 'System', 'ScriptingSystem.dll') if os.path.isdir(src) else src
    ex = Extractor(dll)
    ex.collect()
    roles = ex.detect()
    print('registrars:', {k: '%x (%d)' % v for k, v in roles.items()})
    api = ex.build()
    install = os.path.dirname(os.path.dirname(os.path.abspath(dll)))
    api['source'] = {
        'dll': os.path.abspath(dll),
        'dll_size': os.path.getsize(dll),
        'dll_sha256': hashlib.sha256(ex.d).hexdigest(),
        'altium_version': altium_build(install),
        'extracted': datetime.date.today().isoformat(),
        'registrars': {k: '%x' % t for k, (t, n) in roles.items()},
    }
    I, C = api['interfaces'], api['classes']
    print('altium', api['source']['altium_version'])
    print('interfaces %d (methods %d, props %d)' % (len(I), sum(len(i['methods']) for i in I.values()),
                                                   sum(len(i['props']) for i in I.values())))
    print('classes %d (registered %d; methods %d, props %d)' % (
        len(C), sum(c['registered'] for c in C.values()), sum(len(c['methods']) for c in C.values()),
        sum(len(c['props']) for c in C.values())))
    print('globals %d, records %d, constants %d (enums %d), variables %d' % (
        len(api['globals']), len(api['records']), len(api['constants']), len(api['enums']), len(api['variables'])))
    print('constant kinds', dict(collections.Counter(c['vkind'] for c in api['constants'].values())))
    print('unresolved', dict(ex.unresolved))
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(api, f, ensure_ascii=False, separators=(',', ':'))


if __name__ == '__main__':
    main()
