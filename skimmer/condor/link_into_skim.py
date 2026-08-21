#!/usr/bin/env python3
"""
Fold a dedicated skim version into a larger one by relative symlink.

The v32/v33/v35 pattern: skim new samples under their own version, validate,
then link each dataset dir into the corresponding tag of the target skim so
downstream code sees one tree.

  python3 link_into_skim.py --src VBSVVH_skim_v37            # dry-run
  python3 link_into_skim.py --src VBSVVH_skim_v37 --execute

Tags are matched by substituting the version token, so
Run3_Bkg_v15_v37_4Lep -> Run3_Bkg_v15_v30_4Lep. Tags absent from the target
are skipped (e.g. 2Lep4J, which v30 does not have).
"""
import argparse
import os
import sys

BASE = "/cmsuf/data/store/user/phchang/skim"


def version_of(skim_name):
    return skim_name.rsplit("_", 1)[-1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True, help="Source skim name, e.g. VBSVVH_skim_v37")
    ap.add_argument("--dst", default="VBSVVH_skim_v30", help="Target skim name (default VBSVVH_skim_v30)")
    ap.add_argument("--base-dir", default=BASE)
    ap.add_argument("--execute", action="store_true", help="Actually create links (default: dry-run)")
    args = ap.parse_args()

    src_v, dst_v = version_of(args.src), version_of(args.dst)
    src_root = os.path.join(args.base_dir, args.src)
    dst_root = os.path.join(args.base_dir, args.dst)

    for root, label in ((src_root, "source"), (dst_root, "target")):
        if not os.path.isdir(root):
            sys.exit(f"ERROR: {label} not found: {root}")

    planned, collisions, empties, skipped_tags = [], [], [], []

    for tag in sorted(os.listdir(src_root)):
        src_tag = os.path.join(src_root, tag)
        if not os.path.isdir(src_tag):
            continue
        dst_tag_name = tag.replace(f"_{src_v}_", f"_{dst_v}_")
        dst_tag = os.path.join(dst_root, dst_tag_name)
        if not os.path.isdir(dst_tag):
            skipped_tags.append((tag, dst_tag_name))
            continue

        for ds in sorted(os.listdir(src_tag)):
            src_ds = os.path.join(src_tag, ds)
            if not os.path.isdir(src_ds):
                continue
            if not any(f.startswith("output_") and f.endswith(".root") for f in os.listdir(src_ds)):
                empties.append(os.path.join(tag, ds))
                continue
            dst_ds = os.path.join(dst_tag, ds)
            if os.path.lexists(dst_ds):
                collisions.append(os.path.join(dst_tag_name, ds))
                continue
            planned.append((dst_ds, os.path.join("..", "..", args.src, tag, ds)))

    print(f"=== link {args.src} -> {args.dst} ===")
    for tag, dst_tag_name in skipped_tags:
        print(f"  [skip] {tag}: no {dst_tag_name} in target")
    for e in empties:
        print(f"  [skip] {e}: no output_*.root")
    for c in collisions:
        print(f"  [COLLISION] {c} already exists")
    print(f"  planned links : {len(planned)}")
    print(f"  collisions    : {len(collisions)}")
    print(f"  empty sources : {len(empties)}")

    if collisions:
        sys.exit("ERROR: collisions present; refusing to link. Resolve them first.")
    if not args.execute:
        print("\n[dry-run] nothing written. Re-run with --execute.")
        return

    for dst_ds, rel in planned:
        os.symlink(rel, dst_ds)
    print(f"\n[execute] created {len(planned)} symlinks")

    broken = [d for d, _ in planned if not os.path.exists(d)]
    print(f"[verify] broken links: {len(broken)}")
    for b in broken:
        print(f"  BROKEN {b}")
    if broken:
        sys.exit(1)
    print("[verify] all links resolve to real files")


if __name__ == "__main__":
    main()
