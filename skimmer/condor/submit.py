import os
import sys
import argparse
import math
import subprocess
from datetime import datetime
from time import sleep

from metis.Sample import DBSSample, DirectorySample
from metis.CondorTask import CondorTask
from metis.SLURMTask import SLURMTask
from metis.PackedSLURMSubmitter import PackedSLURMSubmitter
from metis.StatsParser import StatsParser
import samples
from das_nevents import das_info
from sample_channels import is_mc_allowed

condorpath = os.path.dirname(os.path.realpath(__file__))

# ------------------------------------------------------------------
# Helper functions
# ------------------------------------------------------------------
MAX_SUBMITTED = 2500  # stay under avery-b's 3000 QOS limit

def pending_job_count():
    """Count currently queued/running SLURM jobs for this user."""
    result = subprocess.run(
        ["squeue", "-u", os.environ["USER"], "-h"],
        capture_output=True, text=True
    )
    return len(result.stdout.strip().splitlines()) if result.stdout.strip() else 0

MIN_EVENTS_PER_JOB_CONDOR = 3_000_000
MIN_EVENTS_PER_JOB_SLURM = 12_000_000

def query_das_single(dsname):
    """Query dasgoclient for nevents and nfiles for a single dataset."""
    try:
        result_nevents = subprocess.run(
            ["dasgoclient", "-query", f"dataset={dsname} | grep dataset.nevents"],
            capture_output=True, text=True, timeout=120
        )
        nevents = int(result_nevents.stdout.strip()) if result_nevents.stdout.strip() else 0

        result_nfiles = subprocess.run(
            ["dasgoclient", "-query", f"dataset={dsname} | grep dataset.nfiles"],
            capture_output=True, text=True, timeout=120
        )
        nfiles = int(result_nfiles.stdout.strip()) if result_nfiles.stdout.strip() else 0

        evts_per_file = nevents // nfiles if nfiles > 0 else 0
        return {"nevents": nevents, "nfiles": nfiles, "evts_per_file": evts_per_file}
    except Exception as e:
        print(f"ERROR querying DAS for {dsname}: {e}")
        return None

_split_logged = set()  # track which datasets we already printed DAS info for
_das_problems = {}     # dsname -> {"reason": str, "nevents": ..., "nfiles": ...}

def split_func(dsname, min_events_per_job):
    verbose = dsname not in _split_logged
    if dsname not in das_info:
        print(f"  [das] CACHE MISS for {dsname}, querying DAS live...")
        result = query_das_single(dsname)
        if result and result["evts_per_file"] > 0:
            das_info[dsname] = result
            # Append to das_nevents.py so future runs don't need to re-query
            das_nevents_path = os.path.join(condorpath, "das_nevents.py")
            with open(das_nevents_path, "r") as f:
                content = f.read()
            entry = f'    "{dsname}": {{"nevents": {result["nevents"]}, "nfiles": {result["nfiles"]}, "evts_per_file": {result["evts_per_file"]}}},\n'
            content = content.replace("\n}\n", "\n" + entry + "}\n")
            with open(das_nevents_path, "w") as f:
                f.write(content)
            print(f"  [das] Live query OK: {result['nevents']} events, {result['nfiles']} files, {result['evts_per_file']} evts/file -> saved to das_nevents.py")
        else:
            nevts = result["nevents"] if result else "?"
            nfiles = result["nfiles"] if result else "?"
            print(f"  [das] Live query FAILED or empty: nevents={nevts}, nfiles={nfiles} -> defaulting to 20 files/job")
            _das_problems[dsname] = {"reason": "cache_miss_empty", "nevents": nevts, "nfiles": nfiles}
            return 20
    info = das_info[dsname]
    evts_per_file = info["evts_per_file"]
    if evts_per_file > 0:
        files_per_job = max(1, math.ceil(min_events_per_job / evts_per_file))
    else:
        files_per_job = 1
    if verbose:
        print(f"  [das] nevents={info['nevents']:,}  nfiles={info['nfiles']}  evts/file={evts_per_file:,}  -> {files_per_job} files/job (target {min_events_per_job:,} evts/job)")
        _split_logged.add(dsname)
    return files_per_job

def track_zero_files(dsname):
    """Record a dataset that returned 0 input files."""
    if dsname not in _das_problems:
        _das_problems[dsname] = {"reason": "zero_input_files", "nevents": "?", "nfiles": "?"}
    else:
        _das_problems[dsname]["reason"] += "+zero_input_files"

def njobs_to_process(dsname):
    return -1  # -1 = unlimited

def make_unique_key(metadata, version):
    """Auto-construct unique key: {Run}_{Type}_{Nano}_{Version}"""
    return f"{metadata['run']}_{metadata['type']}_{metadata['nano']}_{version}"

# Full channel list for non-signal samples
ALL_CHANNELS = [
    "4Lep",
    "3Lep",
    "2Lep2FJ",
    "2Lep1FJ",
    "1Lep1FJ",
    "0Lep3FJ",
    "0Lep2FJ",
    "0Lep1FJ",
    "0Lep0FJ",
]

# Primary-dataset prefixes allowed per channel family
# Lepton PDs (Run2): MuonEG, DoubleEG, DoubleMuon, SingleMuon, EGamma, SingleElectron
# Lepton PDs (Run3): MuonEG, Muon, Muon0, Muon1, EGamma, EGamma0, EGamma1
# Hadronic PDs (Run2): MET, JetHT
# Hadronic PDs (Run3): JetMET, JetMET0, JetMET1
LEPTON_PDS = {"MuonEG", "DoubleEG", "DoubleMuon", "SingleMuon", "EGamma", "SingleElectron",
              "Muon", "Muon0", "Muon1", "EGamma0", "EGamma1"}
HADRONIC_PDS = {"MET", "JetHT", "JetMET", "JetMET0", "JetMET1"}

CHANNEL_PDS = {
    "4Lep": LEPTON_PDS,
    "3Lep": LEPTON_PDS,
    "2Lep2FJ": LEPTON_PDS,
    "2Lep1FJ": LEPTON_PDS,
    "1Lep1FJ": LEPTON_PDS,
    "0Lep3FJ": HADRONIC_PDS,
    "0Lep2FJ": HADRONIC_PDS,
    "0Lep1FJ": HADRONIC_PDS,
    "0Lep0FJ": HADRONIC_PDS,
}

def get_primary_dataset(dsname):
    """Extract primary dataset name: '/MuonEG/Run2016B-.../NANOAOD' -> 'MuonEG'"""
    return dsname.strip("/").split("/")[0]


# ------------------------------------------------------------------
# Main
# ------------------------------------------------------------------
if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--arch", choices=["el8", "el9"], default="el9",
                        help="Target architecture: el8 (no singularity) or el9 (default, uses singularity)")
    parser.add_argument("--scheduler", choices=["condor", "slurm"], default="slurm",
                        help="Job scheduler: condor or slurm (default)")
    parser.add_argument("--samples", type=str, default=None,
                        help="Comma-separated sample groups to submit (e.g. run2_sig,run2_bkg). Omit to submit ALL groups.")
    parser.add_argument("--version", type=str, default="v1",
                        help="Version suffix for unique_key (default: v1)")
    parser.add_argument("--list-samples", action="store_true",
                        help="Print available sample groups and exit")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print what would be submitted without actually submitting")
    parser.add_argument("--pack-size", type=int, default=1,
                        help="Pack N jobs per SLURM allocation (default 1 = current behavior)")
    parser.add_argument("--cpus-per-subjob", type=int, default=1,
                        help="CPUs per sub-job within a pack (default 1)")
    args = parser.parse_args()

    # --list-samples: print registry and exit
    if args.list_samples:
        samples.list_groups()
        sys.exit(0)

    # Architecture-dependent CMSSW settings (must match setup.sh)
    if args.arch == "el9":
        singularity_image = "/cvmfs/singularity.opensciencegrid.org/cmssw/cms:rhel9"
        cmssw_version = "CMSSW_16_0_0_pre4"
        scram_arch = "el9_amd64_gcc13"
    else:
        singularity_image = "/cvmfs/singularity.opensciencegrid.org/cmssw/cms:rhel8"
        cmssw_version = "CMSSW_14_1_0_pre4"
        scram_arch = "el8_amd64_gcc12"

    # Determine which groups to submit
    if args.samples:
        group_names = [g.strip() for g in args.samples.split(",")]
        for g in group_names:
            if g not in samples.SAMPLE_REGISTRY:
                print(f"ERROR: Unknown sample group '{g}'")
                print("Available groups:")
                samples.list_groups()
                sys.exit(1)
    else:
        group_names = list(samples.SAMPLE_REGISTRY.keys())

    # Skip tail events?
    skip_tail = False

    # ------------------------------------------------------------------
    # Infinite loop until all tasks complete
    # ------------------------------------------------------------------
    while True:
        all_tasks_complete = True
        task_summaries = {}  # unique_key -> {task_key: summary}
        all_unique_keys_and_tags = []
        packed_tasks = []  # collected for packed submission

        # Cache squeue results once per iteration to avoid hundreds of subprocess calls
        from metis.Utils import slurm_q
        cached_all_jobs = slurm_q() if args.scheduler == "slurm" else None

        for group_name in group_names:
            datasets, metadata = samples.get_samples(group_name)
            unique_key = make_unique_key(metadata, args.version)

            # Auto-configure analysis_tags and signal flags based on sample type
            if metadata["type"] == "Sig":
                analysis_tags = ["Sig"]
                signal_flags = "--is_signal --dump_truth"
            else:
                analysis_tags = ALL_CHANNELS
                signal_flags = ""

            print(f"\n=== Group: {group_name} | Key: {unique_key} | Tags: {analysis_tags} ===")

            # ------------------------------------------------------------------
            # Process datasets
            # ------------------------------------------------------------------
            for ds in datasets:
                dsname = ds.get_datasetname()

                # Pre-filter: skip dataset entirely if no active channel accepts it
                if metadata["type"] == "Data":
                    pd_name = get_primary_dataset(dsname)
                    if not any(tag not in CHANNEL_PDS or pd_name in CHANNEL_PDS[tag]
                               for tag in analysis_tags):
                        continue
                elif metadata["type"] == "Bkg":
                    if not any(is_mc_allowed(dsname, tag) for tag in analysis_tags):
                        continue

                # Compute files_per_job (populates das_info cache on miss)
                min_epj = MIN_EVENTS_PER_JOB_SLURM if args.scheduler == "slurm" else MIN_EVENTS_PER_JOB_CONDOR
                fpo = split_func(dsname, min_epj)

                # Use cached nfiles instead of slow DIS get_files() query
                if dsname in das_info:
                    nfiles = das_info[dsname]["nfiles"]
                else:
                    # split_func's DAS query also failed — fall back to get_files()
                    nfiles = len(ds.get_files())

                print(f"\n  --- {dsname} ---")
                print(f"  [files] {nfiles} input files found")
                if nfiles == 0:
                    track_zero_files(dsname)
                for analysis_tag in analysis_tags:
                    # Skip data PDs not relevant to this channel
                    if metadata["type"] == "Data" and analysis_tag in CHANNEL_PDS:
                        pd_name = get_primary_dataset(dsname)
                        if pd_name not in CHANNEL_PDS[analysis_tag]:
                            continue

                    # Skip MC backgrounds not listed for this channel
                    if metadata["type"] == "Bkg":
                        if not is_mc_allowed(dsname, analysis_tag):
                            continue

                    tag = f"{unique_key}_{analysis_tag}"

                    njobs = math.ceil(nfiles / fpo) if fpo > 0 else nfiles
                    print(f"  [job] tag={analysis_tag}  files_per_job={fpo}  -> {njobs} jobs expected")

                    common_kwargs = dict(
                        verbose=True,
                        sample=ds,
                        files_per_output=fpo,
                        output_name="output.root",
                        tag=tag,
                        max_jobs=njobs_to_process(dsname),
                        cmssw_version=cmssw_version,
                        scram_arch=scram_arch,
                        tarfile=f"{condorpath}/package.tar.xz",
                        # recopy_inputs=True, # Force re-copy tarball to task dirs (comment out when not needed)
                        special_dir=f"skim/{tag}",
                        min_completion_fraction=0.50 if skip_tail else 1.0,
                    )

                    if args.scheduler == "slurm":
                        dsname_flat = ds.get_datasetname().replace("/", "_").lstrip("_")
                        slurm_output_dir = f"/cmsuf/data/store/user/phchang/skim/{tag}/{dsname_flat}/"
                        task = SLURMTask(
                            **common_kwargs,
                            output_dir=slurm_output_dir,
                            basedir="/blue/avery/p.chang",
                            input_executable=f"{condorpath}/slurm_executable.sh",
                            account="avery",
                            qos="avery-b",
                            memory="8gb",
                            cpus_per_task=3,
                            arguments=f"{signal_flags} -d ./ -a {analysis_tag} -t Events -T Events",
                        )
                    else:
                        task = CondorTask(
                            **common_kwargs,
                            input_executable=f"{condorpath}/condor_executable_metis.sh",
                            condor_submit_params=dict({
                                "use_xrootd": True,
                                "sites": "T2_US_UCSD",
                                "classads": [["metis_extraargs", f"{signal_flags} -d ./ -a {analysis_tag} -t Events -T Events"]]
                            }, **({"container": singularity_image} if singularity_image else {})),
                        )

                    # Summary key for this task+tag
                    skey = f"{task.get_sample().get_datasetname()}_{analysis_tag}"

                    is_packed = False
                    if not task.complete():
                        if args.dry_run:
                            print(f"  [dry-run] Would submit: {dsname} | tag={tag} | {njobs} jobs")
                        elif args.pack_size > 1 and args.scheduler == "slurm":
                            # Packed mode: collect task, submit later
                            print(f"  [pending] {dsname} | tag={tag}")
                            packed_tasks.append((task, unique_key, skey))
                            is_packed = True
                        else:
                            # Standard mode: submit immediately
                            if args.scheduler == "slurm":
                                queued = pending_job_count()
                                if queued >= MAX_SUBMITTED:
                                    print(f"  [throttle] {queued} jobs in queue (limit {MAX_SUBMITTED}), skipping {dsname} ({tag})")
                                    all_tasks_complete = False
                                    continue
                            print(f"  [submit] {dsname} | tag={tag}")
                            task.process()
                    else:
                        print(f"  [done] Already complete: {dsname} | tag={tag}")

                    # Packed tasks: skip summary here, captured after submission
                    if is_packed:
                        continue

                    # Aggregate completion
                    all_tasks_complete = all_tasks_complete and task.complete()

                    # Update per-key task summary
                    if unique_key not in task_summaries:
                        task_summaries[unique_key] = {}
                    task_summaries[unique_key][skey] = task.get_task_summary(cached_all_jobs=cached_all_jobs)

            # Track unique_key + tags for dashboard generation
            all_unique_keys_and_tags.append((unique_key, analysis_tags))

        # ------------------------------------------------------------------
        # Packed submission: submit all collected tasks via PackedSLURMSubmitter
        # ------------------------------------------------------------------
        if args.pack_size > 1 and args.scheduler == "slurm" and packed_tasks and not args.dry_run:
            packed_tasks_only = [t for t, _, _ in packed_tasks]
            submitter = PackedSLURMSubmitter(
                pack_size=args.pack_size,
                cpus_per_subjob=args.cpus_per_subjob,
                packed_executable=f"{condorpath}/slurm_packed_executable.sh",
                partition="hpg-default",
                qos="avery-b",
                account="avery",
                time="08:00:00",
                memory=f"{args.pack_size * 2}gb",
            )
            print(f"\n=== Packed submission: {len(packed_tasks)} tasks, pack_size={args.pack_size}, cpus_per_subjob={args.cpus_per_subjob} ===")
            submitter.process(packed_tasks_only)
            # Re-cache squeue after submission (new jobs now in queue)
            cached_all_jobs = slurm_q()
            # Re-check completion and re-capture summaries after submission
            for task, ukey, skey in packed_tasks:
                all_tasks_complete = all_tasks_complete and task.complete()
                if ukey not in task_summaries:
                    task_summaries[ukey] = {}
                task_summaries[ukey][skey] = task.get_task_summary(cached_all_jobs=cached_all_jobs)

        # ------------------------------------------------------------------
        # Generate JSON summaries and dashboards per tag
        # ------------------------------------------------------------------
        for unique_key, analysis_tags in all_unique_keys_and_tags:
            key_summary = task_summaries.get(unique_key, {})

            for analysis_tag in analysis_tags:

                # Filter summary for this tag (scoped to this unique_key)
                tag_summary = {k: v for k, v in key_summary.items() if k.endswith(f"_{analysis_tag}")}

                webdir = os.path.expanduser(f"~/public_html/{unique_key}/{analysis_tag}")
                os.makedirs(webdir, exist_ok=True)
                os.system(f"rm -f {webdir}/web_summary.json")

                StatsParser(data=tag_summary, webdir=webdir, summary_fname=f"{webdir}/summary.json", wsummary_name=f"{webdir}/web_summary.json").do()

                os.system("chmod -R 755 {}".format(webdir))
                os.system(f"msummary -r -i {webdir}/web_summary.json")


        # Report problematic datasets
        if _das_problems:
            print("\n" + "=" * 70)
            print(f"WARNING: {len(_das_problems)} dataset(s) with problems:")
            print("-" * 70)
            for ds, info in sorted(_das_problems.items()):
                print(f"  {info['reason']:<30s}  nevents={info['nevents']}  nfiles={info['nfiles']}")
                print(f"    {ds}")
            print("=" * 70)

        # If all done exit the loop
        if all_tasks_complete:
            print("")
            print("All job finished")
            print("")
            break

        if args.dry_run:
            print("\n[dry-run] Exiting after one pass (no jobs submitted)")
            break

        # Neat trick to not exit the script for force updating
        print('Press Ctrl-C to force update, otherwise will sleep for 600 seconds')
        try:
            for i in reversed(range(0, 600)):
                sleep(1) # could use a backward counter to be preeety :)
                sys.stdout.write("\r{} mins {} seconds till updating ...".format(i//60, i%60))
                sys.stdout.flush()
        except KeyboardInterrupt:
            input("Press Enter to force update, or Ctrl-C to quit.")
            print("Force updating...")
