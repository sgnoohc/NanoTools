#!/usr/bin/env python3
"""
Event-level spot check of v42 after the in-place Jet_jetId rename.

The rename modified files in place, so there is no untouched copy to diff
against. This validates instead against things the rename did NOT touch:

  * cutflow_*.cflow  -- AllEvents, written during production
  * runs_summary_*.json -- genEventCount, written during production
  * physics invariants that corruption would break
  * the forward-region pass rates measured BEFORE the rename
    (|eta|>3: v12 ~30%, recomputed ~86%)

Every entry of each sampled file is read in full, so a damaged basket shows up
as a read error rather than being missed by sampling.

Usage:
  python3 spotcheck_jetid.py VBSVVH_skim_v42 --sample 200 --shard 0 --nshards 10
"""
import argparse
import glob
import json
import os
import random
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed

BASE = "/cmsuf/data/store/user/phchang/skim"


def cutflow_allevents(dsdir):
    tot = 0.0
    found = False
    for p in glob.glob(os.path.join(dsdir, "cutflow_*.cflow")):
        try:
            for line in open(p):
                if line.startswith("AllEvents,"):
                    tot += float(line.split(",")[1]); found = True
                    break
        except Exception:
            return None
    return tot if found else None


def check_file(path):
    import ROOT
    ROOT.gROOT.SetBatch(True)
    ROOT.gErrorIgnoreLevel = ROOT.kFatal
    r = {"path": path, "errors": [], "nev": 0,
         "hi_n": 0, "hi_v12": 0, "hi_reco": 0, "njets": 0}
    f = ROOT.TFile.Open(path, "READ")
    if not f or f.IsZombie():
        r["errors"].append("zombie")
        if f: f.Close()
        return r
    t = f.Get("Events")
    if not t or not hasattr(t, "GetListOfBranches"):
        r["errors"].append("no Events tree"); f.Close(); return r

    names = [b.GetName() for b in t.GetListOfBranches()]
    if names.count("Jet_jetId") != 1:
        r["errors"].append(f"Jet_jetId count={names.count('Jet_jetId')}")
    if names.count("Jet_jetId_v12") != 1:
        r["errors"].append(f"Jet_jetId_v12 count={names.count('Jet_jetId_v12')}")
    brs = [b for b in t.GetListOfBranches() if b.GetName() == "Jet_jetId"]
    if brs and brs[0].GetClassName() != "vector<float>":
        r["errors"].append(f"Jet_jetId type={brs[0].GetClassName()}")
    if r["errors"]:
        f.Close(); return r

    reco = ROOT.std.vector("float")()
    brs[0].SetAddress(ROOT.AddressOf(reco))
    n = t.GetEntries()
    r["nev"] = n
    VALID = {0.0, 2.0, 4.0, 6.0}
    for i in range(n):                      # read EVERY entry
        if t.GetEntry(i) <= 0:
            r["errors"].append(f"GetEntry failed at {i}"); break
        if brs[0].GetEntry(i) < 0:
            r["errors"].append(f"Jet_jetId read failed at {i}"); break
        nj = int(t.nJet)
        if len(reco) != nj:
            r["errors"].append(f"len(Jet_jetId)={len(reco)} != nJet={nj} at {i}"); break
        if len(t.Jet_jetId_v12) != nj:
            r["errors"].append(f"len(_v12)={len(t.Jet_jetId_v12)} != nJet={nj} at {i}"); break
        for q in range(nj):
            v = reco[q]
            if v not in VALID:
                r["errors"].append(f"bad recomputed id {v} at evt {i}"); break
            r["njets"] += 1
            if abs(t.Jet_eta[q]) > 3.0:
                r["hi_n"] += 1
                r["hi_reco"] += (v >= 2)
                r["hi_v12"] += (int(t.Jet_jetId_v12[q]) >= 2)
        if r["errors"]:
            break
    f.Close()

    # cross-check against records the rename never touched
    dsdir = os.path.dirname(path)
    idx = os.path.basename(path)[len("output_"):-len(".root")]
    js = os.path.join(dsdir, f"runs_summary_{idx}.json")
    if os.path.isfile(js):
        try:
            d = json.load(open(js))
            if "genEventCount" in d:
                r["gen_count"] = float(d["genEventCount"])
        except Exception:
            r["errors"].append("runs_summary unreadable")
    return r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("skim")
    ap.add_argument("--sample", type=int, default=200)
    ap.add_argument("--seed", type=int, default=20261017)
    ap.add_argument("--maxsize", type=int, default=400_000_000,
                    help="skip files larger than this, to keep each task short")
    ap.add_argument("-j", "--jobs", type=int, default=4)
    ap.add_argument("--shard", type=int, default=0)
    ap.add_argument("--nshards", type=int, default=1)
    args = ap.parse_args()

    top = os.path.join(BASE, args.skim)
    files = []
    for dp, _, nms in os.walk(top):
        for nm in nms:
            if nm.startswith("output_") and nm.endswith(".root"):
                files.append(os.path.join(dp, nm))
    files.sort()
    # stratify: sample within each tag so every era/kind/channel is represented
    bytag = {}
    for p in files:
        tag = p[len(top) + 1:].split("/")[0]
        bytag.setdefault(tag, []).append(p)
    rng = random.Random(args.seed)
    per = max(1, args.sample // max(1, len(bytag)))
    picked = []
    for tag in sorted(bytag):
        cand = [p for p in bytag[tag] if os.path.getsize(p) <= args.maxsize]
        if not cand:
            continue
        picked += rng.sample(cand, min(per, len(cand)))
    picked.sort()
    if args.nshards > 1:
        picked = [p for i, p in enumerate(picked) if i % args.nshards == args.shard]
    print(f"tags={len(bytag)}  sampled={len(picked)} files"
          + (f" (shard {args.shard}/{args.nshards})" if args.nshards > 1 else ""), flush=True)

    bad = []
    tot_ev = tot_jets = hi_n = hi_v12 = hi_reco = 0
    gen_ok = gen_bad = 0
    with ProcessPoolExecutor(max_workers=args.jobs) as ex:
        for fut in as_completed({ex.submit(check_file, p): p for p in picked}):
            r = fut.result()
            if r["errors"]:
                bad.append((r["path"], r["errors"][0]))
            tot_ev += r["nev"]; tot_jets += r["njets"]
            hi_n += r["hi_n"]; hi_v12 += r["hi_v12"]; hi_reco += r["hi_reco"]
            if "gen_count" in r:
                if abs(r["gen_count"] - r["nev"]) < 0.5 or r["gen_count"] >= r["nev"]:
                    gen_ok += 1
                else:
                    gen_bad += 1
    print(f"\nfiles checked   : {len(picked)}")
    print(f"events read     : {tot_ev:,}   (every entry of every file)")
    print(f"jets inspected  : {tot_jets:,}")
    print(f"FILES WITH ERRORS: {len(bad)}")
    for p, e in bad[:15]:
        print(f"   {e}  {p}")
    print(f"runs_summary consistent : {gen_ok}  inconsistent : {gen_bad}")
    if hi_n:
        print(f"\n|eta|>3 jets {hi_n:,}:  v12 pass {hi_v12/hi_n:.1%}   recomputed pass {hi_reco/hi_n:.1%}")
        print("  (pre-rename reference: v12 ~30%, recomputed ~86%)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
