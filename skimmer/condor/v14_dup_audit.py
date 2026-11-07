#!/usr/bin/env python3
"""
Find duplicated events in the v14 PFNano index caused by repeated CRAB tasks.

WHY. make_filelists.py globs everything under each sample's EOS directory. When
the PFNano producers resubmit a CRAB task, the new task writes a fresh
<YYMMDD_HHMMSS>/ directory NEXT TO the old one under the same dataset dir, and
both get indexed. Found 2026-11-07: 2022EE JetMET_Run2022E has two full tasks
(250614_030752, 260208_031014) whose files carry IDENTICAL lumi sets and event
counts -- and v42 read both, so that dataset is double-counted. Shared file
basenames are NOT the test (a CRAB recovery task restarts numbering at 1 but
processes different lumis); lumi content is.

WHAT. For every sample whose files span >1 CRAB task inside ONE dataset dir
(…/<dataset dir>/<task timestamp>/NNNN/x.root), read (run, luminosityBlock) of
every file and decide, at FILE granularity, which files to drop so each lumi is
read once:
  * tasks are ranked by lumi coverage (largest first); the top task is kept whole
  * a lower task whose lumis are >= --whole-task-overlap (0.99) already covered
    is a re-run: DROPPED WHOLE, and the lumis only it had are reported as lost
  * otherwise a file of a lower task is KEPT if all its lumis are new, DROPPED if all are
    already covered, and reported as PARTIAL otherwise (cannot be fixed by file
    selection -- needs event-level dedup or a decision)
Different dataset dirs (ext1, 22Sep2023_v1 vs _v2, JetMET0 vs JetMET1) are
independent statistics and never compared.

Reads the /cmsuf staged copy when present, else the xrootd URL.

OUTPUT. --out JSON: {"<era>|<category>|<sample>": {"drop": [url, ...],
"partial": [url, ...], "tasks": {...summary...}}}. vbsvvh_v14 applies the
"drop" lists (V14_DEDUP_PATH); "partial" must be empty before a launch.

Usage (run on a compute node -- it opens tens of thousands of files):
  python3 v14_dup_audit.py --out v14_dedup.json [--categories VJets_LO,QCD_Mu] -j 16
"""
import argparse
import json
import os
import re
import sys
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor

HERE = os.path.dirname(os.path.realpath(__file__))
INDEX = os.path.join(HERE, "..", "..", "nanoindex_v14_HVV_private.json")
STAGE_ROOT = "/cmsuf/data/store/user/phchang/v14stage"
SKIP_CATEGORIES = {"Tau", "BTagMu"}   # route to no channel; never skimmed
TASK_RE = re.compile(r"^(.*)/(\d{6}_\d{6})/\d{4}/[^/]+\.root$")


def local_or_url(url):
    i = url.find("/store/")
    if i >= 0:
        p = os.path.join(STAGE_ROOT, url[i + len("/store/"):])
        if os.path.isfile(p):
            return p
    return url


def read_lumis(url):
    import uproot
    path = local_or_url(url)
    try:
        with uproot.open(path) as f:
            a = f["LuminosityBlocks"].arrays(["run", "luminosityBlock"], library="np")
            nev = f["Events"].num_entries
        return url, sorted(set(zip(a["run"].tolist(), a["luminosityBlock"].tolist()))), nev, None
    except Exception as e:  # noqa: BLE001 -- report, never guess
        return url, None, None, f"{type(e).__name__}: {e}"


def multi_task_samples(idx, cats):
    """Yield (key, {dsdir: {task: [urls]}}) for samples with >1 task in one dsdir."""
    for era, cd in idx.items():
        for cat, ss in cd.items():
            if cat in SKIP_CATEGORIES or (cats and cat not in cats):
                continue
            for s, files in ss.items():
                g = defaultdict(lambda: defaultdict(list))
                for u in files:
                    m = TASK_RE.match(u)
                    if not m:
                        sys.exit(f"unparseable path (no task timestamp): {u}")
                    g[m.group(1)][m.group(2)].append(u)
                if any(len(t) > 1 for t in g.values()):
                    yield f"{era}|{cat}|{s}", g


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--categories", default="", help="comma list; default all")
    ap.add_argument("-j", "--jobs", type=int, default=8)
    ap.add_argument("--whole-task-overlap", type=float, default=0.99,
                    help="drop a lower-ranked task whole if this fraction of its lumis "
                         "is already covered (default 0.99)")
    args = ap.parse_args()
    cats = set(filter(None, args.categories.split(",")))

    idx = json.load(open(os.path.abspath(INDEX)))
    todo = list(multi_task_samples(idx, cats))
    urls = [u for _, g in todo for t in g.values() if len(t) > 1 for L in t.values() for u in L]
    print(f"samples with repeated CRAB tasks: {len(todo)}   files to read: {len(urls)}", flush=True)

    lumis, nevs, errors = {}, {}, {}
    with ProcessPoolExecutor(args.jobs) as ex:
        for i, (u, ls, nev, err) in enumerate(ex.map(read_lumis, urls, chunksize=16)):
            if err:
                errors[u] = err
            else:
                lumis[u] = set(map(tuple, ls)); nevs[u] = nev
            if (i + 1) % 2000 == 0:
                print(f"  read {i+1}/{len(urls)}", flush=True)

    result, tot_drop, tot_part, tot_drop_ev, tot_lost = {}, 0, 0, 0, 0
    for key, g in todo:
        rec = {"drop": [], "partial": [], "unreadable": [], "tasks": {}}
        for dsdir, tasks in g.items():
            if len(tasks) < 2:
                continue
            cover = {t: set().union(*(lumis.get(u, set()) for u in L)) for t, L in tasks.items()}
            order = sorted(tasks, key=lambda t: (-len(cover[t]), t))
            seen = set(cover[order[0]])
            for t in order:
                kept = dropped = partial = 0
                lost = 0
                # A lower-ranked task that is (almost) entirely a re-run of lumis
                # already read is dropped WHOLE: its files are split at different lumi
                # boundaries, so per-file selection would leave PARTIAL files that
                # cannot be taken without double-counting. The price is the few lumis
                # only it had ("lost_lumis", reported). Found 2026-11-07 on the
                # 2023BPix data: tasks of 4222 lumis each, 4206 shared.
                whole = (t != order[0] and cover[t]
                         and len(cover[t] & seen) / len(cover[t]) >= args.whole_task_overlap)
                if whole:
                    lost = len(cover[t] - seen)
                for u in tasks[t]:
                    if u in errors:
                        rec["unreadable"].append(u); continue
                    if t == order[0]:
                        kept += 1; continue
                    if whole:
                        dropped += 1; rec["drop"].append(u); tot_drop_ev += nevs[u]; continue
                    ls = lumis[u]
                    ov = len(ls & seen)
                    if ov == 0:
                        kept += 1; seen |= ls
                    elif ov == len(ls):
                        dropped += 1; rec["drop"].append(u); tot_drop_ev += nevs[u]
                    else:
                        partial += 1; rec["partial"].append(u)
                rec["tasks"][f"{dsdir.rsplit('/',1)[-1]}/{t}"] = dict(
                    files=len(tasks[t]), lumis=len(cover[t]), kept=kept, dropped=dropped,
                    partial=partial, rank=order.index(t), whole_task_dropped=bool(whole),
                    lost_lumis=lost)
        tot_drop += len(rec["drop"]); tot_part += len(rec["partial"])
        tot_lost += sum(v["lost_lumis"] for v in rec["tasks"].values())
        result[key] = rec
        if rec["drop"] or rec["partial"] or rec["unreadable"]:
            print(f"{key}: drop {len(rec['drop'])}  partial {len(rec['partial'])}  unreadable {len(rec['unreadable'])}")
            for tk, v in rec["tasks"].items():
                print(f"    {tk}: {v}")

    json.dump(result, open(args.out, "w"), indent=1, sort_keys=True)
    print(f"\nSUMMARY samples={len(todo)} files_read={len(lumis)} unreadable={len(errors)} "
          f"drop={tot_drop} (events {tot_drop_ev}) partial={tot_part} lost_lumis={tot_lost}  -> {args.out}")
    return 1 if (tot_part or errors) else 0


if __name__ == "__main__":
    sys.exit(main())
