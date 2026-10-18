#!/usr/bin/env python3
"""
Rename the stale NanoAODv12 Jet_jetId branch in already-produced skims.

The v12-based PFNano inputs (2022/2023) carry their own Jet_jetId (UChar_t),
and the skimmer writes a recomputed JSON-recipe Jet_jetId (vector<float>). Both
reached the output under the SAME name, and RDataFrame resolves by name and
always returns the first one -- the stale v12 ID. Reading it as a float does not
switch branches, it silently returns garbage.

This renames the UChar_t branch (and its leaf) to Jet_jetId_v12, so:

    Jet_jetId      -> RVec<float>    the recomputed JSON-recipe ID
    Jet_jetId_v12  -> RVec<UChar_t>  the original, kept for comparison

It is a METADATA-ONLY edit: branch and leaf names in the TTree header. No
baskets are rewritten and no event data is re-encoded, so it runs in well under
a second per file regardless of size.

The skimmer itself was fixed in 5a1d279, so anything produced from now on comes
out correct and does not need this. This is only for files already on disk.

Safety:
  * dry-run unless --execute is passed (same convention as regen_runs_summary.py)
  * idempotent -- a file that already has Jet_jetId_v12 is skipped
  * a file with only ONE Jet_jetId is skipped (nothing to disambiguate)
  * every modified file is reopened and verified before being counted as done
  * uses processes, not threads: PyROOT deadlocks under ThreadPoolExecutor

Usage:
    python3 rename_jetid.py VBSVVH_skim_v42                 # dry run
    python3 rename_jetid.py VBSVVH_skim_v42 --execute       # apply
    python3 rename_jetid.py VBSVVH_skim_v42 --execute -j 16
"""
import argparse
import os
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed

BASE = "/cmsuf/data/store/user/phchang/skim"
OLD = "Jet_jetId"
NEW = "Jet_jetId_v12"


def classify(path):
    """Inspect a file. Returns (state, nentries) without modifying anything."""
    import ROOT
    ROOT.gROOT.SetBatch(True)
    ROOT.gErrorIgnoreLevel = ROOT.kFatal
    f = ROOT.TFile.Open(path, "READ")
    if not f or f.IsZombie():
        if f:
            f.Close()
        return "unreadable", 0
    t = f.Get("Events")
    if not t or not hasattr(t, "GetListOfBranches"):
        f.Close()
        return "no_tree", 0
    uchar = vec = already = 0
    for b in t.GetListOfBranches():
        n = b.GetName()
        if n == NEW:
            already += 1
        elif n == OLD:
            if b.GetClassName() == "vector<float>":
                vec += 1
            else:
                uchar += 1
    n = t.GetEntries()
    f.Close()
    if already:
        return "already_done", n
    if uchar == 0:
        return "nothing_to_do", n       # v15-style: only the recomputed branch
    if vec == 0:
        return "no_recomputed", n       # v12 branch only -- do NOT touch
    return "needs_rename", n


def rename_one(path):
    """Rename in place, then verify. Returns (path, state, message)."""
    state, n_before = classify(path)
    if state != "needs_rename":
        return path, state, ""

    import ROOT
    ROOT.gROOT.SetBatch(True)
    ROOT.gErrorIgnoreLevel = ROOT.kFatal
    try:
        f = ROOT.TFile.Open(path, "UPDATE")
        if not f or f.IsZombie():
            return path, "failed", "could not open UPDATE"
        t = f.Get("Events")
        done = False
        for b in t.GetListOfBranches():
            if b.GetName() == OLD and b.GetClassName() != "vector<float>":
                b.SetName(NEW)
                b.SetTitle(
                    "Original NanoAODv12 Jet ID flag (bit2=tight, bit3=tightLepVeto); "
                    "renamed so Jet_jetId refers to the recomputed JSON-recipe ID"
                )
                leaves = b.GetListOfLeaves()
                if leaves and leaves.GetEntries() == 1:
                    leaves.At(0).SetName(NEW)
                done = True
                break
        if not done:
            f.Close()
            return path, "failed", "UChar_t branch vanished between passes"
        t.Write("", ROOT.TObject.kOverwrite)
        f.Close()
    except Exception as exc:
        return path, "failed", f"exception during rename: {exc}"

    # verify on a fresh open
    state2, n_after = classify(path)
    if state2 != "already_done":
        return path, "failed", f"post-check state={state2}"
    if n_after != n_before:
        return path, "failed", f"entries changed {n_before} -> {n_after}"
    return path, "renamed", ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("skim", help="e.g. VBSVVH_skim_v42")
    ap.add_argument("--execute", action="store_true", help="actually modify files")
    ap.add_argument("-j", "--jobs", type=int, default=12)
    ap.add_argument("--limit", type=int, default=0, help="only process the first N files")
    ap.add_argument("--root", default=BASE)
    # Sharding keeps each SLURM array task short. HiPerGator login nodes kill
    # long-running processes, and a single 16k-file pass is both too long and
    # too heavy to belong on a login node at all -- run this as an array job.
    ap.add_argument("--shard", type=int, default=0, help="this task's index (0-based)")
    ap.add_argument("--nshards", type=int, default=1, help="total number of shards")
    args = ap.parse_args()

    top = os.path.join(args.root, args.skim)
    if not os.path.isdir(top):
        sys.exit(f"no such skim: {top}")

    print(f"scanning {top} ...", flush=True)
    files = []
    for dirpath, _, names in os.walk(top):
        for nm in names:
            if nm.startswith("output_") and nm.endswith(".root"):
                files.append(os.path.join(dirpath, nm))
    files.sort()
    if args.limit:
        files = files[: args.limit]
    total_all = len(files)
    if args.nshards > 1:
        files = [f for i, f in enumerate(files) if i % args.nshards == args.shard]
    print(f"found {total_all:,} output files"
          + (f"; shard {args.shard}/{args.nshards} takes {len(files):,}" if args.nshards > 1 else ""),
          flush=True)
    if not files:
        return 0

    worker = rename_one if args.execute else classify_only
    mode = "EXECUTE" if args.execute else "DRY RUN (pass --execute to apply)"
    print(f"mode: {mode}   workers: {args.jobs}\n", flush=True)

    counts = {}
    failures = []
    done = 0
    with ProcessPoolExecutor(max_workers=args.jobs) as ex:
        futs = {ex.submit(worker, p): p for p in files}
        for fut in as_completed(futs):
            path, state, msg = fut.result()
            counts[state] = counts.get(state, 0) + 1
            if state == "failed":
                failures.append((path, msg))
            done += 1
            if done % 500 == 0 or done == len(files):
                print(f"  {done:,}/{len(files):,}", flush=True)

    print("\n=== summary ===")
    for k in sorted(counts):
        print(f"  {k:16s} {counts[k]:,}")
    if failures:
        print(f"\n  FAILURES ({len(failures)}):")
        for p, m in failures[:20]:
            print(f"    {m}  {p}")
    return 1 if failures else 0


def classify_only(path):
    state, _ = classify(path)
    return path, state, ""


if __name__ == "__main__":
    sys.exit(main())
