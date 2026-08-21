from metis.Sample import DirectorySample, DBSSample
from vbsvvh_data import nanoaodv15_run3_data, nanoaodv15_run2_data, nanoaodv15_run3_data_2025
from vbsvvh_mc import nanoaodv15_run2_bkg, nanoaodv15_run2_sig, nanoaodv15_run3_bkg, nanoaodv15_run3_sig
from vbsvvh_mc import nanoaodv15_run2_bkg_dy_htbinned, nanoaodv15_run2_bkg_dy_jetbinned
from vbsvvh_mc import nanoaodv15_run2_bkg_zz4l, nanoaodv15_run3_bkg_ggzz4l
from vbsvvh_mc import nanoaodv15_run3_bkg_zh4l


# Temporary test group: just the new QCD-4Jets HT-100to200 Run3 Summer24 sample
nanoaodv15_run3_bkg_qcd4jets_test = [
    DBSSample(dataset="/QCD-4Jets_Bin-HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
]


# New low-C2V Run3 signal scan points (C2V=0.25 and C2V=0.75, both C3=1.0),
# 4 processes each = 8 samples, filtered out of the full run3_sig grid. Isolated
# group so a dedicated version skims ONLY these 8; fold into v30 via symlink
# afterward (the v32/run3_data_2025 pattern).
nanoaodv15_run3_sig_lowc2v = [
    s for s in nanoaodv15_run3_sig
    if "c2v0p25" in s.get_datasetname() or "c2v0p75" in s.get_datasetname()
]


# ---------------------------------------------------------------------------
# Sample registry: maps CLI-friendly names -> (sample_list, metadata)
# ---------------------------------------------------------------------------
SAMPLE_REGISTRY = {
    "run2_data": {
        "samples": nanoaodv15_run2_data,
        "metadata": {"run": "Run2", "type": "Data", "nano": "v15"},
    },
    "run2_bkg": {
        "samples": nanoaodv15_run2_bkg,
        "metadata": {"run": "Run2", "type": "Bkg", "nano": "v15"},
    },
    "run2_sig": {
        "samples": nanoaodv15_run2_sig,
        "metadata": {"run": "Run2", "type": "Sig", "nano": "v15"},
    },
    "run3_data": {
        "samples": nanoaodv15_run3_data,
        "metadata": {"run": "Run3", "type": "Data", "nano": "v15"},
    },
    "run3_data_2025": {
        "samples": nanoaodv15_run3_data_2025,
        "metadata": {"run": "Run3", "type": "Data", "nano": "v15"},
    },
    "run3_bkg": {
        "samples": nanoaodv15_run3_bkg,
        "metadata": {"run": "Run3", "type": "Bkg", "nano": "v15"},
    },
    "run3_sig": {
        "samples": nanoaodv15_run3_sig,
        "metadata": {"run": "Run3", "type": "Sig", "nano": "v15"},
    },
    "run3_sig_lowc2v": {
        "samples": nanoaodv15_run3_sig_lowc2v,
        "metadata": {"run": "Run3", "type": "Sig", "nano": "v15"},
    },
    "run3_bkg_qcd4jets_test": {
        "samples": nanoaodv15_run3_bkg_qcd4jets_test,
        "metadata": {"run": "Run3", "type": "Bkg", "nano": "v15"},
    },
    # High-stat DY alternatives to the inclusive M-50 in run2_bkg (multi-(b)jet
    # phase space). ALTERNATIVES — stitch / pick one scheme; do NOT submit
    # alongside run2_bkg's inclusive DY without handling double-counting.
    "run2_bkg_dy_ht": {
        "samples": nanoaodv15_run2_bkg_dy_htbinned,
        "metadata": {"run": "Run2", "type": "Bkg", "nano": "v15"},
    },
    "run2_bkg_dy_jet": {
        "samples": nanoaodv15_run2_bkg_dy_jetbinned,
        "metadata": {"run": "Run2", "type": "Bkg", "nano": "v15"},
    },
    # Extra ZZ->4L samples requested for the 4Lep channel study. Isolated groups
    # so a dedicated version skims only these; fold into v30 by symlink after.
    # run2_bkg_zz4l OVERLAPS ZZTo4L_M-1toInf in run2_bkg — pick one downstream.
    "run2_bkg_zz4l": {
        "samples": nanoaodv15_run2_bkg_zz4l,
        "metadata": {"run": "Run2", "type": "Bkg", "nano": "v15"},
    },
    "run3_bkg_ggzz4l": {
        "samples": nanoaodv15_run3_bkg_ggzz4l,
        "metadata": {"run": "Run3", "type": "Bkg", "nano": "v15"},
    },
    # ZH production with H->ZZ->4L. Complementary to v30's ggH GluGluH-Hto2Zto4L
    # (different production mode) -- no double-counting with it.
    "run3_bkg_zh4l": {
        "samples": nanoaodv15_run3_bkg_zh4l,
        "metadata": {"run": "Run3", "type": "Bkg", "nano": "v15"},
    },
}


def get_samples(name):
    """Return (sample_list, metadata_dict) for a registry key."""
    entry = SAMPLE_REGISTRY[name]
    return entry["samples"], entry["metadata"]


def list_groups():
    """Print a table of all available sample groups."""
    print(f"{'Group':<15} {'Run':<6} {'Type':<6} {'Nano':<5} {'# Samples'}")
    print("-" * 50)
    for name, entry in SAMPLE_REGISTRY.items():
        m = entry["metadata"]
        n = len(entry["samples"])
        print(f"{name:<15} {m['run']:<6} {m['type']:<6} {m['nano']:<5} {n}")


# Backward compat: bare import still works (empty by default)
samples_to_submit = []
