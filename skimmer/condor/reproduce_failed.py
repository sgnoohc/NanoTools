#!/usr/bin/env python3
"""
Given a failed SLURM job ID (packed or regular), find the task info
and print a copy-pastable local command to reproduce the skim.

Usage:
    python3 reproduce_failed.py <SLURM_JOB_ID> [--subtask N]

Examples:
    python3 reproduce_failed.py 26928684              # packed: list sub-tasks
    python3 reproduce_failed.py 26928684 --subtask 0  # packed: command for sub-task 0
    python3 reproduce_failed.py 25892460              # regular: print command directly
    python3 reproduce_failed.py 26928684 --log        # show tail of log files
"""

import argparse
import glob
import os
import re
import subprocess
import sys

BASEDIR = "/blue/avery/p.chang/tasks"
SKIMMER_DIR = os.path.dirname(os.path.abspath(__file__))
SKIM_BINARY = os.path.join(SKIMMER_DIR, "..", "skim")


def get_job_info(job_id):
    """Get job name and state via sacct."""
    try:
        result = subprocess.run(
            ["sacct", "-j", str(job_id), "--format=JobID,JobName%200,State,Start,End",
             "--noheader", "-P"],
            capture_output=True, text=True, timeout=30,
        )
        for line in result.stdout.strip().splitlines():
            fields = line.split("|")
            if fields[0] == str(job_id):
                return {
                    "job_id": fields[0],
                    "job_name": fields[1],
                    "state": fields[2],
                    "start": fields[3],
                    "end": fields[4],
                }
    except Exception:
        pass
    return None


def inputfiles_to_str(inputfiles):
    """Convert comma-separated input file paths to space-separated, with xrootd prefix if needed."""
    files = inputfiles.split(",")
    result = []
    for f in files:
        if f.startswith("root://"):
            result.append(f)
        elif f.startswith("/store"):
            result.append("root://cmsxrootd.fnal.gov/" + f)
        else:
            result.append(f)
    return " ".join(result)


def make_local_command(outputname, inputfiles, extraargs):
    """Build a copy-pastable ./skim command."""
    return "{skim} {inputs} -n {outputname} {extraargs}".format(
        skim=os.path.abspath(SKIM_BINARY),
        inputs=inputfiles_to_str(inputfiles),
        outputname=outputname,
        extraargs=extraargs,
    ).strip()


# ── Packed jobs ──────────────────────────────────────────────────────

def find_manifest(job_id):
    """Search task directories for packed_{job_id}.manifest."""
    pattern = os.path.join(BASEDIR, "*/logs/packed_{}.manifest".format(job_id))
    matches = glob.glob(pattern)
    return matches[0] if matches else None


def parse_manifest(manifest_path):
    """Parse manifest TSV into list of sub-task dicts."""
    subtasks = []
    with open(manifest_path) as f:
        for line in f:
            line = line.rstrip("\n")
            if not line:
                continue
            parts = line.split("\t")
            task_name = parts[0]
            index = parts[1]
            # Fields: OUTPUTDIR OUTPUTNAME INPUTFILENAMES IFILE CMSSWVERSION SCRAMARCH EXTRAARGS...
            args = parts[2].split()
            subtasks.append({
                "task_name": task_name,
                "index": index,
                "outputdir": args[0],
                "outputname": args[1],
                "inputfiles": args[2],
                "ifile": args[3],
                "extraargs": " ".join(args[6:]) if len(args) > 6 else "",
            })
    return subtasks


def handle_packed(job_id, info, args):
    """Handle a packed SLURM job."""
    manifest = find_manifest(job_id)
    if not manifest:
        print("ERROR: No manifest found for job {}".format(job_id))
        print("Searched: {}/*/logs/packed_{}.manifest".format(BASEDIR, job_id))
        sys.exit(1)
    print("Manifest: {}".format(manifest))

    logdir = os.path.dirname(manifest)
    show_log_paths(logdir, job_id)

    if args.log:
        tail_logs(logdir, job_id)
        return

    subtasks = parse_manifest(manifest)
    print("\n{} sub-tasks in this packed job:\n".format(len(subtasks)))

    for i, st in enumerate(subtasks):
        short_name = st["task_name"].replace("SLURMTask_", "")
        nfiles = len(st["inputfiles"].split(","))
        print("  [{:2d}] {} (index={}, {} files, '{}')".format(
            i, short_name, st["index"], nfiles, st["extraargs"]))

    if args.subtask is None:
        print("\nRe-run with --subtask N to get the command, e.g.:")
        print("  python3 {} {} --subtask 0".format(sys.argv[0], job_id))
        return

    if args.subtask < 0 or args.subtask >= len(subtasks):
        print("\nERROR: --subtask {} out of range (0-{})".format(args.subtask, len(subtasks) - 1))
        sys.exit(1)

    st = subtasks[args.subtask]
    cmd = make_local_command(st["outputname"], st["inputfiles"], st["extraargs"])
    print("\n" + "=" * 70)
    print("Sub-task [{:d}]: {} (index={})".format(args.subtask, st["task_name"], st["index"]))
    print("Output dir: {}".format(st["outputdir"]))
    print("=" * 70)
    print("\nCopy-paste this command to reproduce locally:\n")
    print(cmd)
    print()


# ── Regular (non-packed) jobs ────────────────────────────────────────

def find_regular_task(job_name):
    """Parse job_name = '{unique_name}__{index}' and find the submit script."""
    m = re.match(r"^(.+)__(\d+)$", job_name)
    if not m:
        return None, None, None
    unique_name = m.group(1)
    index = m.group(2)
    taskdir = os.path.join(BASEDIR, unique_name)
    submit_script = os.path.join(taskdir, "submit_{}.sh".format(index))
    return unique_name, index, submit_script


def parse_regular_submit(submit_script):
    """Extract executable arguments from a regular submit script."""
    with open(submit_script) as f:
        for line in f:
            # Line looks like: ./executable.sh OUTPUTDIR OUTPUTNAME INPUTFILES IFILE CMSSW SCRAM EXTRAARGS
            if line.strip().startswith("./executable.sh ") or line.strip().startswith("./slurm_executable.sh "):
                args = line.strip().split(None, 7)  # split into max 8 parts
                # args[0] = ./executable.sh
                # args[1] = OUTPUTDIR, args[2] = OUTPUTNAME, args[3] = INPUTFILES
                # args[4] = IFILE, args[5] = CMSSW, args[6] = SCRAM, args[7+] = EXTRAARGS
                if len(args) >= 7:
                    return {
                        "outputdir": args[1],
                        "outputname": args[2],
                        "inputfiles": args[3],
                        "ifile": args[4],
                        "extraargs": " ".join(args[7:]) if len(args) > 7 else "",
                    }
    return None


def handle_regular(job_id, info, args):
    """Handle a regular (non-packed) SLURM job."""
    job_name = info["job_name"]
    unique_name, index, submit_script = find_regular_task(job_name)

    if not unique_name:
        print("ERROR: Could not parse job name '{}'".format(job_name))
        sys.exit(1)

    taskdir = os.path.join(BASEDIR, unique_name)
    logdir = os.path.join(taskdir, "logs")
    show_log_paths(logdir, job_id)

    if args.log:
        tail_logs(logdir, job_id)
        return

    if not os.path.exists(submit_script):
        print("ERROR: Submit script not found: {}".format(submit_script))
        print("(It may have been overwritten by a later submission for the same index)")
        sys.exit(1)

    task_info = parse_regular_submit(submit_script)
    if not task_info:
        print("ERROR: Could not parse arguments from {}".format(submit_script))
        sys.exit(1)

    cmd = make_local_command(task_info["outputname"], task_info["inputfiles"], task_info["extraargs"])
    nfiles = len(task_info["inputfiles"].split(","))

    print("\nTask: {} (index={}, {} input files)".format(unique_name, index, nfiles))
    print("Output dir: {}".format(task_info["outputdir"]))
    print("\n" + "=" * 70)
    print("Copy-paste this command to reproduce locally:\n")
    print(cmd)
    print()


# ── Common helpers ───────────────────────────────────────────────────

def show_log_paths(logdir, job_id):
    std_log = os.path.join(logdir, "std_logs", "slurm_{}.out".format(job_id))
    std_err = os.path.join(logdir, "std_logs", "slurm_{}.err".format(job_id))
    print("Log out:  {}".format(std_log if os.path.exists(std_log) else "(not found)"))
    print("Log err:  {}".format(std_err if os.path.exists(std_err) else "(not found)"))


def tail_logs(logdir, job_id):
    std_log = os.path.join(logdir, "std_logs", "slurm_{}.out".format(job_id))
    std_err = os.path.join(logdir, "std_logs", "slurm_{}.err".format(job_id))
    if os.path.exists(std_log):
        print("\n--- tail of stdout log ---")
        os.system("tail -100 '{}'".format(std_log))
    if os.path.exists(std_err):
        print("\n--- tail of stderr log ---")
        os.system("tail -50 '{}'".format(std_err))


# ── Main ─────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Reproduce a failed SLURM skim job locally")
    parser.add_argument("job_id", help="SLURM job ID")
    parser.add_argument("--subtask", "-s", type=int, default=None,
                        help="Sub-task index (0-based) for packed jobs. Omit to list all.")
    parser.add_argument("--log", "-l", action="store_true",
                        help="Tail the log files for this job")
    args = parser.parse_args()

    job_id = args.job_id

    info = get_job_info(job_id)
    if info:
        print("Job {}: {} ({})".format(info["job_id"], info["job_name"], info["state"]))
    else:
        print("Job {}: (could not query sacct)".format(job_id))
        sys.exit(1)

    is_packed = info["job_name"].startswith("packed__")

    if is_packed:
        handle_packed(job_id, info, args)
    else:
        handle_regular(job_id, info, args)


if __name__ == "__main__":
    main()
