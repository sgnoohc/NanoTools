// -*- C++ -*-
// NanoBuf.h -- per-file array-branch buffers for the generated Nano class (hand-written, not generated).
//
// Every NanoAOD array branch (e.g. TrigObj_pt[nTrigObj]) is bound to a NanoBuf. Nano::Init() runs once
// per input file and grows each buffer (growFor) to the most BYTES one entry can take in that file:
// the counter's recorded maximum (TLeaf::GetMaximum -- the number ROOT itself uses to size its own
// buffers) x the static length x the ON-DISK element width. Sizing by the on-disk width matters:
// TBranch::SetAddress does no type conversion, and NanoAOD has widened types between versions
// (TrigObj_filterBits Int_t -> ULong64_t, *_seediEtaOriX Char_t -> Short_t), so a buffer sized in
// Nano's declared element type would overflow. Buffers only grow, so memory follows the largest file.
//
// Scalars cannot be grown: nanoCheckScalarWidth() (via Nano::CheckScalarWidths, called once per file
// after Arbusto has set which branches are read) throws if a read scalar is wider on disk than its
// Nano member, instead of letting GetEntry overrun the member.
//
// This replaced 33 hand-tuned N*_MAX compile-time limits that overflowed one after another (nGenPart 746,
// nSV 75, nTrigObj 597, nboostedTau 16, nFatJet 44 ...). Nano::CheckBufferSizes() stays as a per-event
// tripwire against a file whose recorded maximum is wrong.
//
// Init() may move a buffer, so anything sharing its address must re-bind per file. Arbusto does:
// arbusto.init() (CopyAddresses) runs after nt.Init() in skimmer/src/Analysis.h initPerTTree.
//
// Used by utils/make_nanoclassfiles.py (generated Nano.h) and NanoCORE/make_buffers_dynamic.py (the
// one-time migration of the hand-edited Nano.h), and by the skimmer's own jet-ID buffers.
#ifndef NanoBuf_H
#define NanoBuf_H

#include <cstddef>
#include <stdexcept>
#include <string>
#include "TBranch.h"
#include "TLeaf.h"
#include "TTree.h"

template <typename T>
class NanoBuf {
  public:
    NanoBuf() = default;
    NanoBuf(const NanoBuf &) = delete;
    NanoBuf &operator=(const NanoBuf &) = delete;
    ~NanoBuf() { delete[] buf_; }
    // Make room for n elements (at least 1) and return the address to bind. Grow-only; the contents
    // are not preserved (the next GetEntry overwrites them).
    T *grow(size_t n) {
        if (n < 1) n = 1;
        if (n > cap_) {
            T *p = new T[n]();
            delete[] buf_;
            buf_ = p;
            cap_ = n;
        }
        return buf_;
    }
    // Grow to hold one entry of branch b in the current file (see nanoBranchBytes) and return the
    // address to bind. Sized in bytes of the ON-DISK type, rounded up to whole T elements.
    T *growFor(TBranch *b);
    // No implicit conversion to T* on purpose: any use of a buffer as a raw array must be explicit.
    T *data() { return buf_; }
    const T *data() const { return buf_; }
    T &operator[](size_t i) { return buf_[i]; }
    const T &operator[](size_t i) const { return buf_[i]; }
    size_t capacity() const { return cap_; }
  private:
    T *buf_ = nullptr;
    size_t cap_ = 0;
};

// Largest value a leaf takes in the current file, from the file's metadata (0 if absent).
inline long nanoLeafMax(TTree *tree, const char *name) {
    TLeaf *l = tree ? tree->GetLeaf(name) : nullptr;
    return l ? static_cast<long>(l->GetMaximum()) : 0;
}

// The leaf that holds a branch's data (NanoAOD branches have one leaf, named like the branch).
inline TLeaf *nanoLeaf(TBranch *b) {
    if (!b) return nullptr;
    TLeaf *l = b->GetLeaf(b->GetName());
    if (!l && b->GetListOfLeaves()->GetEntries() > 0) l = static_cast<TLeaf *>(b->GetListOfLeaves()->At(0));
    return l;
}

// Most bytes one entry of an array branch can occupy in the current file:
// (counter's recorded maximum) x (static length per count) x (on-disk element width).
inline size_t nanoBranchBytes(TBranch *b) {
    TLeaf *l = nanoLeaf(b);
    if (!l) return 0;
    long per = l->GetLenStatic() > 0 ? l->GetLenStatic() : 1;
    long n = per;
    if (TLeaf *cnt = l->GetLeafCount()) n = per * (cnt->GetMaximum() > 0 ? static_cast<long>(cnt->GetMaximum()) : 0);
    long width = l->GetLenType() > 0 ? l->GetLenType() : 8;
    return n > 0 ? static_cast<size_t>(n * width) : 0;
}

// Throw if a branch that will be READ (not kDoNotProcess) is wider on disk than the member bound to it:
// TBranch::GetEntry would write past the member. Inactive branches are never read, so they are skipped.
inline void nanoCheckScalarWidth(TBranch *b, size_t member_bytes, const char *name) {
    if (!b || b->TestBit(kDoNotProcess)) return;
    TLeaf *l = nanoLeaf(b);
    if (!l || l->GetLenType() <= 0 || static_cast<size_t>(l->GetLenType()) <= member_bytes) return;
    throw std::runtime_error(std::string("Nano: branch ") + name + " is " + l->GetTypeName() + " (" +
                             std::to_string(l->GetLenType()) + " bytes) on disk but Nano.h stores it in " +
                             std::to_string(member_bytes) + " bytes; regenerate Nano.h (utils/make_nanoclassfiles.py) "
                             "or widen that member. File: " + b->GetTree()->GetCurrentFile()->GetName());
}

template <typename T>
T *NanoBuf<T>::growFor(TBranch *b) {
    return grow((nanoBranchBytes(b) + sizeof(T) - 1) / sizeof(T));
}

#endif
