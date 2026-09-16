#!/usr/bin/env python3
"""
Profile v2 SLURM jobs: runtime, events/job, time/event, by sample type and channel.
Reads task directories from /blue/avery/p.chang/tasks/*_v2_* and queries sacct.
"""

import os
import re
import glob
import subprocess
import json
import sys
from collections import defaultdict
from das_nevents import das_info

TASKS_DIR = "/blue/avery/p.chang/tasks"

def find_v2_tasks():
    """Find all v2 task directories."""
    pattern = os.path.join(TASKS_DIR, "SLURMTask_*_v2_*")
    return sorted(glob.glob(pattern))

def parse_log(logfile):
    """Extract key info from a SLURM .out log file."""
    info = {}
    with open(logfile, "r", errors="replace") as f:
        for line in f:
            if line.startswith("[slurm_wrapper] SLURM_JOB_ID"):
                info["job_id"] = line.strip().split("=")[-1].strip()
            elif line.startswith("[slurm_wrapper] time ="):
                info["start_epoch"] = int(line.strip().split("=")[-1].strip())
            elif line.startswith("INPUTFILENAMES:"):
                fnames = line.strip().split(":", 1)[1].strip()
                info["input_files"] = [f.strip() for f in fnames.split(",") if f.strip()]
                info["nfiles"] = len(info["input_files"])
            elif "Copy success" in line:
                info["success"] = True
            elif "[parallel] Total input files:" in line:
                m = re.search(r"Total input files: (\d+), workers: (\d+)", line)
                if m:
                    info["nfiles_parallel"] = int(m.group(1))
                    info["nworkers"] = int(m.group(2))
    return info

def extract_dataset_from_inputs(input_files):
    """Extract the DAS dataset path from input file URLs."""
    if not input_files:
        return None
    # e.g. root://cmsxrootd.fnal.gov//store/data/Run2016B/DoubleEG/NANOAOD/HIPM_UL2016_NanoAODv15-v1/120000/xxx.root
    # -> /DoubleEG/Run2016B-HIPM_UL2016_NanoAODv15-v1/NANOAOD
    f = input_files[0]
    # Extract /store/... path
    m = re.search(r"/store/(data|mc)/([^/]+)/([^/]+)/([^/]+)/([^/]+)/", f)
    if m:
        run_era = m.group(2)
        primary = m.group(3)
        tier = m.group(4)
        campaign = m.group(5)
        return f"/{primary}/{run_era}-{campaign}/{tier}"
    # Try local file path pattern
    m = re.search(r"(data|mc)/([^/]+)/([^/]+)/([^/]+)/([^/]+)/", f)
    if m:
        run_era = m.group(2)
        primary = m.group(3)
        tier = m.group(4)
        campaign = m.group(5)
        return f"/{primary}/{run_era}-{campaign}/{tier}"
    return None

def extract_task_info(dirname):
    """Extract sample name and channel from task directory name."""
    base = os.path.basename(dirname)
    # SLURMTask_{dataset}_{unique_key}_v2_{channel}
    # The _v2_ splits the key from the channel
    m = re.match(r"SLURMTask_(.+?)_v2_(.+)$", base)
    if m:
        sample_part = m.group(1)
        channel = m.group(2)
        return sample_part, channel
    return base, "unknown"

def get_sample_type(dirname):
    """Determine if sample is Data, Bkg (MC background), or Sig (signal)."""
    base = os.path.basename(dirname)
    if "_Data_" in base:
        return "Data"
    elif "_Sig_" in base or "VBFVVH" in base or "_Signal_" in base:
        return "Sig"
    else:
        return "Bkg"

def batch_sacct(job_ids):
    """Query sacct for a batch of job IDs."""
    if not job_ids:
        return {}
    # Query in chunks to avoid command-line length limits
    results = {}
    chunk_size = 200
    for i in range(0, len(job_ids), chunk_size):
        chunk = job_ids[i:i+chunk_size]
        job_list = ",".join(chunk)
        cmd = [
            "sacct", "-j", job_list, "-P", "--noheader",
            "--format=JobID,Elapsed,Start,End,State,MaxRSS,ExitCode"
        ]
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            for line in r.stdout.strip().splitlines():
                parts = line.split("|")
                if len(parts) >= 7:
                    jid = parts[0]
                    # Only want the main job line (not .batch or .extern)
                    if "." not in jid:
                        results[jid] = {
                            "elapsed": parts[1],
                            "start": parts[2],
                            "end": parts[3],
                            "state": parts[4],
                            "maxrss": parts[5],
                            "exitcode": parts[6],
                        }
                    elif ".batch" in jid:
                        base_jid = jid.split(".")[0]
                        if base_jid in results:
                            results[base_jid]["maxrss"] = parts[5]
        except Exception as e:
            print(f"  sacct error: {e}", file=sys.stderr)
    return results

def elapsed_to_seconds(elapsed_str):
    """Convert HH:MM:SS or D-HH:MM:SS to seconds."""
    if not elapsed_str:
        return None
    parts = elapsed_str.split("-")
    if len(parts) == 2:
        days = int(parts[0])
        hms = parts[1]
    else:
        days = 0
        hms = parts[0]
    h, m, s = hms.split(":")
    return days * 86400 + int(h) * 3600 + int(m) * 60 + int(s)

def maxrss_to_mb(rss_str):
    """Convert sacct MaxRSS (e.g., '2332824K') to MB."""
    if not rss_str:
        return None
    rss_str = rss_str.strip()
    if rss_str.endswith("K"):
        return float(rss_str[:-1]) / 1024
    elif rss_str.endswith("M"):
        return float(rss_str[:-1])
    elif rss_str.endswith("G"):
        return float(rss_str[:-1]) * 1024
    return None

def fmt_time(seconds):
    """Format seconds as human-readable."""
    if seconds is None:
        return "N/A"
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    if h > 0:
        return f"{h}h{m:02d}m{s:02d}s"
    return f"{m}m{s:02d}s"

def percentile(sorted_list, p):
    """Compute p-th percentile from sorted list."""
    if not sorted_list:
        return None
    k = (len(sorted_list) - 1) * p / 100.0
    f = int(k)
    c = f + 1
    if c >= len(sorted_list):
        return sorted_list[f]
    return sorted_list[f] + (k - f) * (sorted_list[c] - sorted_list[f])

def print_stats(label, values, unit=""):
    """Print statistics for a list of values."""
    if not values:
        print(f"  {label}: no data")
        return
    sv = sorted(values)
    avg = sum(sv) / len(sv)
    p50 = percentile(sv, 50)
    p90 = percentile(sv, 90)
    p99 = percentile(sv, 99)
    if unit == "s":
        print(f"  {label} (n={len(sv)}): mean={fmt_time(avg)}  median={fmt_time(p50)}  p90={fmt_time(p90)}  p99={fmt_time(p99)}  min={fmt_time(sv[0])}  max={fmt_time(sv[-1])}")
    elif unit == "MB":
        print(f"  {label} (n={len(sv)}): mean={avg:.0f}MB  median={p50:.0f}MB  p90={p90:.0f}MB  max={sv[-1]:.0f}MB")
    else:
        print(f"  {label} (n={len(sv)}): mean={avg:.2f}  median={p50:.2f}  p90={p90:.2f}  max={sv[-1]:.2f}{unit}")

def main():
    print("=" * 80)
    print("SLURM Job Profiling: v2 Tasks")
    print("=" * 80)

    # 1. Find all v2 task directories
    task_dirs = find_v2_tasks()
    print(f"\nFound {len(task_dirs)} v2 task directories")

    # 2. Parse logs and collect job IDs
    print("\nParsing log files...")
    jobs = []  # list of dicts with all job info
    job_ids = []

    for tdir in task_dirs:
        log_dir = os.path.join(tdir, "logs", "std_logs")
        if not os.path.isdir(log_dir):
            continue
        out_files = glob.glob(os.path.join(log_dir, "slurm_*.out"))
        if not out_files:
            continue

        sample_part, channel = extract_task_info(tdir)
        sample_type = get_sample_type(tdir)

        for outf in out_files:
            log_info = parse_log(outf)
            if "job_id" not in log_info:
                continue

            # Determine dataset and events
            ds_path = extract_dataset_from_inputs(log_info.get("input_files", []))
            nfiles = log_info.get("nfiles", 0)

            evts_per_file = 0
            total_events = 0
            if ds_path and ds_path in das_info:
                evts_per_file = das_info[ds_path]["evts_per_file"]
                total_events = nfiles * evts_per_file

            jobs.append({
                "task_dir": os.path.basename(tdir),
                "job_id": log_info["job_id"],
                "sample_part": sample_part,
                "channel": channel,
                "sample_type": sample_type,
                "dataset": ds_path or "unknown",
                "nfiles": nfiles,
                "evts_per_file": evts_per_file,
                "total_events": total_events,
                "success": log_info.get("success", False),
                "nworkers": log_info.get("nworkers", 1),
            })
            job_ids.append(log_info["job_id"])

    print(f"Parsed {len(jobs)} job logs")

    # 3. Query sacct for timing
    print(f"\nQuerying sacct for {len(job_ids)} jobs...")
    sacct_data = batch_sacct(job_ids)
    print(f"Got sacct data for {len(sacct_data)} jobs")

    # 4. Merge sacct data
    completed_jobs = []
    failed_jobs = []
    for job in jobs:
        jid = job["job_id"]
        if jid in sacct_data:
            sd = sacct_data[jid]
            job["elapsed_str"] = sd["elapsed"]
            job["elapsed_s"] = elapsed_to_seconds(sd["elapsed"])
            job["state"] = sd["state"]
            job["maxrss_mb"] = maxrss_to_mb(sd.get("maxrss", ""))
            job["exitcode"] = sd["exitcode"]

            if sd["state"] == "COMPLETED" and job["elapsed_s"] and job["elapsed_s"] > 0:
                if job["total_events"] > 0:
                    job["time_per_mevt"] = job["elapsed_s"] / (job["total_events"] / 1e6)
                else:
                    job["time_per_mevt"] = None
                completed_jobs.append(job)
            else:
                failed_jobs.append(job)

    print(f"\nCompleted jobs: {len(completed_jobs)}")
    print(f"Failed/other jobs: {len(failed_jobs)}")

    # Count failures by state
    state_counts = defaultdict(int)
    for j in failed_jobs:
        state_counts[j.get("state", "UNKNOWN")] += 1
    if state_counts:
        print("\nFailed job states:")
        for state, count in sorted(state_counts.items(), key=lambda x: -x[1]):
            print(f"  {state}: {count}")

    # =====================================================================
    # OVERALL STATISTICS
    # =====================================================================
    print("\n" + "=" * 80)
    print("OVERALL STATISTICS (completed jobs)")
    print("=" * 80)

    elapsed_vals = [j["elapsed_s"] for j in completed_jobs if j["elapsed_s"]]
    events_vals = [j["total_events"] for j in completed_jobs if j["total_events"] > 0]
    nfiles_vals = [j["nfiles"] for j in completed_jobs]
    tpmevt_vals = [j["time_per_mevt"] for j in completed_jobs if j.get("time_per_mevt")]
    rss_vals = [j["maxrss_mb"] for j in completed_jobs if j.get("maxrss_mb")]

    print_stats("Wall time", elapsed_vals, unit="s")
    print_stats("Events/job (millions)", [v / 1e6 for v in events_vals])
    print_stats("Files/job", nfiles_vals)
    print_stats("Time per M events", tpmevt_vals, unit="s")
    print_stats("MaxRSS", rss_vals, unit="MB")

    # =====================================================================
    # BY SAMPLE TYPE (Data vs Bkg vs Sig)
    # =====================================================================
    print("\n" + "=" * 80)
    print("BY SAMPLE TYPE")
    print("=" * 80)

    for stype in ["Data", "Bkg", "Sig"]:
        subset = [j for j in completed_jobs if j["sample_type"] == stype]
        if not subset:
            continue
        print(f"\n--- {stype} ({len(subset)} jobs) ---")
        print_stats("  Wall time", [j["elapsed_s"] for j in subset if j["elapsed_s"]], unit="s")
        print_stats("  Events/job (M)", [j["total_events"] / 1e6 for j in subset if j["total_events"] > 0])
        print_stats("  Time/Mevt", [j["time_per_mevt"] for j in subset if j.get("time_per_mevt")], unit="s")
        print_stats("  MaxRSS", [j["maxrss_mb"] for j in subset if j.get("maxrss_mb")], unit="MB")

    # =====================================================================
    # BY CHANNEL
    # =====================================================================
    print("\n" + "=" * 80)
    print("BY ANALYSIS CHANNEL")
    print("=" * 80)

    channels = sorted(set(j["channel"] for j in completed_jobs))
    channel_data = []
    for ch in channels:
        subset = [j for j in completed_jobs if j["channel"] == ch]
        elapsed = [j["elapsed_s"] for j in subset if j["elapsed_s"]]
        tpmevt = [j["time_per_mevt"] for j in subset if j.get("time_per_mevt")]
        rss = [j["maxrss_mb"] for j in subset if j.get("maxrss_mb")]
        if elapsed:
            avg_elapsed = sum(elapsed) / len(elapsed)
            avg_tpmevt = sum(tpmevt) / len(tpmevt) if tpmevt else 0
            avg_rss = sum(rss) / len(rss) if rss else 0
            channel_data.append((ch, len(subset), avg_elapsed, avg_tpmevt, avg_rss))

    if channel_data:
        print(f"\n  {'Channel':<12s} {'Jobs':>6s} {'Avg Time':>10s} {'Avg s/Mevt':>12s} {'Avg RSS':>10s}")
        print(f"  {'-'*12} {'-'*6} {'-'*10} {'-'*12} {'-'*10}")
        for ch, n, avg_t, avg_tpm, avg_rss in sorted(channel_data, key=lambda x: -x[2]):
            print(f"  {ch:<12s} {n:>6d} {fmt_time(avg_t):>10s} {fmt_time(avg_tpm):>12s} {avg_rss:>8.0f}MB")

    # =====================================================================
    # BY DATASET (top 20 slowest)
    # =====================================================================
    print("\n" + "=" * 80)
    print("BY DATASET (top 20 slowest avg runtime)")
    print("=" * 80)

    ds_groups = defaultdict(list)
    for j in completed_jobs:
        ds_groups[j["dataset"]].append(j)

    ds_stats = []
    for ds, jlist in ds_groups.items():
        elapsed = [j["elapsed_s"] for j in jlist if j["elapsed_s"]]
        tpmevt = [j["time_per_mevt"] for j in jlist if j.get("time_per_mevt")]
        if elapsed:
            avg_t = sum(elapsed) / len(elapsed)
            max_t = max(elapsed)
            avg_tpm = sum(tpmevt) / len(tpmevt) if tpmevt else 0
            total_evts = jlist[0]["total_events"] if jlist else 0
            ds_stats.append((ds, len(jlist), avg_t, max_t, avg_tpm, total_evts))

    ds_stats.sort(key=lambda x: -x[2])
    print(f"\n  {'Dataset':<75s} {'Jobs':>5s} {'Avg':>8s} {'Max':>8s} {'s/Mevt':>8s} {'Mevt/job':>9s}")
    print(f"  {'-'*75} {'-'*5} {'-'*8} {'-'*8} {'-'*8} {'-'*9}")
    for ds, n, avg_t, max_t, avg_tpm, total_evts in ds_stats[:20]:
        ds_short = ds if len(ds) <= 75 else "..." + ds[-72:]
        mevt = total_evts / 1e6 if total_evts else 0
        print(f"  {ds_short:<75s} {n:>5d} {fmt_time(avg_t):>8s} {fmt_time(max_t):>8s} {fmt_time(avg_tpm):>8s} {mevt:>8.1f}M")

    # =====================================================================
    # RUNTIME DISTRIBUTION (histogram)
    # =====================================================================
    print("\n" + "=" * 80)
    print("RUNTIME DISTRIBUTION")
    print("=" * 80)

    if elapsed_vals:
        # Buckets in minutes
        buckets = [0, 1, 2, 3, 4, 5, 7, 10, 15, 20, 30, 45, 60, 90, 120, 180, 240, 480]
        counts = [0] * (len(buckets))
        for v in elapsed_vals:
            mins = v / 60
            placed = False
            for i in range(len(buckets) - 1):
                if mins < buckets[i + 1]:
                    counts[i] += 1
                    placed = True
                    break
            if not placed:
                counts[-1] += 1

        max_count = max(counts) if counts else 1
        print(f"\n  {'Range':<18s} {'Count':>6s} {'Pct':>6s}  Bar")
        for i in range(len(buckets)):
            if i < len(buckets) - 1:
                label = f"  {buckets[i]:>3d}-{buckets[i+1]:>3d} min"
            else:
                label = f"  {buckets[i]:>3d}+ min   "
            pct = counts[i] / len(elapsed_vals) * 100
            bar_len = int(counts[i] / max_count * 40) if max_count > 0 else 0
            bar = "#" * bar_len
            if counts[i] > 0:
                print(f"  {label:<18s} {counts[i]:>6d} {pct:>5.1f}%  {bar}")

    # =====================================================================
    # LONGEST RUNNING JOBS (top 20)
    # =====================================================================
    print("\n" + "=" * 80)
    print("TOP 20 LONGEST RUNNING JOBS")
    print("=" * 80)

    by_time = sorted(completed_jobs, key=lambda j: j.get("elapsed_s", 0), reverse=True)[:20]
    print(f"\n  {'JobID':>10s} {'Time':>10s} {'Events':>10s} {'s/Mevt':>8s} {'RSS':>8s} {'Channel':<10s} {'Dataset'}")
    print(f"  {'-'*10} {'-'*10} {'-'*10} {'-'*8} {'-'*8} {'-'*10} {'-'*40}")
    for j in by_time:
        mevt = j['total_events'] / 1e6 if j['total_events'] else 0
        tpm = fmt_time(j.get('time_per_mevt')) if j.get('time_per_mevt') else "N/A"
        rss = f"{j['maxrss_mb']:.0f}MB" if j.get('maxrss_mb') else "N/A"
        ds = j['dataset']
        if len(ds) > 50:
            ds = "..." + ds[-47:]
        print(f"  {j['job_id']:>10s} {fmt_time(j['elapsed_s']):>10s} {mevt:>9.1f}M {tpm:>8s} {rss:>8s} {j['channel']:<10s} {ds}")

    # =====================================================================
    # AGGREGATE RESOURCE USAGE
    # =====================================================================
    print("\n" + "=" * 80)
    print("AGGREGATE RESOURCE USAGE")
    print("=" * 80)

    total_cpu_hours = sum(j["elapsed_s"] * j.get("nworkers", 1) for j in completed_jobs if j["elapsed_s"]) / 3600
    total_wall_hours = sum(j["elapsed_s"] for j in completed_jobs if j["elapsed_s"]) / 3600
    total_events_processed = sum(j["total_events"] for j in completed_jobs if j["total_events"] > 0)

    print(f"\n  Total completed jobs:     {len(completed_jobs)}")
    print(f"  Total wall-clock hours:   {total_wall_hours:.1f} hrs")
    print(f"  Total CPU hours (approx): {total_cpu_hours:.1f} hrs (wall * nworkers)")
    print(f"  Total events processed:   {total_events_processed / 1e9:.2f} billion")
    if total_wall_hours > 0:
        print(f"  Avg throughput:           {total_events_processed / 1e6 / total_wall_hours:.1f} Mevt/wall-hr")
    print()

if __name__ == "__main__":
    main()
