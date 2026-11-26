#!/usr/bin/env python3
"""Rewrite Nano.h / Nano.cc so every array-branch buffer is sized per input file.

Before: each array branch (e.g. TrigObj_pt[nTrigObj]) was a fixed C array sized by a
compile-time N*_MAX limit. Any input with a larger count overflowed it, so the limits were
bumped one by one as inputs exceeded them (nGenPart, nSV, nTrigObj, nboostedTau, nFatJet ...).

After: each array is a NanoBuf<T> (NanoBuf.h). Nano::Init() (once per input file) grows it to the largest
count that file holds, read from the counter leaf's metadata (TLeaf::GetMaximum, the value ROOT
itself uses to size its own buffers), and re-binds it. CheckBufferSizes() remains as a per-event
tripwire comparing each counter with its file's recorded maximum.

Exactly three textual uses per array are rewritten, and the counts are asserted:
  Nano.h   'T X_[NFOO_MAX];'                      -> 'NanoBuf<T> X_;'
  Nano.cc  'b_X_->SetAddress(&X_);'               -> 'b_X_->SetAddress(X_.growFor(b_X_));'
  Nano.cc  'vector<T>(X_,X_+bytes/sizeof(X_[0]))' -> 'vector<T>(X_.data(),X_.data()+bytes/sizeof(X_[0]))'
NanoBuf has no implicit pointer conversion, so any other use of an array fails to compile --
except SetAddress(&X_), which would silently bind the wrong address; that one is asserted.
Buffers are sized in bytes of the ON-DISK type (growFor), because NanoAOD has widened types between
versions (TrigObj_filterBits Int_t -> ULong64_t) and SetAddress does no conversion.

Scalars cannot grow, so Nano::CheckScalarWidths() is generated (one nanoCheckScalarWidth per scalar
binding); the skimmer calls it once per file after Arbusto has set which branches are read, and it
throws if a read scalar is wider on disk than its member.

Usage: python3 make_buffers_dynamic.py [NanoCORE dir]   (refuses to run twice)
"""
import os, re, sys

D = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
H, C = os.path.join(D, "Nano.h"), os.path.join(D, "Nano.cc")
h, c = open(H).read(), open(C).read()
if "class NanoBuf" in h:
    sys.exit("Nano.h already uses NanoBuf -- nothing to do")

HELPERS = r'''// Array-branch buffers are NanoBuf (NanoBuf.h), sized per input file in Init() from each counter's
// recorded maximum -- there are no compile-time N*_MAX limits. Migrated by make_buffers_dynamic.py.
#include "NanoBuf.h"
'''

# --- Nano.h: helpers replace the N*_MAX block ---------------------------------------------
defs = re.findall(r"^#define N\w+_MAX .*\n", h, flags=re.M)
assert len(defs) == 33, f"expected 33 N*_MAX defines, found {len(defs)}"
block = "".join(defs)
assert block in h, "N*_MAX defines are not contiguous"
h = h.replace(block, HELPERS, 1)

# --- Nano.h: array declarations -> NanoBuf ---------------------------------------------------
decl = re.compile(r"^(\s+)([A-Za-z_][\w:]*) (\w+_)\[N\w+_MAX\];(\s*//.*)?$", re.M)   # keeps a trailing comment
arrays = [m.group(3) for m in decl.finditer(h)]
assert len(arrays) == 741 and len(set(arrays)) == 741, f"expected 741 unique arrays, found {len(arrays)}"
h = decl.sub(lambda m: f"{m.group(1)}NanoBuf<{m.group(2)}> {m.group(3)};{m.group(4) or ''}", h)
assert "_MAX]" not in h, "an array declaration still uses an N*_MAX limit"

# --- Nano.h: CheckBufferSizes compares with the file's recorded maximum -----------------------
chk = re.compile(r'check\(b_(\w+)_, \1_, N\w+_MAX, "\1"\);')
counters = chk.findall(h)
assert len(counters) == 34, f"expected 34 counter checks, found {len(counters)}"
h = chk.sub(r'check(b_\1_, \1_, filemax_\1_, "\1");', h)
old_msg = '''                              << " exceeds buffer limit " << max
                              << " in file " << b->GetTree()->GetCurrentFile()->GetName()
                              << ". Increase the corresponding _MAX in Nano.h and recompile." << std::endl;'''
new_msg = '''                              << " exceeds the maximum recorded in the file's metadata (" << max
                              << "), which sizes the buffers, in file " << b->GetTree()->GetCurrentFile()->GetName()
                              << ". The file's metadata is inconsistent." << std::endl;'''
assert h.count(old_msg) == 1, "CheckBufferSizes message not found"
h = h.replace(old_msg, new_msg)
members = "".join(f"    unsigned int filemax_{n}_ = 0;\n" for n in counters)
anchor = "    Int_t year_;\npublic:\n"
assert h.count(anchor) == 1
h = h.replace(anchor, "    Int_t year_;\n    // Per-file maximum of each counter (set in Init), checked by CheckBufferSizes().\n"
              + members + "public:\n", 1)

# --- Nano.cc: bind grown buffers, record counter maxima, copy out via data() -----------------
n_bind = n_vec = 0
for a in arrays:
    old = f"b_{a}->SetAddress(&{a});"
    assert c.count(old) == 1, f"{a}: expected one SetAddress(&{a}), found {c.count(old)}"
    c = c.replace(old, f"b_{a}->SetAddress({a}.growFor(b_{a}));"); n_bind += 1
    vec = re.compile(r"vector<([\w:]+)>\(" + a + "," + a + r"\+bytes/sizeof\(" + a + r"\[0\]\)\)")
    c, k = vec.subn(r"vector<\1>(" + a + ".data()," + a + ".data()+bytes/sizeof(" + a + "[0]))", c)
    assert k == 1, f"{a}: expected one vector copy, found {k}"; n_vec += 1
    assert f"&{a})" not in c and f"&{a};" not in c, f"{a}: an address-of use remains"
end_init = "    ParseYear(tree);\n}\nvoid Nano::SetYear"
assert c.count(end_init) == 1
c = c.replace(end_init, "    // Per-file counter maxima for CheckBufferSizes() (the buffers above were grown to these).\n"
              + "".join(f'    filemax_{n}_ = nanoLeafMax(tree, "{n}");\n' for n in counters)
              + end_init, 1)

# --- scalars: a per-file width guard over every remaining (scalar) binding ------------------------
scalars = re.findall(r"if \(b_(\w+_)\) \{ b_\1->SetAddress\(&\1\); \}", c)
assert len(scalars) == len(set(scalars)) and not set(scalars) & set(arrays), "scalar list overlaps arrays"
end_init = "    ParseYear(tree);\n}\n"
assert c.count(end_init) == 1
c = c.replace(end_init, end_init + "// Throws if a branch Arbusto will READ is wider on disk than its scalar member (see NanoBuf.h).\n"
              + "// Call once per file AFTER the branch statuses are set (skimmer: after arbusto.init()).\n"
              + "void Nano::CheckScalarWidths() {\n"
              + "".join(f'    nanoCheckScalarWidth(b_{v}, sizeof({v}), "{v[:-1]}");\n' for v in scalars)
              + "}\n", 1)
decl_init = "    void Init(TTree *tree);\n"
assert h.count(decl_init) == 1
h = h.replace(decl_init, decl_init + "    void CheckScalarWidths();\n", 1)

open(H, "w").write(h); open(C, "w").write(c)
print(f"Nano.h: 33 N*_MAX defines removed, {len(arrays)} arrays -> NanoBuf, {len(counters)} checks -> per-file maxima")
print(f"Nano.cc: {n_bind} SetAddress rebound to grown buffers, {n_vec} accessors copy via data(), "
      f"{len(scalars)} scalars width-checked in CheckScalarWidths()")
