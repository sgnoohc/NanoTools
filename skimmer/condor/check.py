#!/usr/bin/env python3
"""
Validation script for skim campaign output.
Checks JSON validity, key completeness, value sanity, file pairing,
cutflow consistency, and job completeness.

Usage:
    python3 check.py --skim-name VBSVVH_skim_v27
    python3 check.py --skim-name VBSVVH_skim_v27 --subdir Run2_Bkg_v15_v27_0Lep1FJ
    python3 check.py --skim-name VBSVVH_skim_v27 --no-dashboard --check-root
"""

import argparse
import csv
import glob
import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

# Only imported when --check-root is used
ROOT = None

SKIM_BASE = "/cmsuf/data/store/user/phchang/skim"

MC_REQUIRED_KEYS = ["eventCount", "genEventCount", "genEventSumw", "genEventSumw2",
                     "LHEScaleSumw", "LHEPdfSumw", "PSSumw"]
DATA_REQUIRED_KEYS = ["eventCount"]
CUTFLOW_COLUMNS = ["cut", "raw_events", "weighted_events"]


def classify_sample(subdir_name):
    """Return 'data', 'mc', or 'sig' based on subdirectory name."""
    if "_Data_" in subdir_name:
        return "data"
    elif "_Sig_" in subdir_name:
        return "sig"
    else:
        return "mc"


def find_job_indices(dataset_path):
    """Find all job indices present in a dataset directory from any output file."""
    indices = set()
    for f in os.listdir(dataset_path):
        for prefix in ("output_", "cutflow_", "runs_summary_"):
            if f.startswith(prefix):
                # Extract index: prefix{N}.ext
                base = f[len(prefix):]
                idx_str = base.split(".")[0]
                try:
                    indices.add(int(idx_str))
                except ValueError:
                    pass
    return sorted(indices)


def check_json(json_path, sample_type):
    """Check a runs_summary JSON file. Returns list of (severity, message)."""
    issues = []
    try:
        with open(json_path) as f:
            data = json.load(f)
    except (json.JSONDecodeError, Exception) as e:
        issues.append(("ERROR", f"Invalid JSON: {e}"))
        return issues, None

    # Key completeness
    if sample_type == "data":
        required = DATA_REQUIRED_KEYS
    else:
        required = MC_REQUIRED_KEYS

    for key in required:
        if key not in data:
            issues.append(("ERROR", f"Missing key '{key}'"))

    # Value sanity
    ec = data.get("eventCount", None)
    if ec is not None and ec <= 0:
        issues.append(("ERROR", f"eventCount={ec} (expected > 0)"))

    if sample_type != "data":
        gec = data.get("genEventCount", None)
        gesw = data.get("genEventSumw", None)
        gesw2 = data.get("genEventSumw2", None)

        if gec is not None and ec is not None and gec < ec:
            issues.append(("ERROR", f"genEventCount={gec} < eventCount={ec}"))
        if gesw is not None and gesw == 0:
            issues.append(("ERROR", f"genEventSumw=0"))
        if gesw2 is not None and gesw2 <= 0:
            issues.append(("ERROR", f"genEventSumw2={gesw2} (expected > 0)"))

        lhe_scale = data.get("LHEScaleSumw", None)
        if lhe_scale is not None and len(lhe_scale) != 9:
            issues.append(("WARNING", f"LHEScaleSumw has {len(lhe_scale)} entries (expected 9)"))

        ps = data.get("PSSumw", None)
        if ps is not None and len(ps) == 0:
            issues.append(("WARNING", f"PSSumw is empty"))

        lhe_pdf = data.get("LHEPdfSumw", None)
        if lhe_pdf is not None and len(lhe_pdf) == 0:
            issues.append(("WARNING", f"LHEPdfSumw is empty"))

    return issues, data


def check_cutflow(csv_path):
    """Check a cutflow CSV. Returns list of (severity, message) and parsed dict."""
    issues = []
    cuts = {}
    try:
        with open(csv_path) as f:
            reader = csv.DictReader(f)
            cols = reader.fieldnames or []
            for expected in CUTFLOW_COLUMNS:
                if expected not in cols:
                    issues.append(("ERROR", f"Missing column '{expected}'"))
                    return issues, cuts
            for row in reader:
                cut_name = row["cut"]
                try:
                    raw = float(row["raw_events"])
                except (ValueError, KeyError):
                    raw = None
                try:
                    wgt = float(row["weighted_events"])
                except (ValueError, KeyError):
                    wgt = None
                cuts[cut_name] = (raw, wgt)
    except Exception as e:
        issues.append(("ERROR", f"Cannot parse cutflow CSV: {e}"))
        return issues, cuts

    if "AllEvents" in cuts:
        raw_all, _ = cuts["AllEvents"]
        if raw_all is not None and raw_all <= 0:
            issues.append(("ERROR", f"AllEvents raw_events={raw_all} (expected > 0)"))
    else:
        issues.append(("ERROR", "Missing 'AllEvents' row in cutflow"))

    if "TheEnd" in cuts:
        raw_end, _ = cuts["TheEnd"]
        if raw_end is not None and raw_end < 0:
            issues.append(("ERROR", f"TheEnd raw_events={raw_end} (expected >= 0)"))
    else:
        issues.append(("WARNING", "Missing 'TheEnd' row in cutflow"))

    return issues, cuts


def check_root_file(root_path, json_data):
    """Open ROOT file and check structural integrity. Returns [(severity, msg)]."""
    issues = []
    try:
        f = ROOT.TFile.Open(root_path)
        if not f or f.IsZombie():
            issues.append(("ERROR", "ROOT file is zombie (corrupt)"))
            return issues
        if f.TestBit(ROOT.TFile.kRecovered):
            issues.append(("WARNING", "ROOT file was auto-recovered (possibly corrupt)"))
        t = f.Get("Events")
        if not t:
            issues.append(("ERROR", "No 'Events' tree in ROOT file"))
        elif json_data:
            ec = json_data.get("eventCount")
            if ec is not None and t.GetEntries() != ec:
                issues.append(("ERROR",
                    f"Events entries={t.GetEntries()} != runs_summary eventCount={ec}"))
        f.Close()
    except Exception as e:
        issues.append(("ERROR", f"Cannot open ROOT file: {e}"))
    return issues


def check_dataset(dataset_path, sample_type, verbose=False, check_root=False):
    """Run all checks on a single dataset directory. Returns list of (severity, message)."""
    issues = []
    indices = find_job_indices(dataset_path)

    if not indices:
        issues.append(("ERROR", "No output files found"))
        return issues

    # Check for gaps
    if indices:
        expected = set(range(min(indices), max(indices) + 1))
        missing = expected - set(indices)
        if missing:
            issues.append(("WARNING", f"Missing job indices: {sorted(missing)}"))

    for idx in indices:
        root_file = os.path.join(dataset_path, f"output_{idx}.root")
        csv_file = os.path.join(dataset_path, f"cutflow_{idx}.csv")
        json_file = os.path.join(dataset_path, f"runs_summary_{idx}.json")

        prefix = f"[job {idx}]"

        # File pairing
        root_exists = os.path.exists(root_file)
        csv_exists = os.path.exists(csv_file)
        json_exists = os.path.exists(json_file)

        if not root_exists:
            issues.append(("ERROR", f"{prefix} Missing output_{idx}.root"))
        if not csv_exists:
            issues.append(("ERROR", f"{prefix} Missing cutflow_{idx}.csv"))
        if not json_exists:
            issues.append(("ERROR", f"{prefix} Missing runs_summary_{idx}.json"))

        # ROOT file size
        if root_exists:
            size = os.path.getsize(root_file)
            if size == 0:
                issues.append(("ERROR", f"{prefix} output_{idx}.root is 0 bytes"))

        # JSON checks
        json_data = None
        if json_exists:
            json_issues, json_data = check_json(json_file, sample_type)
            for sev, msg in json_issues:
                issues.append((sev, f"{prefix} {msg}"))

        # ROOT file integrity check
        if check_root and root_exists:
            root_issues = check_root_file(root_file, json_data)
            for sev, msg in root_issues:
                issues.append((sev, f"{prefix} {msg}"))

        # Cutflow checks
        cuts = {}
        if csv_exists:
            csv_issues, cuts = check_cutflow(csv_file)
            for sev, msg in csv_issues:
                issues.append((sev, f"{prefix} {msg}"))

        # Cross-check JSON vs cutflow
        if json_data and cuts:
            # eventCount (post-skim) should match TheEnd in cutflow
            ec = json_data.get("eventCount", None)
            if ec is not None and "TheEnd" in cuts:
                raw_end, _ = cuts["TheEnd"]
                if raw_end is not None and abs(ec - raw_end) > 0.5:
                    issues.append(("ERROR", f"{prefix} eventCount={ec} != TheEnd={raw_end}"))
            # For MC: genEventCount should match AllEvents in cutflow
            if sample_type != "data":
                gec = json_data.get("genEventCount", None)
                if gec is not None and "AllEvents" in cuts:
                    raw_all, _ = cuts["AllEvents"]
                    if raw_all is not None and abs(gec - raw_all) > 0.5:
                        issues.append(("ERROR", f"{prefix} genEventCount={gec} != AllEvents={raw_all}"))


    return issues


def check_dashboard_completeness(dashboard_glob):
    """Check dashboard summary.json files for incomplete jobs."""
    issues = []
    summary_files = sorted(glob.glob(dashboard_glob))
    if not summary_files:
        issues.append(("WARNING", "No dashboard summary files found"))
        return issues

    for sf in summary_files:
        rel = sf.replace(os.path.expanduser("~/public_html/"), "")
        try:
            with open(sf) as f:
                data = json.load(f)
        except Exception as e:
            issues.append(("ERROR", f"Dashboard {rel}: cannot parse: {e}"))
            continue

        for dataset_name, info in data.items():
            jobs = info.get("jobs", {})
            total = len(jobs)
            done = sum(1 for j in jobs.values()
                       if j.get("output", [None, None])[0] and j.get("output_exists", False))
            if done < total:
                issues.append(("WARNING",
                    f"Dashboard {rel}: {dataset_name} has {done}/{total} jobs done"))

    return issues


def extract_version(skim_name):
    """Extract the version suffix (e.g. 'v27') from a skim name like 'VBSVVH_skim_v27'."""
    m = re.search(r'_(v\d+)$', skim_name)
    return m.group(1) if m else None


def main():
    parser = argparse.ArgumentParser(description="Validate skim campaign output")
    parser.add_argument("--skim-name", type=str, required=True,
                        help="Skim name (e.g. VBSVVH_skim_v27). Output base is derived as /cmsuf/data/store/user/phchang/skim/<skim-name>")
    parser.add_argument("--base-dir", type=str, default=None,
                        help="Override output base directory (instead of deriving from --skim-name)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show per-file details")
    parser.add_argument("--subdir", type=str, default=None,
                        help="Only check a specific subdirectory (e.g. Run2_Bkg_v15_v27_0Lep1FJ)")
    parser.add_argument("--no-dashboard", action="store_true",
                        help="Skip dashboard completeness check")
    parser.add_argument("--check-root", action="store_true",
                        help="Open ROOT files to check IsZombie/kRecovered (requires PyROOT)")
    args = parser.parse_args()

    output_base = args.base_dir if args.base_dir else os.path.join(SKIM_BASE, args.skim_name)
    version = extract_version(args.skim_name)
    if version:
        dashboard_glob = os.path.expanduser(f"~/public_html/Run*_{version}/*/summary.json")
    else:
        dashboard_glob = os.path.expanduser(f"~/public_html/Run*_{args.skim_name}/*/summary.json")

    if not os.path.isdir(output_base):
        print(f"ERROR: output base directory does not exist: {output_base}")
        sys.exit(1)

    if args.check_root:
        try:
            import ROOT as _ROOT
            _ROOT.gROOT.SetBatch(True)
            global ROOT
            ROOT = _ROOT
        except ImportError:
            print("ERROR: --check-root requires PyROOT (import ROOT failed)")
            sys.exit(1)

    all_issues = {}  # subdir -> dataset -> [(severity, message)]
    summary = {}     # subdir -> {datasets, errors, warnings}

    subdirs = sorted(os.listdir(output_base))
    if args.subdir:
        subdirs = [s for s in subdirs if s == args.subdir]
        if not subdirs:
            print(f"ERROR: subdirectory '{args.subdir}' not found in {output_base}")
            sys.exit(1)

    total_datasets = 0
    total_errors = 0
    total_warnings = 0

    for subdir in subdirs:
        subdir_path = os.path.join(output_base, subdir)
        if not os.path.isdir(subdir_path):
            continue

        sample_type = classify_sample(subdir)
        datasets = sorted([d for d in os.listdir(subdir_path)
                           if os.path.isdir(os.path.join(subdir_path, d))])

        sub_errors = 0
        sub_warnings = 0
        all_issues[subdir] = {}

        for dataset in datasets:
            ds_path = os.path.join(subdir_path, dataset)
            issues = check_dataset(ds_path, sample_type, verbose=args.verbose,
                                   check_root=args.check_root)

            if issues:
                all_issues[subdir][dataset] = issues
                for sev, _ in issues:
                    if sev == "ERROR":
                        sub_errors += 1
                    else:
                        sub_warnings += 1

        summary[subdir] = {
            "datasets": len(datasets),
            "errors": sub_errors,
            "warnings": sub_warnings,
        }
        total_datasets += len(datasets)
        total_errors += sub_errors
        total_warnings += sub_warnings

        status = "OK" if sub_errors == 0 and sub_warnings == 0 else \
                 f"{sub_errors}E/{sub_warnings}W"
        print(f"  {subdir:<45s} {len(datasets):>5d} datasets   {status}")

    # Dashboard check
    dashboard_issues = []
    if not args.no_dashboard:
        print("\nChecking dashboard completeness...")
        dashboard_issues = check_dashboard_completeness(dashboard_glob)
        for sev, msg in dashboard_issues:
            if sev == "ERROR":
                total_errors += 1
            else:
                total_warnings += 1

    # Summary
    print(f"\n{'='*70}")
    print(f"SUMMARY: {total_datasets} datasets, {total_errors} errors, {total_warnings} warnings")
    print(f"{'='*70}")

    # Detailed issues
    if total_errors > 0 or total_warnings > 0:
        # Errors first
        if total_errors > 0:
            print(f"\n--- ERRORS ---")
            for subdir in sorted(all_issues):
                for dataset in sorted(all_issues[subdir]):
                    errs = [(s, m) for s, m in all_issues[subdir][dataset] if s == "ERROR"]
                    if errs:
                        print(f"\n  {subdir}/{dataset}")
                        for _, msg in errs:
                            print(f"    ERROR: {msg}")
            for sev, msg in dashboard_issues:
                if sev == "ERROR":
                    print(f"    ERROR: {msg}")

        if total_warnings > 0:
            print(f"\n--- WARNINGS ---")
            for subdir in sorted(all_issues):
                for dataset in sorted(all_issues[subdir]):
                    warns = [(s, m) for s, m in all_issues[subdir][dataset] if s == "WARNING"]
                    if warns:
                        print(f"\n  {subdir}/{dataset}")
                        for _, msg in warns:
                            print(f"    WARNING: {msg}")
            for sev, msg in dashboard_issues:
                if sev == "WARNING":
                    print(f"    WARNING: {msg}")

    elif args.verbose:
        print("\nAll checks passed!")

    sys.exit(0 if total_errors == 0 else 1)


if __name__ == "__main__":
    main()
