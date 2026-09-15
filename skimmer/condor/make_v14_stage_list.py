#!/usr/bin/env python3
"""
Build the src->dest manifest for staging v14 PFNano inputs onto /cmsuf.

Why stage at all: the packed executable copies every input to node-local /tmp
before running skim, and it does that once per (dataset, channel) task. For the
v14 background MC that is ~517 TB of repeated transfer, and because
SLURM_TMPDIR is /tmp on this cluster (not a per-job dir) and nothing deletes
the inputs afterwards, the copies accumulate on shared node scratch -- observed
at 1.5-1.6 TB per node, one node at 100% full.

Staging to /cmsuf sidesteps all of it: slurm_packed_executable.sh already has a
branch that skips xrdcp entirely when INPUTFILENAMES starts with /cmsuf/, so
staged jobs read the shared copy and write nothing to node /tmp.

Destination mirrors the path after "/store/", so the mapping stays reversible
and obvious:
  root://cmseos.fnal.gov//store/user/lpcpfnano/PFNano_Run3/.../MC_postEE2022_1.root
  -> /cmsuf/data/store/user/phchang/v14stage/user/lpcpfnano/PFNano_Run3/.../MC_postEE2022_1.root

Usage:
  python3 make_v14_stage_list.py 2022                 # one era, bkg only
  python3 make_v14_stage_list.py 2022 --include-data  # add the data groups
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

STAGE_ROOT = "/cmsuf/data/store/user/phchang/v14stage"
INDEX = "/blue/avery/p.chang/work/skim/NanoTools_/nanoindex_v14_HVV_private.json"
DATA_CATEGORIES = {"JetMET", "EGamma", "Muon", "Tau", "BTagMu"}
SIGNAL_CATEGORIES = {"HVV_Signal"}


def staged_path(url):
    """root://host//store/<rest>  ->  <STAGE_ROOT>/<rest>. Returns None if no /store/."""
    marker = "/store/"
    i = url.find(marker)
    if i < 0:
        return None
    return os.path.join(STAGE_ROOT, url[i + len(marker):])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("era", choices=["2022", "2022EE", "2023", "2023BPix"])
    ap.add_argument("--include-data", action="store_true")
    ap.add_argument("--include-signal", action="store_true")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    idx = json.load(open(INDEX))
    if args.era not in idx:
        sys.exit(f"era {args.era} not in index")

    pairs, skipped_no_store = [], 0
    for cat, cd in sorted(idx[args.era].items()):
        if cat in DATA_CATEGORIES and not args.include_data:
            continue
        if cat in SIGNAL_CATEGORIES and not args.include_signal:
            continue
        for sname, files in sorted(cd.items()):
            for url in files:
                dest = staged_path(url)
                if dest is None:
                    skipped_no_store += 1
                    continue
                pairs.append((url, dest))

    # The index can list the same physical file under more than one sample;
    # staging it twice would be wasted transfer and a write race.
    seen, uniq = set(), []
    for src, dest in pairs:
        if dest in seen:
            continue
        seen.add(dest)
        uniq.append((src, dest))

    out = args.out or os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        f"stage_manifest_{args.era}.txt",
    )
    with open(out, "w") as f:
        for src, dest in uniq:
            f.write(f"{src}\t{dest}\n")

    print(f"era            : {args.era}")
    print(f"entries        : {len(pairs)}")
    print(f"unique dests   : {len(uniq)}" + (f"  ({len(pairs)-len(uniq)} duplicate paths collapsed)" if len(pairs) != len(uniq) else ""))
    if skipped_no_store:
        print(f"SKIPPED (no /store/ in url): {skipped_no_store}")
    print(f"manifest       : {out}")
    print(f"est. volume    : {len(uniq)*1063/1e6:.1f} TB  (at measured 1063 MB/file mean)")


if __name__ == "__main__":
    main()
