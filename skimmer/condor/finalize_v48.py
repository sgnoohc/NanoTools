#!/usr/bin/env python3
"""
Post-processing for the v48 4LepLoose campaign (ZZZ analysis request).

Two steps, both idempotent and both pure-symlink (no data is moved or copied):

1. CONSOLIDATE THE v13 TAG.
   run3_bkg_hh_bbtautau is NanoAODv13, so submit.py keys it as
   Run3_Bkg_v13_v48 and it lands in its own directory -- a fifth directory,
   when the request was for four. v30 solves this by linking those datasets
   into the v15 tag (link_into_skim.py --tag-subst v13=v15), and we do the
   same: the real files stay in the honest v13 directory, and the v15
   directory gains a relative symlink so the full Run 3 MC list is readable
   from one place.

2. Summer24for2025 ERA ALIASES.
   CMS produced no 2025 MC, so the Summer24 samples serve both 2024 and 2025.
   RDataFrame identifies a sample by its path string, so two eras pointing at
   the same directory collapse into one identity and the second silently
   disappears. One relative alias per Summer24 dataset fixes it:
       <dataset>Summer24for2025 -> <dataset>
   Only Summer24 samples qualify: a Run3Summer22 sample (the two bbtautau
   points) does not serve 2025 and is deliberately skipped.

   Note this is MORE complete than v30, where only the 131 datasets from the
   original base run matched; the 37 added later by symlink never received
   aliases.

Usage:
    python3 finalize_v48.py                 # dry run
    python3 finalize_v48.py --execute
"""
import argparse
import os
import sys

BASE = "/cmsuf/data/store/user/phchang/skim"
ALIAS = "Summer24for2025"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skim", default="VBSVVH_skim_v48")
    ap.add_argument("--execute", action="store_true")
    args = ap.parse_args()

    root = os.path.join(BASE, args.skim)
    v15 = os.path.join(root, "Run3_Bkg_v15_v48_4LepLoose")
    v13 = os.path.join(root, "Run3_Bkg_v13_v48_4LepLoose")
    if not os.path.isdir(v15):
        sys.exit(f"missing {v15}")

    mode = "EXECUTE" if args.execute else "DRY RUN (pass --execute to apply)"
    print(f"skim: {args.skim}\nmode: {mode}\n")

    # --- step 1: link the v13 datasets into the v15 tag ---
    made = skipped = 0
    if os.path.isdir(v13):
        for ds in sorted(os.listdir(v13)):
            src = os.path.join(v13, ds)
            if not os.path.isdir(src):
                continue
            dest = os.path.join(v15, ds)
            if os.path.lexists(dest):
                skipped += 1
                continue
            rel = os.path.join("..", os.path.basename(v13), ds)
            print(f"  link  {ds[:72]}")
            if args.execute:
                os.symlink(rel, dest)
            made += 1
    print(f"step 1 (v13 -> v15): {made} new, {skipped} already present\n")

    # --- step 2: Summer24for2025 aliases ---
    ents = os.listdir(v15)
    bases = [e for e in ents if not e.endswith(ALIAS)]
    a_made = a_skip = a_na = 0
    for ds in sorted(bases):
        if "Summer24" not in ds:
            a_na += 1            # e.g. Run3Summer22 -- does not serve 2025
            continue
        dest = os.path.join(v15, ds + ALIAS)
        if os.path.lexists(dest):
            a_skip += 1
            continue
        if args.execute:
            os.symlink(ds, dest)          # relative, same directory
        a_made += 1
    print(f"step 2 (era aliases): {a_made} new, {a_skip} already present, "
          f"{a_na} not Summer24 (skipped)")

    if args.execute:
        ents = os.listdir(v15)
        base_n = len([e for e in ents if not e.endswith(ALIAS)])
        al_n = len([e for e in ents if e.endswith(ALIAS)])
        broken = [e for e in ents
                  if os.path.islink(os.path.join(v15, e))
                  and not os.path.exists(os.path.join(v15, e))]
        print(f"\nfinal Run3_Bkg_v15_v48_4LepLoose: {base_n} datasets + {al_n} aliases")
        print(f"broken symlinks: {len(broken)}")
        for b in broken[:5]:
            print(f"   {b}")
        return 1 if broken else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
