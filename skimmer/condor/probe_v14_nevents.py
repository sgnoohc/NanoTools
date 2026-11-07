#!/usr/bin/env python3
"""
Write the counts.json that make_v14_nevents.py turns into v14_nevents.py.

Rows: [era, category, sname, nfiles, mean_entries_or_null] for EVERY v14 sample
in the index. Samples already in v14_nevents.v14_info keep their cached
evts_per_file (no re-probe -- the cache is a splitting estimate, see its header);
samples missing from it are probed by opening up to --nprobe files (the staged
/cmsuf copy when present, else xrootd) and averaging Events entries. nfiles is
the CURRENT file count after vbsvvh_v14's duplicate-task drop list.

Usage:
  python3 probe_v14_nevents.py counts.json && python3 make_v14_nevents.py counts.json
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
import vbsvvh_v14 as v  # noqa: E402
from v14_nevents import v14_info  # noqa: E402

FALLBACK = 20000  # make_v14_nevents.DEFAULT_EVTS_PER_FILE


def probe(files, n):
    import uproot
    picks = [files[int(i * len(files) / n)] for i in range(min(n, len(files)))]
    ents = []
    for u in picks:
        i = u.find("/store/")
        loc = os.path.join(v.STAGE_ROOT, u[i + 7:]) if i >= 0 else u
        p = loc if os.path.isfile(loc) else u
        try:
            with uproot.open(p) as f:
                ents.append(f["Events"].num_entries)
        except Exception as e:  # noqa: BLE001
            print(f"  [probe-fail] {p}: {e}", file=sys.stderr)
    return sum(ents) / len(ents) if ents else None


def main():
    out_path = sys.argv[1]
    nprobe = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    idx = v._load_index()
    rows, n_cached, n_probed, n_failed = [], 0, 0, 0
    for era, cats in idx.items():
        for cat, ss in cats.items():
            for sname, files in ss.items():
                drop = v._dropped(era, cat, sname)
                files = [u for u in files if u not in drop]
                if not files:
                    continue
                name = v.dataset_name(era, cat, sname)
                if name in v14_info:
                    epf = v14_info[name]["evts_per_file"]
                    rows.append([era, cat, sname, len(files), None if epf == FALLBACK else epf])
                    n_cached += 1
                    continue
                mean = probe(files, nprobe)
                n_probed += 1
                n_failed += mean is None
                print(f"  probed {name}: {len(files)} files, mean {mean}")
                rows.append([era, cat, sname, len(files), mean])
    json.dump(rows, open(out_path, "w"))
    print(f"rows={len(rows)} cached={n_cached} probed={n_probed} probe_failed={n_failed} -> {out_path}")


if __name__ == "__main__":
    main()
