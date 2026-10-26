"""PE section mapping plus the Delphi RTTI / string-literal readers the extractor needs."""
import re, struct, pefile

TK = ['Unknown', 'Integer', 'Char', 'Enumeration', 'Float', 'String', 'Set', 'Class', 'Method', 'WChar',
      'LString', 'WString', 'Variant', 'Array', 'Record', 'Interface', 'Int64', 'DynArray', 'UString',
      'ClassRef', 'Pointer', 'Procedure', 'MRecord']
IDENT = re.compile(rb'[A-Za-z_][A-Za-z0-9_.<>,]*\Z')


class PE:
    def __init__(self, path):
        self.pe = pefile.PE(path, fast_load=True)
        self.d = self.pe.__data__
        self.base = self.pe.OPTIONAL_HEADER.ImageBase
        self.secs = [(s.VirtualAddress, s.SizeOfRawData, s.PointerToRawData, s.Name.rstrip(b'\0').decode())
                     for s in self.pe.sections]
        t = [s for s in self.secs if s[3] == '.text'][0]
        self.text_rva, self.text_size, self.text_off = t[0], t[1], t[2]

    def r2o(self, r):
        for va, sz, po, _ in self.secs:
            if va <= r < va + sz:
                return r - va + po
        return None

    def q(self, r):
        o = self.r2o(r)
        return struct.unpack_from('<Q', self.d, o)[0] if o is not None else None

    def deref(self, r):
        """rva of the pointer stored at rva r, or None"""
        v = self.q(r)
        if v and self.base <= v < self.base + 0x10000000:
            return v - self.base
        return None

    def ss(self, o):
        n = self.d[o]
        return self.d[o + 1:o + 1 + n].decode('latin-1'), o + 1 + n

    def ustr(self, r):
        """Delphi string literal (UnicodeString, or AnsiString/UTF8String) whose data starts at rva r"""
        o = self.r2o(r)
        if o is None or o < 12:
            return None
        h = self.d[o - 12:o - 4]
        if h[4:] != b'\xff\xff\xff\xff':
            return None
        n = struct.unpack_from('<i', self.d, o - 4)[0]
        if not 0 <= n < 100000:
            return None
        if h[:4] == b'\xb0\x04\x02\x00':
            return self.d[o:o + 2 * n].decode('utf-16-le', 'replace')
        if h[2:4] == b'\x01\x00' and self.d[o + n] == 0:
            cp = struct.unpack_from('<H', h)[0]
            return self.d[o:o + n].decode('utf-8' if cp == 65001 else 'latin-1', 'replace')
        return None

    def typeinfo(self, r):
        """(kind, name) if rva r looks like a PTypeInfo"""
        o = self.r2o(r)
        if o is None:
            return None
        k = self.d[o]
        if k >= len(TK):
            return None
        n = self.d[o + 1]
        name = self.d[o + 2:o + 2 + n]
        if not name or not IDENT.match(name):
            return None
        return TK[k], name.decode('latin-1')

