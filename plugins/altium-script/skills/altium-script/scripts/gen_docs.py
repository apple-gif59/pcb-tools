"""Render data/api.json into references/api/*.md.

Usage: python -X utf8 gen_docs.py <api.json> <out dir>
"""
import sys, os, json, collections

RO = '  // read-only'


def fmt_str(s):
    out, buf = [], ''
    for ch in s:
        if ch == "'":
            buf += "''"
        elif ord(ch) < 32 or ord(ch) == 127:
            if buf:
                out.append("'%s'" % buf)
                buf = ''
            out.append('#%d' % ord(ch))
        else:
            buf += ch
    if buf or not out:
        out.append("'%s'" % buf)
    return ''.join(out)


def fmt_set(bits):
    if not bits:
        return '[]'
    rs, a = [], bits[0]
    prev = a
    for b in bits[1:] + [None]:
        if b is not None and b == prev + 1:
            prev = b
            continue
        rs.append(str(a) if a == prev else '%d..%d' % (a, prev))
        if b is not None:
            a = prev = b
    return '[%s]' % ', '.join(rs)


def fmt_val(v, kind):
    if kind == 'str':
        return fmt_str(v)
    if kind == 'set':
        return fmt_set(v)
    if kind == 'bool':
        return 'True' if v else 'False'
    if kind == 'unknown' or v is None:
        return '?'
    if kind == 'float' or kind == 'date' or kind == 'currency':
        return repr(v)
    return str(v)


def params_txt(ps):
    out = []
    for fl, pn, tn in ps:
        pre = 'var ' if fl & 1 else 'const ' if fl & 2 else 'out ' if fl & 32 else ''
        out.append('%s%s: %s' % (pre, pn, ('array of ' + tn) if fl & 4 else tn))
    return '; '.join(out)


def intf_prop(n, p):
    idx = ''
    if 'nindex' in p:
        idx = '[%s]' % (params_txt(p['index']) if p.get('index') else ', '.join(['?'] * (p['nindex'] or 1)))
    s = 'property %s%s: %s' % (n, idx, p['type'])
    if p.get('getter'):
        s += ' read ' + p['getter']
    if p.get('setter'):
        s += ' write ' + p['setter']
    s += ';'
    if p.get('default'):
        s += ' default;'
    if not p.get('setter'):
        s += RO
    return s


def class_prop(n, p):
    idx = ''
    if 'nindex' in p:
        idx = '[%s]' % ', '.join(['Index%s: ?' % (i + 1 if p['nindex'] > 1 else '') for i in range(p['nindex'] or 1)])
    s = 'property %s%s: %s;' % (n, idx, p['type'])
    if p.get('default'):
        s += ' default;'
    if p.get('readonly'):
        s += RO
    return s


def chain(tbl, n):
    out = []
    while n and n not in out:
        out.append(n)
        n = tbl[n]['parent'] if n in tbl else None
    return out


def write(path, lines):
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')


def main():
    api = json.load(open(sys.argv[1], encoding='utf-8'))
    out = sys.argv[2]
    os.makedirs(out, exist_ok=True)
    I, C, G, K = api['interfaces'], api['classes'], api['globals'], api['constants']
    src = api['source']
    stamp = '来源：Altium Designer %s 的 `System\\ScriptingSystem.dll`（脚本引擎的注册表，%s 提取）。由 `scripts/gen_docs.py` 生成，不要手改。' % (
        src.get('altium_version') or '?', src['extracted'])

    def group(n):
        u = (I[n]['unit'] or '').lower()
        if u == 'rt_pcb' or n.startswith('IPCB_'):
            return 'PCB'
        if u == 'rt_schematic' or n.startswith('ISch_'):
            return 'SCH'
        return 'Other'

    files = {'PCB': 'PCB_Interfaces.md', 'SCH': 'SCH_Interfaces.md', 'Other': 'Other_Interfaces.md'}
    titles = {'PCB': 'PCB 接口（IPCB_*，单元 RT_PCB）', 'SCH': '原理图接口（ISch_*，单元 Rt_Schematic）',
              'Other': '其他接口（工作区、客户端/服务器、项目、库、FPGA 等）'}
    where = {}
    for gk in files:
        names = sorted(n for n in I if group(n) == gk)
        L = ['# ' + titles[gk], '', stamp, '',
             '每节列出该接口**自己注册的**成员；继承来的成员在父接口那一节（`继承` 一行给出链）。'
             '查某个接口的全部成员（含继承）用 `scripts/lookup.py <接口名>`。',
             '属性写成 `read <getter> write <setter>`，没有 `write` 的是只读属性（行尾 `// read-only`），不要赋值（`IPCB_Board.LayerColor` 赋值实测会卡死执行器）。'
             'getter/setter 本身也是注册过的方法，可以直接调用。', '']
        for n in names:
            it = I[n]
            where[n] = files[gk]
            ch = chain(I, n)
            L.append('## %s' % n)
            L.append('继承：%s ｜ 单元：%s ｜ 自有 %d 个方法、%d 个属性' % (
                ' → '.join(ch), it['unit'], len(it['methods']), len(it['props'])))
            L.append('')
            for pn in sorted(it['props'], key=str.lower):
                L.append(intf_prop(pn, it['props'][pn]))
            for mn in sorted(it['methods'], key=str.lower):
                for m in it['methods'][mn]:
                    L.append(m['decl'])
            L.append('')
        write(os.path.join(out, files[gk]), L)

    # classes
    L = ['# 类', '', stamp, '',
         '每节列出该类自己的成员：显式注册的方法/属性，加上 RTTI 里的 published 属性（窗体控件的属性、事件都在这里）。'
         '继承成员在父类那一节；不在本文件里的父类（如 TObject）没有向脚本单独注册成员。'
         '带下标的类属性只知道下标个数，不知道类型（写成 `Index: ?`）。', '']
    for n in sorted(C, key=str.lower):
        c = C[n]
        ch = chain(C, n)
        L.append('## %s' % n)
        L.append('继承：%s ｜ 单元：%s%s' % (' → '.join(ch + ([c['parent']] if c['parent'] and c['parent'] not in C else [])),
                                       c['unit'], '' if c['registered'] else ' ｜ 未在类列表里注册，只能通过实例访问'))
        L.append('')
        for pn in sorted(c['props'], key=str.lower):
            L.append(class_prop(pn, c['props'][pn]))
        for fn in sorted(c['fields'], key=str.lower):
            L.append('field %s;' % fn)
        for mn in sorted(c['methods'], key=str.lower):
            for m in c['methods'][mn]:
                L.append(m['decl'])
        L.append('')
    write(os.path.join(out, 'Classes.md'), L)

    # global routines, records, variables
    fn = sorted((n for n in G if any(m['kind'] == 'function' for m in G[n])), key=str.lower)
    pr = sorted((n for n in G if n not in fn), key=str.lower)
    L = ['# 全局函数、过程、记录类型和变量', '', stamp, '', '## 函数（%d）' % len(fn), '']
    for n in fn:
        for m in G[n]:
            L.append(m['decl'])
    L += ['', '## 过程（%d）' % len(pr), '']
    for n in pr:
        for m in G[n]:
            L.append(m['decl'])
    L += ['', '## 记录类型（%d）' % len(api['records']), '',
          '向脚本注册过的记录类型（多为 Windows 消息和 VCL 内部记录），名字可以当类型用。', '']
    L += [', '.join(api['records'][i:i + 8]) for i in range(0, len(api['records']), 8)]
    L += ['', '## 全局变量（%d）' % len(api['variables']), '']
    for n in sorted(api['variables'], key=str.lower):
        L.append('var %s;%s' % (n, RO if api['variables'][n]['readonly'] else ''))
    write(os.path.join(out, 'Global_Functions.md'), L)

    # constants
    E = api['enums']
    L = ['# 常量和枚举', '', stamp, '',
         '值都是脚本里实际拿到的值。集合常量写成元素序号的集合（如 `[1..32]`）。', '',
         '## 同名常量冲突', '',
         '下面这些名字被不同单元注册了不同的值，脚本里只能拿到第一个值（AD23 实测）。'
         '不能按枚举定义推断它传给某个函数或属性后的效果：PCB 的 `TUnit` 定义是 eImperial = 1，'
         '但实测 `CoordUnitToString(C, eImperial)`（脚本里 eImperial = 0）输出的是 mil，结果正确。用到这些名字时，先在 AD 里用小脚本确认效果。', '',
         '| 常量 | 脚本里的值 | 来自 | 其他单元里的值 |', '|---|---|---|---|']
    for n in sorted(K, key=str.lower):
        c = K[n]
        if 'other_values' in c:
            others = '；'.join('%s（%s）' % (fmt_val(o['value'], c['vkind']), '、'.join(o['enum']) or '无枚举')
                              for o in c['other_values'])
            L.append('| `%s` | %s | %s | %s |' % (n, fmt_val(c['value'], c['vkind']), '、'.join(c['enum']) or '—', others))
    L += ['', '## 枚举类型', '',
          '只列出至少有一个元素作为常量注册了的枚举。元素后面标 `// 脚本里不可用` 的没注册成常量；'
          '标 `// 脚本里是 N` 的名字被别的单元占用了（见上表）。', '']
    for en in sorted(E, key=str.lower):
        e = E[en]
        L.append('### %s' % en)
        L.append('')
        for vn, ov in sorted(e['values'].items(), key=lambda x: x[1]):
            c = K.get(vn)
            note = ''
            if c is None:
                note = '  // 脚本里不可用'
            elif c['vkind'] != 'int' or c['value'] != ov:
                note = '  // 脚本里是 %s' % fmt_val(c['value'], c['vkind'])
            L.append('%s = %d%s' % (vn, ov, note))
        L.append('')
    rest = sorted((n for n in K if not K[n]['enum']), key=str.lower)
    L += ['## 其他常量（%d）' % len(rest), '', '不属于任何枚举类型的常量，按首字母分组。', '']
    cur = None
    for n in rest:
        h = n[0].upper()
        if h != cur:
            L += ['', '### %s' % h, '']
            cur = h
        c = K[n]
        L.append('%s = %s' % (n, fmt_val(c['value'], c['vkind'])))
    write(os.path.join(out, 'Constants.md'), L)

    # map / index
    units = collections.defaultdict(list)
    for n in I:
        units[I[n]['unit']].append(n)
    L = ['# API 总览', '', stamp, '',
         '| 内容 | 数量 | 文件 |', '|---|---|---|',
         '| 接口 | %d（方法 %d、属性 %d） | PCB_Interfaces.md / SCH_Interfaces.md / Other_Interfaces.md |' % (
             len(I), sum(len(i['methods']) for i in I.values()), sum(len(i['props']) for i in I.values())),
         '| 类 | %d（方法 %d、属性 %d） | Classes.md |' % (
             len(C), sum(len(c['methods']) for c in C.values()), sum(len(c['props']) for c in C.values())),
         '| 全局函数/过程 | %d | Global_Functions.md |' % len(G),
         '| 记录类型 / 全局变量 | %d / %d | Global_Functions.md |' % (len(api['records']), len(api['variables'])),
         '| 常量 / 枚举类型 | %d / %d | Constants.md |' % (len(K), len(E)), '',
         '## 接口一览（按单元）', '', '格式：`接口 : 父接口（自有方法数/属性数）`。', '']
    for u in sorted(units, key=lambda x: (-len(units[x]), str(x))):
        L.append('### %s（%d 个，见 %s）' % (u, len(units[u]), where[units[u][0]]))
        L.append('')
        for n in sorted(units[u], key=str.lower):
            it = I[n]
            L.append('- %s : %s（%d/%d）' % (n, it['parent'] or '-', len(it['methods']), len(it['props'])))
        L.append('')
    write(os.path.join(out, 'API_Map.md'), L)
    print('written to', out)


if __name__ == '__main__':
    main()
