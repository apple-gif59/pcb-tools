"""Query the AD script API (data/api.json) with inheritance resolved.

  python -X utf8 lookup.py IPCB_Track            all members of an interface/class, inherited ones included
  python -X utf8 lookup.py IPCB_Track.Layer      one member (searched up the parent chain); if absent, the subtypes
                                                 and other interfaces that have it
  python -X utf8 lookup.py PCBServer.GetCurrentPCBBoard.LayerColor
                                                 a call chain: the head may be a global function returning an
                                                 interface; each member's type leads to the next
  python -X utf8 lookup.py ShowMessage           a global routine, constant, variable, record or enum type
  python -X utf8 lookup.py TCoord                a type name that only appears inside signatures
  python -X utf8 lookup.py Inc                   a language built-in the official examples call (not in the registry)
  python -X utf8 lookup.py PCB:Zoom              a process (RunProcess / Client.SendMessage) and the parameters AD's menus pass it
  python -X utf8 lookup.py -s "Layer.*Color"     regex search over every name (members and class fields, tried both bare
                                                 and as Owner.Member; globals, constants, enum and record types,
                                                 processes and their menu captions)

Exit code: 0 found (also Client.SendMessage and SchServer.ProcessControl, which are only on another interface but
were run successfully in AD23), 1 not found or only on another interface, 2 bad or missing arguments.
"""
import sys, os, re, json, difflib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_docs import intf_prop, class_prop, fmt_val

SKILL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(SKILL, 'data')
api = json.load(open(os.path.join(DATA, 'api.json'), encoding='utf-8'))
P = json.load(open(os.path.join(DATA, 'processes.json'), encoding='utf-8'))['commands']
I, C, G, K, E = api['interfaces'], api['classes'], api['globals'], api['constants'], api['enums']
ci = lambda tbl: {k.lower(): k for k in tbl}
Ii, Ci, Gi, Ki, Pi = ci(I), ci(C), ci(G), ci(K), ci(P)

# names the examples call that the engine's registry doesn't have: handled by the DelphiScript language itself.
# Each one has code uses in references/scripts (comments, strings and Obj.X calls excluded); all but Result
# were run in the AD23 sandbox (Result needs a function of one's own, which a statement body can't declare).
BUILTINS = ('Abs', 'Assigned', 'Break', 'Copy', 'Dec', 'Delete', 'Exit', 'Inc', 'Include', 'Length', 'Nil', 'Ord',
            'Result', 'Round', 'Trunc')
UNTESTED = ('Result',)
SANDBOX_NOTE = {
    'Exit': 'run_altium_script 的语句体里不要用：它直接离开沙盒的 Run 过程，结果不写盘，MCP 等满 timeout_seconds '
            '后报 no result 并自动恢复（实测）。要跳过后面的语句用 if/else。',
    'Result': '只能在函数里用；run_altium_script 只接受语句体，不能声明函数，那里没有 Result。',
}

# members that aren't on the declared type but altium-mcp ran successfully in AD23 -> the interface it resolves to
MEASURED = {('iclient', 'sendmessage'): 'IProcessLauncher', ('isch_serverinterface', 'processcontrol'): 'IClient'}
# members that aren't on the declared type and were tried in AD23 without success
KNOWN_FAIL = {('isch_document', 'filename'): 'AD23 实测读 ISch_Document.FileName 会报错。'
                                             '原理图文档的完整路径用 DocumentName（实测）。'}
# set elements the dictionary shows as bare ordinals; passed on their own they mean a different set
CONST_NOTE = {
    'rfReplaceAll': '这是集合 TReplaceFlags 的元素（序号 0）。StringReplace 的 Flags 要写 MkSet(rfReplaceAll)；'
                    '直接传 rfReplaceAll 等于传空集合，只替换第一处，不报错（AD23 实测）。沙盒里也可以用常量 REPLACEALL（= 1）。',
    'rfIgnoreCase': '这是集合 TReplaceFlags 的元素（序号 1）。StringReplace 的 Flags 要写 MkSet(rfIgnoreCase)；'
                    '直接传 rfIgnoreCase（= 1）等于传 MkSet(rfReplaceAll)。',
}


def table_of(name):
    n = name.lower()
    if n in Ii:
        return I, Ii[n], intf_prop
    if n in Ci:
        return C, Ci[n], class_prop
    return None, None, None


def chain(tbl, n):
    out = []
    while n and n in tbl and n not in out:
        out.append(n)
        n = tbl[n]['parent']
    return out


def is_ctor(tbl, m):
    return tbl is C and m.lower() == 'create'


def decls(tbl, m, ds):
    """method declarations; a class's Create is its constructor (RTTI registers it as a procedure)"""
    if is_ctor(tbl, m):
        return [re.sub(r'^procedure\b', 'constructor', d['decl']) for d in ds]
    return [d['decl'] for d in ds]


def member_lines(tbl, n, fmtp):
    t = tbl[n]
    out = [fmtp(p, t['props'][p]) for p in sorted(t['props'], key=str.lower)]
    out += ['field %s;' % f for f in sorted(t.get('fields', {}), key=str.lower)]
    for m in sorted(t['methods'], key=str.lower):
        out += decls(tbl, m, t['methods'][m])
    return out


def find_member(tbl, n, mem, fmtp):
    """(defining type, member name as registered, declarations), or Nones"""
    ml = mem.lower()
    for x in chain(tbl, n):
        t = tbl[x]
        for p in t['props']:
            if p.lower() == ml:
                return x, p, [fmtp(p, t['props'][p])]
        for m in t['methods']:
            if m.lower() == ml:
                return x, m, decls(tbl, m, t['methods'][m])
        for f in t.get('fields', {}):
            if f.lower() == ml:
                return x, f, ['field %s;' % f]
    return None, None, None


def member_type(tbl, owner, mem):
    """type a member yields: a property's type or a function's result (None for procedures and fields)"""
    t, ml = tbl[owner], mem.lower()
    for p, v in t['props'].items():
        if p.lower() == ml:
            return v['type']
    for m, ds in t['methods'].items():
        if m.lower() == ml:
            return next((d['result'] for d in ds if d.get('result')), None)
    return None


def definers(mem):
    """every interface/class that itself defines mem: (table, owner, member name, first declaration)"""
    rows = []
    for t2, f2 in ((I, intf_prop), (C, class_prop)):
        for o in sorted(t2, key=str.lower):
            y, m, l2 = find_member(t2, o, mem, f2)
            if y == o:
                rows.append((t2, o, m, l2[0]))
    return rows


def subtype_definers(tbl, n, mem, fmtp):
    """types below n that have mem, grouped by the type that defines it (n's own chain is known not to have it):
    (table, definer, member name, declaration, the definer's descendants that inherit it)"""
    rows, heirs = {}, {}
    for d in sorted(tbl, key=str.lower):
        if d != n and n in chain(tbl, d):
            x, m, lines = find_member(tbl, d, mem, fmtp)
            if x is not None:
                rows.setdefault(x, (tbl, x, m, lines[0]))
                if d != x:
                    heirs.setdefault(x, []).append(d)
    return [rows[x] + (heirs.get(x, []),) for x in sorted(rows, key=str.lower)]


def print_rows(rows, limit=15):
    for r in rows[:limit]:
        print('  %s.%s  %s' % r[1:4])
        if len(r) > 4 and r[4]:
            print('      继承它的：%s%s' % ('、'.join(r[4][:12]), '……共 %d 个' % len(r[4]) if len(r[4]) > 12 else ''))
    if len(rows) > limit:
        print('  ……共 %d 个，全部列出用 lookup -s "^%s$"' % (len(rows), rows[0][2]))


def missing_member(tbl, n, mem, fmtp):
    """explain a member that n's chain doesn't have; returns (candidate definers, whether they are n's subtypes)"""
    print('%s 及其父类型（%s）里都没有 %s。' % (n, ' → '.join(chain(tbl, n)), mem))
    if (n.lower(), mem.lower()) in KNOWN_FAIL:
        print(KNOWN_FAIL[n.lower(), mem.lower()])
        return [], False
    sub = subtype_definers(tbl, n, mem, fmtp)
    if sub:
        print('%s 的下层类型里有。迭代器、工厂返回的常是基类型（FirstPCBObject、PCBObjectFactory 返回 IPCB_Primitive，'
              'FirstSchObject、SchObjectFactory 返回 ISch_BasicContainer），对象实际是下面某个类型，'
              '改查具体类型（lookup <类型>.%s）。定义它的类型和继承它的类型：' % (n, sub[0][2]))
        print_rows(sub)
        return sub, True
    rows = definers(mem)
    if rows:
        pre = n.split('_')[0].lower()
        rows.sort(key=lambda r: (r[1].split('_')[0].lower() != pre, r[1].lower()))
        via = MEASURED.get((n.lower(), mem.lower()))
        if via:
            print('别的接口上有同名成员。这个写法 altium-mcp 在 AD23 上实测能用，不用再试；'
                  '按 %s 上的签名写：' % via)
            rows.sort(key=lambda r: r[1] != via)
        else:
            print('别的接口/类上有同名成员。对象如果也实现了其中某个接口，可能能用'
                  '（如 Client.SendMessage 实测能用，它注册在 IProcessLauncher 上），先在 AD 里试：')
        print_rows(rows)
    else:
        print('AD23 里没有任何接口或类有这个成员，脚本里不能用（读写不存在的成员报 Undeclared identifier）。')
    return rows, False


def show_member(q):
    parts = q.split('.')
    head = parts[0]
    tbl, n, fmtp = table_of(head)
    if tbl is None:
        g = Gi.get(head.lower())
        res = next((d['result'] for d in G[g] if not d['params'] and d.get('result')), None) if g else None
        if res:
            tbl, n, fmtp = table_of(res)
        if tbl is None:
            v = next((v for v in api['variables'] if v.lower() == head.lower()), None)
            if v:
                print('%s 是全局变量，字典里没有记它的类型，调用链从它开始查不下去。知道它是哪个类就直接查类的成员，'
                      '类名通常是 T 加变量名（Application 是 TApplication：lookup TApplication.Title）。' % v)
                return False
            print('%s 不是接口、类，也不是返回接口的全局函数。点号前写接口名（如 IPCB_Board.LayerColor），'
                  '或从全局函数开始写调用链（如 PCBServer.GetCurrentPCBBoard.LayerColor）。' % head)
            return False
        print('%s 是全局函数，返回 %s' % (g, n))
    unsure, assumed = [], []
    for i, mem in enumerate(parts[1:]):
        last = i == len(parts) - 2
        x, name, lines = find_member(tbl, n, mem, fmtp)
        if x is None:
            cands, is_sub = missing_member(tbl, n, mem, fmtp)
            known = (n.lower(), mem.lower()) in MEASURED
            if last or not cands:
                return known and bool(cands) and not unsure and not assumed
            # carry on only when every candidate leads to the same type
            types = {(member_type(r[0], r[1], r[2]) or '').lower() for r in cands}
            tbl2, n2, f2 = table_of(types.pop()) if len(types) == 1 else (None, None, None)
            if tbl2 is None:
                print('这些成员的类型不一致或不是接口，后面的 %s 查不下去。' % '.'.join(parts[i + 2:]))
                return False
            name = cands[0][2]
            print('（它们的类型都是 %s，按它接着查）' % n2)
            print('%s.%s → %s' % (n, name, n2))
            if is_sub:
                assumed.append('%s.%s' % (cands[0][1] if len(cands) == 1 else '<类型>', '.'.join(parts[i + 1:])))
            elif not known:
                unsure.append('%s.%s' % (n, name))
            tbl, n, fmtp = tbl2, n2, f2
            continue
        if last:
            print('%s.%s  （定义在 %s）' % (n, name, x))
            print('\n'.join(lines))
            if unsure:
                print('注意：%s 不在声明类型上，整条链只是可能能用，先在 AD 里试。' % '、'.join(unsure))
            if assumed:
                print('注意：这条链中间是按下层类型接着查的，对象确实是那个类型才成立。脚本里按具体类型写，'
                      '再查一次（lookup %s）。' % assumed[0])
            return not unsure and not assumed
        typ = n if is_ctor(tbl, name) else member_type(tbl, x, name)
        tbl2, n2, f2 = table_of(typ) if typ else (None, None, None)
        if tbl2 is None:
            print('%s.%s 的类型是 %s，不是接口或类，后面的 %s 查不下去。' % (n, name, typ or '（无返回值）', '.'.join(parts[i + 2:])))
            return False
        print('%s.%s → %s' % (n, name, n2))
        tbl, n, fmtp = tbl2, n2, f2


def type_names(d):
    """the type positions of a declaration: parameter types and the result"""
    return [p[2] for p in d['params'] or [] if p[2]] + ([d['result']] if d.get('result') else [])


def show_typename(name):
    """a type that is only referenced from signatures (TCoord, TLayer, ...): the engine registers no definition"""
    rx = re.compile(r'\b%s\b' % re.escape(name), re.I)
    uses = []
    for tbl, fmtp in ((I, intf_prop), (C, class_prop)):
        for n, t in tbl.items():
            uses += ['%s: %s' % (n, fmtp(p, v)) for p, v in t['props'].items() if rx.search(v.get('type') or '')]
            uses += ['%s: %s' % (n, d['decl']) for ds in t['methods'].values() for d in ds
                     if any(rx.search(x) for x in type_names(d))]
    uses += [d['decl'] for ds in G.values() for d in ds if any(rx.search(x) for x in type_names(d))]
    if not uses:
        return False
    print('%s 是签名里用到的类型名（%d 处），脚本引擎没有单独注册它，所以没有定义可查。'
          'DelphiScript 不检查变量的声明类型，完整脚本里声明变量时照写（X : %s）或不写类型都行。例如：' % (name, len(uses), name))
    print('\n'.join('  ' + u for u in uses[:3]))
    return True


def show_builtin(name):
    b = next((x for x in BUILTINS if x.lower() == name.lower()), None)
    if b is None:
        return False
    rx = re.compile(r'(?<![.\w])%s\b' % b, re.I)
    root = os.path.join(SKILL, 'references', 'scripts')
    if os.name == 'nt':
        root = '\\\\?\\' + root   # 插件缓存目录很深时，示例的长文件名会超过 260 字符
    files, first = 0, None
    for dp, dn, fn in os.walk(root):
        dn.sort()
        for f in sorted(fn):
            if not f.lower().endswith('.pas'):
                continue
            p = os.path.join(dp, f)
            txt = open(p, encoding='cp1252', errors='replace').read()
            txt = re.sub(r'\{[^}]*\}|\(\*.*?\*\)', lambda m: '\n' * m.group().count('\n'), txt, flags=re.S)
            for i, l in enumerate(txt.splitlines(), 1):
                if rx.search(re.sub(r"//.*|'[^']*'", '', l)):
                    files += 1
                    first = first or '%s:%d  %s' % (os.path.relpath(p, root), i, l.strip())
                    break
    print('%s 是 DelphiScript 语言自带的，不经过脚本引擎的注册表，所以字典里没有它。%s'
          '官方示例 %d 个文件在用，例如 %s' % (b, '' if b in UNTESTED else 'AD23 沙盒里实测过。', files, first))
    if b in SANDBOX_NOTE:
        print('注意：' + SANDBOX_NOTE[b])
    return True


def show_bare_member(name):
    """a bare name that exists only as a member (Width, DM_Compile): needs an object in front"""
    rows = definers(name)
    if not rows:
        return False
    print('%s 不是全局名字，是接口/类的成员，要写成 对象.%s。有这个成员的：' % (rows[0][2], rows[0][2]))
    print_rows(rows)
    return True


def const_line(n):
    c = K[n]
    s = '%s = %s' % (n, fmt_val(c['value'], c['vkind']))
    if c['enum']:
        s += '   { %s }' % ', '.join(c['enum'])
    for o in c.get('other_values', []):
        s += '\n  注意：另一个单元注册的值是 %s（%s），脚本里拿不到' % (fmt_val(o['value'], c['vkind']), ', '.join(o['enum']) or '无枚举')
    return s


def show_type(name):
    tbl, n, fmtp = table_of(name)
    if tbl is None:
        return False
    ch = chain(tbl, n)
    t = tbl[n]
    print('%s  继承：%s  单元：%s' % (n, ' → '.join(ch), t['unit']))
    for x in ch:
        lines = member_lines(tbl, x, fmtp)
        if not lines:
            continue
        print('\n[%s%s]' % (x, '' if x == n else '（继承）'))
        print('\n'.join(lines))
    return True


def show_name(name):
    found = False
    nl = name.lower()
    if nl in Gi:
        print('\n'.join(d['decl'] for d in G[Gi[nl]]))
        if any(p[1] == 'cArgs' for d in G[Gi[nl]] for p in d['params'] or []):
            print('可变参数函数：上面是它内部实现的签名，脚本里把参数逐个写在括号里%s。' % (
                '，如 MkSet(eTrackObject, eViaObject)' if Gi[nl] == 'MkSet'
                else '；它要什么参数字典里看不出，官方示例里也没有调用，用之前先在 AD 里试'))
        found = True
    if nl in Ki:
        print('const ' + const_line(Ki[nl]))
        if Ki[nl] in CONST_NOTE:
            print('注意：' + CONST_NOTE[Ki[nl]])
        found = True
    for v in api['variables']:
        if v.lower() == nl:
            print('var %s;%s' % (v, '  // read-only' if api['variables'][v]['readonly'] else ''))
            found = True
    for r in api['records']:
        if r.lower() == nl:
            print('record type %s' % r)
            found = True
    for en, e in E.items():
        if e['name'].lower() == nl:
            print('enum %s = (%s)' % (en, ', '.join('%s=%d' % kv for kv in sorted(e['values'].items(), key=lambda x: x[1]))))
            found = True
    return found


def show_process(q):
    k = Pi.get(q.lower())
    if k is None:
        print('AD23 的命令表（System\\*.ins）和菜单（System\\*.rcs）里都没有 %s。' % q)
        srv, cmd = (s.lower() for s in q.split(':', 1))
        near = [n for n in P if cmd in n.split(':', 1)[1].lower() or n.split(':', 1)[1].lower() in cmd]
        near = near or [Pi[n] for n in difflib.get_close_matches(q.lower(), Pi, 12)]
        near.sort(key=lambda n: (n.split(':', 1)[0].lower() != srv, n.lower()))
        if near:
            print('名字相近的：' + '、'.join(near[:12]))
        return False
    e = P[k]
    src = '.ins 命令表' if e['ins'] else '只在 .rcs 菜单里'
    print('%s  （%s）%s' % (k, src, '  ' + e['summary'] if e['summary'] else ''))
    if e['captions']:
        print('菜单项：' + ' / '.join(e['captions'][:10]))
    if e['params']:
        print('AD 菜单传的参数（%d 种，原样可用；菜单以外的参数要看示例或实测）：' % len(e['params']))
        print('\n'.join('  ' + p for p in e['params']))
    else:
        print('AD 菜单里调用它时不带参数。要带参数看示例脚本或实测。')
    return True


def search(pat):
    rx = re.compile(pat, re.I)
    hits = []
    for n, e in P.items():
        if rx.search(n) or any(rx.search(c) for c in e['captions']):
            hits.append('%s  （进程）%s' % (n, ' / '.join(e['captions'][:3])))
    mem = lambda n, m: rx.search(m) or rx.search(n + '.' + m)
    for tbl, fmtp in ((I, intf_prop), (C, class_prop)):
        for n, t in tbl.items():
            if rx.search(n):
                hits.append('%s  （%s）' % (n, '接口' if tbl is I else '类'))
            for p in t['props']:
                if mem(n, p):
                    hits.append('%s.%s  %s' % (n, p, fmtp(p, t['props'][p])))
            for f in t.get('fields', {}):
                if mem(n, f):
                    hits.append('%s.%s  field %s;' % (n, f, f))
            for m, ds in t['methods'].items():
                if mem(n, m):
                    hits += ['%s.%s  %s' % (n, m, d) for d in decls(tbl, m, ds)]
    for n, ds in G.items():
        if rx.search(n):
            hits += ['%s' % d['decl'] for d in ds]
    for n in K:
        if rx.search(n):
            hits.append('const ' + const_line(n))
    for n in api['variables']:
        if rx.search(n):
            hits.append('var %s;' % n)
    for en, e in E.items():
        if rx.search(e['name']):
            hits.append('enum %s' % en)
    for r in api['records']:
        if rx.search(r):
            hits.append('record type %s' % r)
    print('\n'.join(sorted(hits, key=str.lower)) or '没有匹配')
    print('-- %d 条' % len(hits))
    return len(hits)


def usage_error(msg):
    print(msg + '。用法见 lookup --help')
    sys.exit(2)


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(2)
    if args[0] in ('-h', '--help'):
        if len(args) > 1:
            usage_error('%s 后面不跟参数，多出来的参数：%s' % (args[0], ' '.join(args[1:])))
        print(__doc__)
        return
    if args[0] == '-s':
        if len(args) < 2 or not args[1]:
            usage_error('-s 后面要跟一个非空的正则，例如 lookup -s "Layer.*Color"')
        if len(args) > 2:
            usage_error('-s 只接受一个正则，多出来的参数：%s；正则里有空格要加引号' % ' '.join(args[2:]))
        try:
            n = search(args[1])
        except re.error as ex:
            print('正则写错了（%s）。要按字面搜特殊字符，前面加反斜杠，例如 \\[' % ex)
            sys.exit(2)
        sys.exit(0 if n else 1)
    if args[0].startswith('-'):
        usage_error('不认识的选项 %s，只有 -s 和 -h（--help）' % args[0])
    if len(args) > 1:
        usage_error('一次只查一个名字，多出来的参数：%s' % ' '.join(args[1:]))
    q = args[0].strip()
    if ':' in q:
        q = re.sub(r'\s*:\s*', ':', q)
        if not all(q.split(':', 1)):
            usage_error('进程名写成 服务器:命令，如 PCB:Zoom；列出一个服务器的全部进程用 lookup -s "^PCB:"')
        if not show_process(q):
            sys.exit(1)
        return
    if '.' in q:
        if not all(s.strip() for s in q.split('.')):
            usage_error('%s 里有空的一段，点号两边都要写名字，如 IPCB_Board.LayerColor' % q)
        if not show_member('.'.join(s.strip() for s in q.split('.'))):
            sys.exit(1)
        return
    if not q:
        usage_error('要查的名字是空的')
    if not (show_type(q) | show_name(q) or show_typename(q) or show_builtin(q)):
        if not show_bare_member(q):
            print('字典里没有叫 %s 的名字。沙盒预置的变量、过程和常量（ResultText、S1、Obj1、SandboxLog、REPLACEALL 等）'
                  '在 altium-mcp skill 里，本来就不在字典里；别的名字可能拼错了，用 -s 做模糊搜索。' % q)
        sys.exit(1)


if __name__ == '__main__':
    main()
