from metis.Sample import DirectorySample, DBSSample
from vbsvvh_data import nanoaodv15_run3_data, nanoaodv15_run2_data
from vbsvvh_mc import nanoaodv15_run2_bkg, nanoaodv15_run2_sig, nanoaodv15_run3_bkg


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
    "run3_bkg": {
        "samples": nanoaodv15_run3_bkg,
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
