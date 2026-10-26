import sys, re, olefile

# usage: pcbdoc_heights.py <PcbLib> <PcbDoc> <out.txt>
# Reads HEIGHT from the saved files (not from AD memory).
lib_path, pcb_path, out = sys.argv[1:4]
lines = []

ole = olefile.OleFileIO(lib_path)
lib = {}
for entry in ole.listdir():
    if len(entry) == 2 and entry[1] == 'Parameters':
        data = ole.openstream(entry).read()
        txt = data[4:].decode('latin-1', 'replace')
        kv = dict(p.split('=', 1) for p in txt.strip('\x00|').split('|') if '=' in p)
        name = kv.get('PATTERN') or entry[0]
        lib[name] = kv.get('HEIGHT', '')
ole.close()
for k in sorted(lib):
    lines.append(f'LIB\t{k}\t{lib[k]}')

ole = olefile.OleFileIO(pcb_path)
data = ole.openstream(['Components6', 'Data']).read()
ole.close()
pos = 0
n = 0
while pos + 4 <= len(data):
    ln = int.from_bytes(data[pos:pos + 4], 'little')
    rec = data[pos + 4:pos + 4 + ln].decode('latin-1', 'replace')
    pos += 4 + ln
    kv = dict(p.split('=', 1) for p in rec.strip('\x00|').split('|') if '=' in p)
    n += 1
    lines.append(f"PCB\t{kv.get('SOURCEDESIGNATOR', '?')}\t{kv.get('PATTERN', '?')}\t{kv.get('HEIGHT', '')}")
lines.insert(0, f'# lib footprints {len(lib)}, pcb components {n}')
open(out, 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
print(lines[0])
