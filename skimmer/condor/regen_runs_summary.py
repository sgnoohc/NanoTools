#!/usr/bin/env python3
"""
Regenerate runs_summary JSON files for jobs that have 0-byte JSONs
but valid ROOT output files. Operates in-place on the output directory.

Usage:
    python3 regen_runs_summary.py --skim-name VBSVVH_skim_v27              # dry-run (default)
    python3 regen_runs_summary.py --skim-name VBSVVH_skim_v27 --execute     # actually write files
    python3 regen_runs_summary.py --skim-name VBSVVH_skim_v27 --execute --jobs 5  # limit parallelism
"""

import argparse
import json
import os
import sys
import tempfile
from concurrent.futures import ProcessPoolExecutor, as_completed

SKIM_BASE = "/cmsuf/data/store/user/phchang/skim"


def find_zero_byte_runs_summaries(output_base):
    """Walk the output tree and return list of (json_path, root_path) for 0-byte JSONs."""
    pairs = []
    for campaign in sorted(os.listdir(output_base)):
        cp = os.path.join(output_base, campaign)
        if not os.path.isdir(cp):
            continue
        for dataset in sorted(os.listdir(cp)):
            dp = os.path.join(cp, dataset)
            if not os.path.isdir(dp):
                continue
            for f in sorted(os.listdir(dp)):
                if f.startswith("runs_summary_") and f.endswith(".json"):
                    fp = os.path.join(dp, f)
                    if os.path.getsize(fp) == 0:
                        idx = f.replace("runs_summary_", "").replace(".json", "")
                        root_path = os.path.join(dp, f"output_{idx}.root")
                        if os.path.exists(root_path) and os.path.getsize(root_path) > 0:
                            pairs.append((fp, root_path))
                        else:
                            print(f"  SKIP (no valid ROOT): {fp}")
    return pairs


def generate_runs_summary(root_path):
    """Read a ROOT file and return the runs_summary dict (same logic as the job scripts)."""
    import ROOT as r

    out = {}
    f = r.TFile.Open(root_path)
    if not f or f.IsZombie():
        return None

    # Event count
    events_tree = f.Get("Events")
    if events_tree:
        out["eventCount"] = int(events_tree.GetEntries())

    # MC: summarize GenWeights from Runs TTree
    t = f.Get("Runs")
    if t and t.GetBranch("genEventCount"):
        scalars = {"genEventCount": 0, "genEventSumw": 0.0, "genEventSumw2": 0.0}
        arrays = {}
        for i in range(t.GetEntries()):
            t.GetEntry(i)
            for k in scalars:
                scalars[k] += getattr(t, k)
            if i == 0:
                for bname in ["LHEScaleSumw", "LHEPdfSumw", "PSSumw"]:
                    br = t.GetBranch(bname)
                    if br:
                        n = getattr(t, "n" + bname)
                        arrays[bname] = [0.0] * n
            for bname, sums in arrays.items():
                vals = getattr(t, bname)
                for j in range(len(sums)):
                    sums[j] += vals[j]
        out.update(scalars)
        out.update(arrays)

    f.Close()

    if not out:
        return None

    # Ensure JSON-serializable (convert ROOT types)
    for k, v in out.items():
        if isinstance(v, list):
            out[k] = [float(x) for x in v]
        elif isinstance(v, float) or hasattr(v, "__float__"):
            out[k] = float(v)
        elif isinstance(v, int) or hasattr(v, "__int__"):
            out[k] = int(v)

    return out


def process_one(json_path, root_path, dry_run):
    """Process a single (json_path, root_path) pair. Returns (json_path, status_msg)."""
    try:
        out = generate_runs_summary(root_path)
    except Exception as e:
        return (json_path, f"ERROR reading ROOT: {e}")

    if out is None:
        return (json_path, "ERROR: no data extracted from ROOT file")

    if dry_run:
        keys = ", ".join(sorted(out.keys()))
        return (json_path, f"WOULD WRITE ({len(out)} keys: {keys})")

    # Atomic write: tmp file then rename
    dirname = os.path.dirname(json_path)
    try:
        fd, tmp_path = tempfile.mkstemp(suffix=".json", dir=dirname)
        with os.fdopen(fd, "w") as jf:
            json.dump(out, jf, indent=2)
        os.rename(tmp_path, json_path)
        size = os.path.getsize(json_path)
        return (json_path, f"OK ({size} bytes, {len(out)} keys)")
    except Exception as e:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
        return (json_path, f"ERROR writing JSON: {e}")


def main():
    parser = argparse.ArgumentParser(description="Regenerate 0-byte runs_summary JSON files from ROOT outputs")
    parser.add_argument("--skim-name", type=str, required=True,
                        help="Skim name (e.g. VBSVVH_skim_v27). Output base is derived as /cmsuf/data/store/user/phchang/skim/<skim-name>")
    parser.add_argument("--base-dir", type=str, default=None,
                        help="Override output base directory (instead of deriving from --skim-name)")
    parser.add_argument("--execute", action="store_true", help="Actually write files (default: dry-run)")
    parser.add_argument("--jobs", type=int, default=4, help="Number of parallel workers (default: 4)")
    args = parser.parse_args()

    output_base = args.base_dir if args.base_dir else os.path.join(SKIM_BASE, args.skim_name)

    if not os.path.isdir(output_base):
        print(f"ERROR: output base directory does not exist: {output_base}")
        sys.exit(1)

    dry_run = not args.execute
    if dry_run:
        print("=== DRY RUN (pass --execute to write files) ===\n")
    else:
        print("=== EXECUTING: will overwrite 0-byte JSON files ===\n")

    print(f"Scanning {output_base} ...")
    pairs = find_zero_byte_runs_summaries(output_base)
    print(f"Found {len(pairs)} zero-byte runs_summary files with valid ROOT outputs\n")

    if not pairs:
        print("Nothing to do.")
        return

    ok = 0
    fail = 0
    with ProcessPoolExecutor(max_workers=args.jobs) as pool:
        futures = {pool.submit(process_one, jp, rp, dry_run): jp for jp, rp in pairs}
        for future in as_completed(futures):
            json_path, msg = future.result()
            rel = os.path.relpath(json_path, output_base)
            print(f"  {rel}: {msg}")
            if msg.startswith("OK") or msg.startswith("WOULD"):
                ok += 1
            else:
                fail += 1

    print(f"\nDone: {ok} succeeded, {fail} failed")


if __name__ == "__main__":
    main()
