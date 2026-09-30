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
# Primary datasets that route to NO channel (submit.py UNUSED_PDS): the skim
# counts electrons and muons only, and BTagMu is a b-tag calibration PD. They
# would produce zero jobs, so staging their ~10k files is pure cost. Pass
# --stage-unused to override.
UNUSED_PDS = {"Tau", "BTagMu"}
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
    ap.add_argument("--include-data", action="store_true", help="Stage the DATA categories only (not bkg).")
    ap.add_argument("--include-signal", action="store_true", help="Stage the SIGNAL category only (not bkg).")
    ap.add_argument("--stage-unused", action="store_true",
                    help="Also stage PDs that route to no channel (Tau, BTagMu).")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    idx = json.load(open(INDEX))
    if args.era not in idx:
        sys.exit(f"era {args.era} not in index")

    pairs, skipped_no_store = [], 0
    for cat, cd in sorted(idx[args.era].items()):
        is_data = cat in DATA_CATEGORIES
        is_sig = cat in SIGNAL_CATEGORIES
        if args.include_data:
            if not is_data:
                continue
            if cat in UNUSED_PDS and not args.stage_unused:
                continue
        elif args.include_signal:
            if not is_sig:
                continue
        elif is_data or is_sig:
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

    # Name the manifest after (era, kind) so it lines up with the .staged_<era>_<kind>
    # marker that vbsvvh_v14._is_staged() reads. Marker granularity MUST match what
    # was actually staged -- an over-broad marker hands jobs /cmsuf paths that do not
    # exist, and they fail with no fallback.
    kind = "data" if args.include_data else ("sig" if args.include_signal else "bkg")
    out = args.out or os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        f"stage_manifest_{args.era}_{kind}.txt",
    )
    with open(out, "w") as f:
        for src, dest in uniq:
            f.write(f"{src}\t{dest}\n")

    print(f"era            : {args.era}")
    print(f"entries        : {len(pairs)}")
    print(f"unique dests   : {len(uniq)}" + (f"  ({len(pairs)-len(uniq)} duplicate paths collapsed)" if len(pairs) != len(uniq) else ""))
    if skipped_no_store:
        print(f"SKIPPED (no /store/ in url): {skipped_no_store}")
    print(f"kind           : {kind}")
    print(f"manifest       : {out}")
    print(f"est. volume    : {len(uniq)*1063/1e6:.1f} TB  (at measured 1063 MB/file mean)")


if __name__ == "__main__":
    main()
