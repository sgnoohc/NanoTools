#!/usr/bin/env python3
"""
Monitor and kill stuck packed SLURM jobs.

Standalone script -- no ProjectMetis imports, only stdlib.
Replicates squeue parsing, duration parsing, and stuck detection logic
from Utils.py and SLURMTask.py.
"""

import argparse
import glob
import os
import subprocess
import sys
import time


TERMINAL_STATES = {"FAILED", "TIMEOUT", "CANCELLED", "NODE_FAIL", "OUT_OF_MEMORY", "SUSPENDED"}


def parse_slurm_duration(time_str):
    """Parse SLURM duration string (D-HH:MM:SS or HH:MM:SS or MM:SS) to seconds."""
    days = 0
    if "-" in time_str:
        days_str, time_str = time_str.split("-", 1)
        days = int(days_str)
    parts = time_str.split(":")
    if len(parts) == 3:
        h, m, s = int(parts[0]), int(parts[1]), int(parts[2])
    elif len(parts) == 2:
        h, m, s = 0, int(parts[0]), int(parts[1])
    else:
        return 0
    return days * 86400 + h * 3600 + m * 60 + s


def format_duration(seconds):
    """Format seconds into a compact human-readable string."""
    seconds = int(seconds)
    if seconds < 60:
        return "{}s".format(seconds)
    elif seconds < 3600:
        m = seconds // 60
        s = seconds % 60
        return "{}m{:02d}s".format(m, s)
    elif seconds < 86400:
        h = seconds // 3600
        m = (seconds % 3600) // 60
        return "{}h{:02d}m".format(h, m)
    else:
        d = seconds // 86400
        h = (seconds % 86400) // 3600
        return "{}d{:02d}h".format(d, h)


def query_packed_jobs():
    """Run squeue and return list of dicts for packed__* jobs."""
    user = os.environ.get("USER", "")
    cmd = ["squeue", "-u", user, "--format=%i %j %T %M %r", "-h"]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode != 0:
            return []
    except Exception:
        return []

    jobs = []
    for line in result.stdout.strip().split("\n"):
        line = line.strip()
        if not line:
            continue
        parts = line.split(None, 4)
        if len(parts) < 4:
            continue
        job_id = parts[0]
        job_name = parts[1]
        state = parts[2]
        time_used = parts[3]
        reason = parts[4] if len(parts) > 4 else ""

        if not job_name.startswith("packed__"):
            continue

        runtime_sec = parse_slurm_duration(time_used)
        jobs.append({
            "job_id": job_id,
            "job_name": job_name,
            "state": state,
            "time_used": time_used,
            "reason": reason,
            "runtime_sec": runtime_sec,
        })
    return jobs


def find_manifest(job_id, task_dir):
    """Glob for packed_{job_id}.manifest under task_dir."""
    pattern = os.path.join(task_dir, "*/logs/packed_{}.manifest".format(job_id))
    matches = glob.glob(pattern)
    return matches[0] if matches else None


def parse_manifest(path):
    """Read tab-separated manifest. Return (list of sub-job dicts, set of unique task names)."""
    subjobs = []
    task_names = set()
    try:
        with open(path) as f:
            for line in f:
                parts = line.strip().split("\t")
                if len(parts) < 2:
                    continue
                task_name = parts[0]
                index = parts[1]
                args = parts[2:] if len(parts) > 2 else []
                subjobs.append({"task_name": task_name, "index": index, "args": args})
                task_names.add(task_name)
    except (IOError, OSError):
        pass
    return subjobs, task_names


def find_log(job_id, task_dir):
    """Glob for slurm_{job_id}.out under task_dir."""
    pattern = os.path.join(task_dir, "*/logs/std_logs/slurm_{}.out".format(job_id))
    matches = glob.glob(pattern)
    return matches[0] if matches else None


def classify_job(job, max_minutes, stale_minutes, task_dir):
    """Determine if a job is stuck. Returns (reason_str, detail_str) or (None, None)."""
    state = job["state"]
    runtime_sec = job["runtime_sec"]
    runtime_min = runtime_sec / 60.0
    job_id = job["job_id"]

    # Terminal states are always flagged
    if state in TERMINAL_STATES:
        return "STATE_{}".format(state), ""

    if state != "RUNNING":
        return None, None

    # Helper to get log staleness in minutes (None if file missing/inaccessible)
    def _log_staleness_min():
        log_path = find_log(job_id, task_dir)
        if log_path is None:
            return None
        try:
            return (time.time() - os.path.getmtime(log_path)) / 60.0
        except OSError:
            return None

    # Long running check
    if runtime_min > max_minutes:
        # Also check for stale log if running long enough
        if runtime_min > 5:
            stale = _log_staleness_min()
            if stale is None:
                return "LOG_MISSING", ""
            if stale > stale_minutes:
                return "STALE_LOG", "(log {})".format(format_duration(stale * 60))
        return "LONG_RUNNING", "(>{})".format(format_duration(max_minutes * 60))

    # Stale log check for jobs running > 5 min but under max_minutes
    if runtime_min > 5:
        stale = _log_staleness_min()
        if stale is None:
            return "LOG_MISSING", ""
        if stale > stale_minutes:
            return "STALE_LOG", "(log {})".format(format_duration(stale * 60))

    return None, None


def shorten_task_names(task_names, max_len=34):
    """Abbreviate a set of task names for display."""
    if not task_names:
        return ""
    names = sorted(task_names)
    # Strip common SLURMTask_ prefix
    short = []
    for n in names:
        if n.startswith("SLURMTask_"):
            n = n[len("SLURMTask_"):]
        # Truncate long names with ..
        if len(n) > 30:
            n = ".." + n[-28:]
        short.append(n)
    result = ", ".join(short)
    if len(result) > max_len:
        result = result[:max_len - 3] + "..."
    return result


def main():
    parser = argparse.ArgumentParser(
        description="Monitor and kill stuck packed SLURM jobs."
    )
    parser.add_argument("--kill", action="store_true",
                        help="Actually cancel stuck jobs (default: dry-run report)")
    parser.add_argument("--max-minutes", type=float, default=5.0,
                        help="Flag RUNNING jobs exceeding this many minutes (default: 5)")
    parser.add_argument("--stale-minutes", type=float, default=45.0,
                        help="Flag jobs whose log is stale for this many minutes (default: 45)")
    parser.add_argument("--task-dir", default="/blue/avery/p.chang/tasks",
                        help="Task directory root (default: /blue/avery/p.chang/tasks)")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Show manifest details and log paths")
    args = parser.parse_args()

    jobs = query_packed_jobs()
    if not jobs:
        print("No packed jobs in queue.")
        return

    # Classify each job
    results = []
    for job in jobs:
        manifest_path = find_manifest(job["job_id"], args.task_dir)
        subjobs, task_names = ([], set())
        if manifest_path:
            subjobs, task_names = parse_manifest(manifest_path)

        reason, detail = classify_job(job, args.max_minutes, args.stale_minutes, args.task_dir)
        reason_str = ""
        if reason:
            reason_str = "{} {}".format(reason, detail).strip()

        results.append({
            "job": job,
            "manifest_path": manifest_path,
            "subjobs": subjobs,
            "task_names": task_names,
            "n_subjobs": len(subjobs),
            "reason": reason,
            "reason_str": reason_str,
        })

    # Print summary table
    header = "{:<12s} {:<12s} {:<9s} {:>5s}  {:<22s} {}".format(
        "JobID", "State", "Runtime", "#Sub", "Reason", "Tasks"
    )
    sep = "{:<12s} {:<12s} {:<9s} {:>5s}  {:<22s} {}".format(
        "-" * 10, "-" * 10, "-" * 8, "-" * 4, "-" * 20, "-" * 34
    )
    print(header)
    print(sep)

    stuck_ids = []
    for r in results:
        job = r["job"]
        tasks_display = shorten_task_names(r["task_names"])
        print("{:<12s} {:<12s} {:<9s} {:>5d}  {:<22s} {}".format(
            job["job_id"],
            job["state"],
            format_duration(job["runtime_sec"]),
            r["n_subjobs"],
            r["reason_str"],
            tasks_display,
        ))
        if r["reason"]:
            stuck_ids.append(job["job_id"])

        if args.verbose:
            if r["manifest_path"]:
                print("    manifest: {}".format(r["manifest_path"]))
            else:
                print("    manifest: NOT FOUND")
            log_path = find_log(job["job_id"], args.task_dir)
            if log_path:
                try:
                    log_age = (time.time() - os.path.getmtime(log_path)) / 60.0
                    print("    log: {} (age: {})".format(log_path, format_duration(log_age * 60)))
                except OSError:
                    print("    log: {} (stat failed)".format(log_path))
            else:
                print("    log: NOT FOUND")
            if r["subjobs"]:
                for sj in r["subjobs"]:
                    print("      sub: {} #{}".format(sj["task_name"], sj["index"]))
            print()

    n_total = len(results)
    n_stuck = len(stuck_ids)
    print("\n{} packed job(s) total, {} stuck.".format(n_total, n_stuck))

    if not stuck_ids:
        return

    if args.kill:
        id_str = " ".join(stuck_ids)
        print("\nCancelling: {}".format(", ".join(stuck_ids)))
        subprocess.run(["scancel"] + stuck_ids, timeout=30)
        print("Done.")
    else:
        print("\n[DRY RUN] Would cancel: {}".format(", ".join(stuck_ids)))
        print("Run with --kill to actually cancel these jobs.")


if __name__ == "__main__":
    main()
