#!/usr/bin/env python3
"""Print '<jobs_done> <jobs_total> <zero_job_tasks> <n_tasks>' for a version's tasks."""
import pickle, os, glob, sys
pat = sys.argv[1] if len(sys.argv) > 1 else "*_v48_4LepLoose"
T = glob.glob(f"/blue/avery/p.chang/tasks/{pat}")
t = d = z = n_err = 0
for D in T:
    try:
        io = pickle.load(open(f"{D}/backup.pkl", "rb"))["io_mapping"]
    except Exception as exc:
        # Do NOT swallow this. Without PYTHONPATH=.../ProjectMetis the metis
        # classes cannot be unpickled, every task is skipped, and the caller
        # reads "0 0" as if nothing were outstanding.
        print(f"ERROR unpickling {os.path.basename(D)}: {type(exc).__name__}: {exc}",
              file=sys.stderr)
        n_err += 1
        continue
    if not io:
        z += 1
        continue
    t += len(io)
    d += sum(os.path.isfile(str(getattr(o, "name", o))) for _, o in io)
if n_err:
    sys.exit(f"ABORT: {n_err}/{len(T)} task dirs unreadable -- refusing to report a state")
print(f"{d} {t} {z} {len(T)}")
