#!/usr/bin/env python3
"""
Physics-level validation of runs_summary_*.json: sum of generator weights.

check.py validates STRUCTURE (files exist, are not zombies, pair up). It does
not check that the numbers inside runs_summary are right, and the ways they go
wrong are all silent:

  * A job's Runs tree is cloned per input file. If a file is processed twice --
    or an input list overlaps between jobs -- genEventSumw is inflated and every
    normalisation downstream is wrong, with nothing in check.py to show it.
  * Conversely a dropped job loses weight, under-counting the denominator.

The strong invariant used here needs no external reference:

    every channel reads the SAME input files for a given dataset, so the sum of
    genEventSumw over a dataset's jobs MUST be identical in every channel.

Any spread across channels means jobs are seeing different inputs than intended.
Second check: genEventCount summed over jobs should equal the cutflow's
AllEvents for that dataset-channel -- they are produced by different code paths
(Runs tree vs the cutflow counter) so agreement is a real cross-check.

Usage:
    python3 check_weights.py VBSVVH_skim_v42 [--tol 1e-9] [--max-report 20]
"""
import argparse
import collections
import glob
import json
import os
import sys

BASE = "/cmsuf/data/store/user/phchang/skim"


def read_summaries(dsdir):
    """Sum genEventSumw / genEventCount over a dataset dir's runs_summary files."""
    sumw = count = 0.0
    n = 0
    for p in sorted(glob.glob(os.path.join(dsdir, "runs_summary_*.json"))):
        try:
            with open(p) as f:
                d = json.load(f)
        except Exception:
            return None, None, -1          # unreadable
        if "genEventSumw" not in d:
            return None, None, -2          # data, no gen weights
        sumw += float(d.get("genEventSumw", 0.0))
        count += float(d.get("genEventCount", 0.0))
        n += 1
    return sumw, count, n


def cutflow_allevents(dsdir):
    tot = 0.0
    for p in glob.glob(os.path.join(dsdir, "cutflow_*.cflow")):
        try:
            with open(p) as f:
                for line in f:
                    if line.startswith("AllEvents,"):
                        tot += float(line.split(",")[1])
                        break
        except Exception:
            return None
    return tot


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("skim")
    ap.add_argument("--tol", type=float, default=1e-9,
                    help="relative tolerance for cross-channel agreement")
    ap.add_argument("--max-report", type=int, default=20)
    args = ap.parse_args()

    root = os.path.join(BASE, args.skim)
    if not os.path.isdir(root):
        sys.exit(f"no such skim: {root}")

    # dataset -> {channel: (sumw, count, njobs)}
    per_ds = collections.defaultdict(dict)
    cutflow_mismatch = []
    n_data = n_unreadable = 0

    for tag in sorted(os.listdir(root)):
        tagdir = os.path.join(root, tag)
        if not os.path.isdir(tagdir):
            continue
        # strip the trailing _<channel> to group the same dataset across channels
        base_tag, _, channel = tag.rpartition("_")
        for ds in sorted(os.listdir(tagdir)):
            dsdir = os.path.join(tagdir, ds)
            if not os.path.isdir(dsdir):
                continue
            sumw, count, n = read_summaries(dsdir)
            if n == -1:
                n_unreadable += 1
                continue
            if n == -2:
                n_data += 1
                continue
            if n == 0:
                continue
            per_ds[(base_tag, ds)][channel] = (sumw, count, n)

            cf = cutflow_allevents(dsdir)
            if cf is not None and count > 0 and abs(cf - count) / count > 1e-6:
                cutflow_mismatch.append((tag, ds, count, cf))

    # --- cross-channel consistency ---
    bad = []
    for (base_tag, ds), chans in per_ds.items():
        vals = [v[0] for v in chans.values()]
        if len(vals) < 2:
            continue
        lo, hi = min(vals), max(vals)
        if hi > 0 and (hi - lo) / hi > args.tol:
            bad.append((base_tag, ds, chans, (hi - lo) / hi))

    print(f"skim                        : {args.skim}")
    print(f"MC dataset groups checked   : {len(per_ds)}")
    print(f"data dataset-dirs (skipped) : {n_data}")
    print(f"unreadable runs_summary     : {n_unreadable}")
    print()
    print(f"CROSS-CHANNEL genEventSumw disagreements : {len(bad)}")
    for base_tag, ds, chans, rel in sorted(bad, key=lambda x: -x[3])[:args.max_report]:
        print(f"  rel spread {rel:.3e}  {base_tag} / {ds[:48]}")
        for c, (w, n, j) in sorted(chans.items()):
            print(f"      {c:9s} sumw={w:.10g}  jobs={j}")
    print()
    print(f"genEventCount vs cutflow AllEvents mismatches : {len(cutflow_mismatch)}")
    for tag, ds, cnt, cf in cutflow_mismatch[:args.max_report]:
        print(f"  {tag} / {ds[:44]}  runs={cnt:.0f} cutflow={cf:.0f}")

    return 1 if (bad or cutflow_mismatch or n_unreadable) else 0


if __name__ == "__main__":
    sys.exit(main())
