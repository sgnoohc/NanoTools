#!/usr/bin/env python3
"""
Delete all output files for job indices that are missing runs_summary_N.json.

This forces MetIS to see those outputs as missing and resubmit them.

For each dataset directory under the skim output base:
  - Find all job indices N that have output_N.root but no runs_summary_N.json
  - Delete: output_N.root, cutflow_N.{csv,cflow,txt}, runs_summary_N.json (if partial)

Usage:
    python3 cleanup_missing_runs_summary.py --skim-name VBSVVH_skim_v27              # dry-run (default)
    python3 cleanup_missing_runs_summary.py --skim-name VBSVVH_skim_v27 --execute     # actually delete files
"""

import argparse
import glob
import os
import re
import sys

SKIM_BASE = "/cmsuf/data/store/user/phchang/skim"


def find_affected(base_dir):
    """Yield (dataset_dir, index, files_to_delete) for each missing runs_summary."""
    # Each tag dir contains dataset subdirs
    for tag_dir in sorted(glob.glob(os.path.join(base_dir, "*"))):
        if not os.path.isdir(tag_dir):
            continue
        for ds_dir in sorted(glob.glob(os.path.join(tag_dir, "*"))):
            if not os.path.isdir(ds_dir):
                continue

            # Find all job indices that have output_N.root
            output_files = glob.glob(os.path.join(ds_dir, "output_*.root"))
            for ofile in sorted(output_files):
                m = re.search(r"output_(\d+)\.root$", ofile)
                if not m:
                    continue
                idx = m.group(1)

                runs_json = os.path.join(ds_dir, f"runs_summary_{idx}.json")
                if os.path.isfile(runs_json):
                    continue  # this index is fine

                # Missing runs_summary — collect all files for this index
                files_to_delete = []
                for pattern in [
                    f"output_{idx}.root",
                    f"cutflow_{idx}.csv",
                    f"cutflow_{idx}.cflow",
                    f"cutflow_{idx}.txt",
                    f"runs_summary_{idx}.json",  # in case partial/empty
                ]:
                    fpath = os.path.join(ds_dir, pattern)
                    if os.path.isfile(fpath):
                        files_to_delete.append(fpath)

                if files_to_delete:
                    yield ds_dir, idx, files_to_delete


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--skim-name", type=str, required=True,
                        help="Skim name (e.g. VBSVVH_skim_v27). Output base is derived as /cmsuf/data/store/user/phchang/skim/<skim-name>")
    parser.add_argument("--base-dir", type=str, default=None,
                        help="Override output base directory (instead of deriving from --skim-name)")
    parser.add_argument("--execute", action="store_true", help="Actually delete files (default is dry-run)")
    args = parser.parse_args()

    args.base_dir = args.base_dir if args.base_dir else os.path.join(SKIM_BASE, args.skim_name)

    if not os.path.isdir(args.base_dir):
        print(f"ERROR: output base directory does not exist: {args.base_dir}")
        sys.exit(1)

    total_indices = 0
    total_files = 0

    for ds_dir, idx, files in find_affected(args.base_dir):
        total_indices += 1
        rel_ds = os.path.relpath(ds_dir, args.base_dir)
        print(f"\n[missing runs_summary_{idx}.json] {rel_ds}")
        for fpath in files:
            total_files += 1
            fname = os.path.basename(fpath)
            if args.execute:
                os.remove(fpath)
                print(f"  DELETED: {fname}")
            else:
                print(f"  would delete: {fname}")

    print(f"\n{'='*60}")
    mode = "DELETED" if args.execute else "would delete"
    print(f"Total: {total_indices} job indices affected, {total_files} files {mode}")
    if not args.execute and total_files > 0:
        print("Re-run with --execute to actually delete files.")


if __name__ == "__main__":
    main()
