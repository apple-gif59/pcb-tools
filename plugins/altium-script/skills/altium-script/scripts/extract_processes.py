r"""Extract the process (command) names and their parameter strings from an AD install.

Usage: python -X utf8 extract_processes.py <AD install dir> <out processes.json>

Two sources under <install>\System, neither complete on its own:
  *.ins  every server's declared commands (Command Name = 'Zoom' LongSummary = '...'), no parameters
  *.rcs  menus, toolbars and shortcuts (Command='PCB:Zoom' ... Params='Action = All|Target=Document'),
         i.e. every parameter combination the UI itself sends; some commands appear only here
Standard library only.
"""
import sys, os, re, glob, json, datetime


def norm(p):
    return re.sub(r'\s*([=|])\s*', r'\1', p.strip())


def altium_build(install):
    """FullBuild of the install from HKLM/SOFTWARE/Altium/Builds (the exe has no version resource)"""
    try:
        import winreg
        root = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Altium\Builds')
        i = 0
        while True:
            try:
                sub = winreg.EnumKey(root, i)
            except OSError:
                break
            i += 1
            k = winreg.OpenKey(root, sub)
            try:
                path = winreg.QueryValueEx(k, 'ProgramsInstallPath')[0]
                if os.path.normcase(os.path.abspath(path)) == os.path.normcase(install):
                    return winreg.QueryValueEx(k, 'FullBuild')[0]
            except OSError:
                pass
    except OSError:
        pass
    return None


def main():
    install, out = sys.argv[1], sys.argv[2]
    sysdir = os.path.join(install, 'System')
    cmds = {}        # lower 'srv:cmd' -> entry
    servers = {}     # lower srv -> spelling from .ins

    def entry(srv, cmd):
        k = (srv + ':' + cmd).lower()
        if k not in cmds:
            cmds[k] = {'name': '%s:%s' % (servers.get(srv.lower(), srv), cmd), 'summary': '', 'ins': False,
                       'params': [], 'captions': []}
        return cmds[k]

    for f in sorted(glob.glob(os.path.join(sysdir, '*.ins'))):
        t = open(f, encoding='latin-1').read()
        m = re.search(r"EditorName\s*=\s*'([^']+)'", t)
        srv = m.group(1) if m else os.path.basename(f)[:-4]
        servers[srv.lower()] = srv
        for c, s in re.findall(r"Command\s+Name\s*=\s*'([^']+)'\s*(?:LongSummary\s*=\s*'([^']*)')?", t):
            e = entry(srv, c)
            e['ins'], e['summary'] = True, e['summary'] or s.strip()
    for f in sorted(glob.glob(os.path.join(sysdir, '*.rcs'))):
        for line in open(f, encoding='latin-1'):
            m = re.search(r"Command='([^':@]+):([^']+)'", line)   # '@PLSCH:...' refers to another menu item
            if not m:
                continue
            e = entry(m.group(1), m.group(2))
            p = re.search(r"Params='([^']*)'", line)
            p = norm(p.group(1)) if p else ''
            if p and p not in e['params']:
                e['params'].append(p)
            c = re.search(r"Caption='([^']*)'", line)
            c = c.group(1).replace('&', '').strip() if c else ''
            if c and c not in e['captions']:
                e['captions'].append(c)

    res = {'commands': {e['name']: e for e in sorted(cmds.values(), key=lambda e: e['name'].lower())},
           'source': {'system_dir': os.path.abspath(sysdir), 'altium_version': altium_build(os.path.abspath(install)),
                      'extracted': datetime.date.today().isoformat()}}
    for e in res['commands'].values():
        del e['name']
        e['params'].sort(key=str.lower)
    n = res['commands']
    print('altium', res['source']['altium_version'])
    print('commands %d (in .ins %d, only in .rcs %d), with parameters %d' % (
        len(n), sum(e['ins'] for e in n.values()), sum(not e['ins'] for e in n.values()),
        sum(bool(e['params']) for e in n.values())))
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(res, f, ensure_ascii=False, indent=0)


if __name__ == '__main__':
    main()
