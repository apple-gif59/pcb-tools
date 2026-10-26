"""Minimal x64 decoder: instruction lengths for the whole ISA subset a Delphi compiler emits,
plus a tiny symbolic tracker for argument registers / stack slots at call sites."""
import struct

PREFIXES = {0xF0, 0xF2, 0xF3, 0x2E, 0x36, 0x3E, 0x26, 0x64, 0x65, 0x66, 0x67}

# one-byte opcode table: (has_modrm, imm_kind)  imm_kind: 0 none, 'b' 1, 'w' 2, 'z' 4/2, 'v' 8/4/2, 'rel8', 'rel32', 'moffs', 'iwb' 3, 'F6', 'F7'
OP1 = {}
for b in range(256):
    OP1[b] = None
for base in (0x00, 0x08, 0x10, 0x18, 0x20, 0x28, 0x30, 0x38):
    for k in range(4):
        OP1[base + k] = (True, 0)
    OP1[base + 4] = (False, 'b')
    OP1[base + 5] = (False, 'z')
for b in range(0x50, 0x60):
    OP1[b] = (False, 0)
OP1[0x63] = (True, 0)
OP1[0x68] = (False, 'z')
OP1[0x69] = (True, 'z')
OP1[0x6A] = (False, 'b')
OP1[0x6B] = (True, 'b')
for b in range(0x6C, 0x70):
    OP1[b] = (False, 0)
for b in range(0x70, 0x80):
    OP1[b] = (False, 'rel8')
OP1[0x80] = (True, 'b')
OP1[0x81] = (True, 'z')
OP1[0x83] = (True, 'b')
for b in range(0x84, 0x90):
    OP1[b] = (True, 0)
for b in range(0x90, 0xA0):
    OP1[b] = (False, 0)
OP1[0x9A] = None
for b in (0xA0, 0xA1, 0xA2, 0xA3):
    OP1[b] = (False, 'moffs')
for b in (0xA4, 0xA5, 0xA6, 0xA7, 0xAA, 0xAB, 0xAC, 0xAD, 0xAE, 0xAF):
    OP1[b] = (False, 0)
OP1[0xA8] = (False, 'b')
OP1[0xA9] = (False, 'z')
for b in range(0xB0, 0xB8):
    OP1[b] = (False, 'b')
for b in range(0xB8, 0xC0):
    OP1[b] = (False, 'v')
OP1[0xC0] = (True, 'b')
OP1[0xC1] = (True, 'b')
OP1[0xC2] = (False, 'w')
OP1[0xC3] = (False, 0)
OP1[0xC6] = (True, 'b')
OP1[0xC7] = (True, 'z')
OP1[0xC8] = (False, 'iwb')
OP1[0xC9] = (False, 0)
OP1[0xCA] = (False, 'w')
OP1[0xCB] = (False, 0)
OP1[0xCC] = (False, 0)
OP1[0xCD] = (False, 'b')
OP1[0xCF] = (False, 0)
for b in range(0xD0, 0xD4):
    OP1[b] = (True, 0)
OP1[0xD7] = (False, 0)
for b in range(0xD8, 0xE0):
    OP1[b] = (True, 0)
for b in range(0xE0, 0xE8):
    OP1[b] = (False, 'b')
OP1[0xE8] = (False, 'rel32')
OP1[0xE9] = (False, 'rel32')
OP1[0xEB] = (False, 'rel8')
for b in range(0xEC, 0xF0):
    OP1[b] = (False, 0)
for b in (0xF1, 0xF4, 0xF5, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD):
    OP1[b] = (False, 0)
OP1[0xF6] = (True, 'F6')
OP1[0xF7] = (True, 'F7')
OP1[0xFE] = (True, 0)
OP1[0xFF] = (True, 0)

OP2_NOMODRM = {0x05, 0x06, 0x07, 0x08, 0x09, 0x0B, 0x0E, 0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x37, 0x77,
               0xA0, 0xA1, 0xA2, 0xA8, 0xA9, 0xAA} | set(range(0xC8, 0xD0))
OP2_IMM8 = {0x70, 0x71, 0x72, 0x73, 0xA4, 0xAC, 0xBA, 0xC2, 0xC4, 0xC5, 0xC6, 0x0F}


class Insn:
    __slots__ = ('addr', 'len', 'op', 'map', 'rex', 'pfx', 'modrm', 'mod', 'reg', 'rm', 'base', 'index',
                 'disp', 'riprel', 'imm', 'opsize16')


def decode(d, off, addr):
    """decode one instruction at file offset off (rva addr). Returns Insn or None."""
    i = off
    pfx = []
    while d[i] in PREFIXES:
        pfx.append(d[i])
        i += 1
        if len(pfx) > 5:
            return None
    rex = 0
    if 0x40 <= d[i] <= 0x4F:
        rex = d[i]
        i += 1
    ins = Insn()
    ins.addr = addr
    ins.pfx = pfx
    ins.rex = rex
    ins.opsize16 = 0x66 in pfx
    b = d[i]
    i += 1
    if b == 0x0F:
        b2 = d[i]
        i += 1
        if b2 == 0x38:
            ins.map = 3
            ins.op = d[i]
            i += 1
            has_modrm, immk = True, 0
        elif b2 == 0x3A:
            ins.map = 4
            ins.op = d[i]
            i += 1
            has_modrm, immk = True, 'b'
        else:
            ins.map = 2
            ins.op = b2
            if b2 in OP2_NOMODRM:
                has_modrm, immk = False, 0
            elif 0x80 <= b2 <= 0x8F:
                has_modrm, immk = False, 'rel32'
            else:
                has_modrm, immk = True, ('b' if b2 in OP2_IMM8 else 0)
    elif b in (0xC4, 0xC5):
        # VEX
        if b == 0xC5:
            i += 1
            mm = 1
        else:
            mm = d[i] & 0x1F
            i += 2
        ins.map = 10 + mm
        ins.op = d[i]
        i += 1
        has_modrm, immk = True, ('b' if mm == 3 else 0)
    else:
        ins.map = 1
        ins.op = b
        t = OP1.get(b)
        if t is None:
            return None
        has_modrm, immk = t
    ins.modrm = None
    ins.riprel = False
    ins.disp = 0
    ins.base = None
    ins.index = None
    ins.mod = ins.reg = ins.rm = None
    if has_modrm:
        m = d[i]
        i += 1
        mod, reg, rm = m >> 6, (m >> 3) & 7, m & 7
        ins.modrm = m
        ins.mod = mod
        ins.reg = reg | (8 if rex & 4 else 0)
        ins.rm = rm | (8 if rex & 1 else 0)
        if mod != 3:
            if rm == 4:
                sib = d[i]
                i += 1
                base = sib & 7
                idx = ((sib >> 3) & 7) | (8 if rex & 2 else 0)
                ins.index = None if idx == 4 else idx
                if mod == 0 and base == 5:
                    ins.base = None
                    ins.disp = struct.unpack_from('<i', d, i)[0]
                    i += 4
                else:
                    ins.base = base | (8 if rex & 1 else 0)
            elif mod == 0 and rm == 5:
                ins.riprel = True
                ins.disp = struct.unpack_from('<i', d, i)[0]
                i += 4
            else:
                ins.base = rm | (8 if rex & 1 else 0)
            if mod == 1:
                ins.disp = struct.unpack_from('<b', d, i)[0]
                i += 1
            elif mod == 2:
                ins.disp = struct.unpack_from('<i', d, i)[0]
                i += 4
    ins.imm = None
    if immk == 'F6':
        immk = 'b' if (ins.reg & 7) in (0, 1) else 0
    elif immk == 'F7':
        immk = 'z' if (ins.reg & 7) in (0, 1) else 0
    if immk == 'b':
        ins.imm = struct.unpack_from('<b', d, i)[0]
        i += 1
    elif immk == 'w':
        ins.imm = struct.unpack_from('<H', d, i)[0]
        i += 2
    elif immk == 'z':
        if ins.opsize16:
            ins.imm = struct.unpack_from('<h', d, i)[0]
            i += 2
        else:
            ins.imm = struct.unpack_from('<i', d, i)[0]
            i += 4
    elif immk == 'v':
        if rex & 8:
            ins.imm = struct.unpack_from('<Q', d, i)[0]
            i += 8
        elif ins.opsize16:
            ins.imm = struct.unpack_from('<H', d, i)[0]
            i += 2
        else:
            ins.imm = struct.unpack_from('<I', d, i)[0]
            i += 4
    elif immk == 'rel8':
        ins.imm = struct.unpack_from('<b', d, i)[0]
        i += 1
    elif immk == 'rel32':
        ins.imm = struct.unpack_from('<i', d, i)[0]
        i += 4
    elif immk == 'moffs':
        i += 4 if 0x67 in pfx else 8
    elif immk == 'iwb':
        i += 3
    ins.len = i - off
    return ins


VOLATILE = (0, 1, 2, 8, 9, 10, 11)  # rax rcx rdx r8 r9 r10 r11
RSP, RBP = 4, 5


def trace_function(pe, start, end, want_call):
    """Linear-sweep one function. For each call whose target satisfies want_call(target),
    yield (call_rva, target, regs, stack, xmm, events) with symbolic arg values.
    Values: ('addr', rva) | ('mem', rva) | ('imm', int) | ('local', disp) | ('smem', rva) (movsxd)"""
    d = pe.d
    off0 = pe.r2o(start)
    regs = {}
    stack = {}
    xmm = {}
    locals_w = {}  # local disp -> (call_rva, target, regs snapshot) of last call that took &local as rcx
    a = start
    bad = 0

    def indirect(ins):
        """[reg+disp] where reg was loaded from a global pointer slot -> rva it points at"""
        if ins.riprel or ins.base is None or ins.index is not None:
            return None
        v = regs.get(ins.base)
        if not v or v[0] != 'mem':
            return None
        p = pe.q(v[1])
        if p is None or not pe.base <= p < pe.base + 0x10000000:
            return None
        return p - pe.base + ins.disp

    while a < end:
        o = off0 + (a - start)
        ins = decode(d, o, a)
        if ins is None:
            return bad + 1
        nxt = a + ins.len
        op, mp = ins.op, ins.map
        w = bool(ins.rex & 8)
        if mp == 1 and op == 0xE8:
            tgt = nxt + ins.imm
            if want_call(tgt):
                yield (a, tgt, dict(regs), dict(stack), dict(xmm), locals_w)
            # record calls that build a local (rcx = &local)
            v = regs.get(1)
            if v and v[0] == 'local':
                locals_w[v[1]] = (a, tgt, dict(regs), dict(xmm))
            for r in VOLATILE:
                regs.pop(r, None)
            xmm.clear()
            stack.clear()
        elif mp == 1 and op == 0x8D and ins.mod != 3:  # lea
            if ins.riprel:
                regs[ins.reg] = ('addr', nxt + ins.disp)
            elif ins.base in (RBP, RSP) and ins.index is None:
                regs[ins.reg] = ('local', ins.disp if ins.base == RBP else ('rsp', ins.disp))
            else:
                regs.pop(ins.reg, None)
        elif mp == 1 and op == 0x8B:  # mov r, r/m
            if ins.mod == 3:
                if ins.rm in regs:
                    regs[ins.reg] = regs[ins.rm]
                else:
                    regs.pop(ins.reg, None)
            elif ins.riprel:
                regs[ins.reg] = ('mem' if w else 'mem32', nxt + ins.disp)
            elif indirect(ins) is not None:
                regs[ins.reg] = ('mem' if w else 'mem32', indirect(ins))
            else:
                regs.pop(ins.reg, None)
        elif mp == 1 and op == 0x83 and ins.mod == 3 and (ins.reg & 7) == 1:  # or r, imm8
            v = regs.get(ins.rm)
            if v and v[0] == 'imm':
                regs[ins.rm] = ('imm', v[1] | ins.imm)
            elif ins.imm == -1:
                regs[ins.rm] = ('imm', -1)
            else:
                regs.pop(ins.rm, None)
        elif mp == 2 and op == 0x6E and ins.opsize16 and w and ins.mod == 3:  # movq xmm, r64
            v = regs.get(ins.rm)
            if v and v[0] == 'imm':
                xmm[ins.reg] = ('fimm', v[1])
            else:
                xmm.pop(ins.reg, None)
        elif mp == 1 and op == 0x63 and ins.riprel:  # movsxd r, [rip]
            regs[ins.reg] = ('smem', nxt + ins.disp)
        elif mp == 1 and op == 0x89:  # mov r/m, r
            if ins.mod == 3:
                if ins.reg in regs:
                    regs[ins.rm] = regs[ins.reg]
                else:
                    regs.pop(ins.rm, None)
            elif ins.base == RSP and ins.index is None:
                stack[ins.disp] = regs.get(ins.reg)
        elif mp == 1 and op in (0x31, 0x33) and ins.mod == 3 and ins.reg == ins.rm:
            regs[ins.reg] = ('imm', 0)
        elif mp == 1 and 0xB8 <= op <= 0xBF:
            regs[(op - 0xB8) | (8 if ins.rex & 1 else 0)] = ('imm', ins.imm)
        elif mp == 1 and op == 0xC7:
            if ins.mod == 3:
                regs[ins.rm] = ('imm', ins.imm)
            elif ins.base == RSP and ins.index is None:
                stack[ins.disp] = ('imm', ins.imm)
        elif mp == 1 and op == 0xC6 and ins.mod != 3 and ins.base == RSP and ins.index is None:
            stack[ins.disp] = ('imm', ins.imm & 0xFF)
        elif mp == 2 and op == 0x10 and ins.mod != 3 and ins.pfx and ins.pfx[-1] in (0xF2, 0xF3):  # movsd/movss xmm,m
            m = nxt + ins.disp if ins.riprel else indirect(ins)
            if m is not None:
                xmm[ins.reg] = ('fmem', m, 8 if ins.pfx[-1] == 0xF2 else 4)
            else:
                xmm.pop(ins.reg, None)
        elif mp == 2 and op == 0x5A and ins.pfx and ins.pfx[-1] == 0xF3:  # cvtss2sd xmm, xmm/m32
            if ins.riprel:
                xmm[ins.reg] = ('fmem', nxt + ins.disp, 4)
            elif ins.mod != 3 and indirect(ins) is not None:
                xmm[ins.reg] = ('fmem', indirect(ins), 4)
            elif ins.mod == 3 and ins.rm in xmm:
                xmm[ins.reg] = xmm[ins.rm]
            else:
                xmm.pop(ins.reg, None)
        elif mp == 1 and 0xB0 <= op <= 0xB7 and not ins.rex:  # mov r8, imm8 (al..bh: only low regs tracked)
            r = op - 0xB0
            if r < 4:
                regs[r] = ('imm', ins.imm & 0xFF)
        elif mp == 1 and op in (0xC3, 0xE9, 0xEB) or (mp == 1 and 0x70 <= op <= 0x7F) or (mp == 2 and 0x80 <= op <= 0x8F):
            pass  # keep linear; branches inside registration code are rare
        else:
            # any other instruction writing a GPR via modrm reg field: conservatively forget it
            if ins.modrm is not None and mp == 1 and op in (0x01, 0x03, 0x09, 0x0B, 0x21, 0x23, 0x29, 0x2B, 0x31, 0x33, 0x0F):
                if op & 2:
                    regs.pop(ins.reg, None)
                elif ins.mod == 3:
                    regs.pop(ins.rm, None)
            elif mp == 1 and 0x58 <= op <= 0x5F:
                regs.pop((op - 0x58) | (8 if ins.rex & 1 else 0), None)
            elif ins.modrm is not None and mp == 1 and op in (0x81, 0x83, 0xC1, 0xD1, 0xF7, 0xFF) and ins.mod == 3:
                if not (op == 0xFF and (ins.reg & 7) in (2, 4)):
                    regs.pop(ins.rm, None)
            elif mp == 1 and op == 0xFF and ins.mod is not None and (ins.reg & 7) == 2:  # indirect call
                for r in VOLATILE:
                    regs.pop(r, None)
                xmm.clear()
                stack.clear()
            elif mp == 2 and op in (0xB6, 0xB7, 0xBE, 0xBF, 0xAF, 0x40, 0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47,
                                    0x48, 0x49, 0x4A, 0x4B, 0x4C, 0x4D, 0x4E, 0x4F):
                regs.pop(ins.reg, None)
            elif mp == 2 and op in (0x10, 0x28, 0x57, 0x5A, 0x2A):
                xmm.pop(ins.reg, None)
        a = nxt
    return 0
