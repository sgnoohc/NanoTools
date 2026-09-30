"""
LPC PFNano (DAZSLE) NanoAODv14 samples, driven by nanoindex_v14_HVV_private.json.

Unlike every other sample module here, these are NOT DAS datasets: the index is a
year -> category -> sample -> [explicit xrootd URL] map produced by
make_filelists.py, pointing at root://cmseos.fnal.gov/. They are therefore built
as metis FilelistSample rather than DBSSample/DirectorySample.

Reading them requires the year-parsing and JetId era fixes in 458911d -- these
paths carry no campaign string for signal, use Run3Summer23 for 2023 MC, and name
files "MC_preEE2022_*.root" (which naively substring-matches "EE").

DATASET NAMING. metis names become output directory names, and submit.py derives
the primary dataset for Data channel routing with
get_primary_dataset() == name.strip("/").split("/")[0]. So Data MUST be named
"/<PD>/..." for PD routing to work at all; a bare "Muon_Run2022E" would yield a
"PD" of that whole string and match nothing. Era goes in the second field.
"""

import json
import os

from metis.Sample import FilelistSample

_HERE = os.path.dirname(os.path.realpath(__file__))
INDEX_PATH = os.path.join(_HERE, "..", "..", "nanoindex_v14_HVV_private.json")

# Categories that are Data, keyed by the primary dataset they correspond to.
DATA_CATEGORIES = {"JetMET", "EGamma", "Muon", "Tau", "BTagMu"}
# The VBS VVH signal scan lives here.
SIGNAL_CATEGORIES = {"HVV_Signal"}
# Everything else in the index is MC background.

ERAS = ["2022", "2022EE", "2023", "2023BPix"]

STAGE_ROOT = "/cmsuf/data/store/user/phchang/v14stage"

_index_cache = None
_staged_cache = None


def _is_staged(era, kind):
    """True if (era, kind) is fully staged on /cmsuf, per marker file.

    Markers are per (era, KIND), not per era. Staging is driven by
    make_v14_stage_list.py, which selects categories -- the first pass staged
    background MC only. A per-era marker would have claimed the era's DATA was
    staged too, and since _local_or_remote() trusts the marker without stat'ing
    each file, every data job would have been handed a /cmsuf path that does not
    exist. The executable skips xrdcp for /cmsuf inputs, so those jobs fail with
    no fallback. Keep marker granularity matched to staging granularity.

    The verifier writes a marker only after confirming every manifest entry for
    that (era, kind) landed non-empty.
    """
    global _staged_cache
    if _staged_cache is None:
        _staged_cache = set()
        for e in ERAS:
            for k in ("bkg", "data", "sig"):
                if os.path.isfile(os.path.join(STAGE_ROOT, f".staged_{e}_{k}")):
                    _staged_cache.add((e, k))
    return (era, kind) in _staged_cache


def _local_or_remote(url, era, kind):
    """Map an index URL to its staged /cmsuf path when that era is staged.

    This is the whole point of staging: slurm_packed_executable.sh skips xrdcp
    entirely for inputs under /cmsuf, so jobs read the one shared copy instead
    of each re-downloading to node-local /tmp. Falls back to the original URL
    if the era is unstaged or the individual file is somehow absent.
    """
    if not _is_staged(era, kind):
        return url
    i = url.find("/store/")
    if i < 0:
        return url
    # No per-file existence check here on purpose. The .staged_<era> marker is
    # written only after the verifier confirms every manifest entry landed
    # non-empty, so the mapping is already known-good -- and stat'ing 180k files
    # on Lustre at import time cost minutes on every submit.py invocation.
    # Set V14_VERIFY_STAGED=1 to re-check per file (slow).
    dest = os.path.join(STAGE_ROOT, url[i + len("/store/"):])
    if os.environ.get("V14_VERIFY_STAGED") and not os.path.isfile(dest):
        return url
    return dest


def _load_index():
    global _index_cache
    if _index_cache is None:
        with open(os.path.abspath(INDEX_PATH)) as f:
            _index_cache = json.load(f)
    return _index_cache


def dataset_name(era, category, sname):
    """Build a DAS-like name. Kept in one place because the nevents cache is
    keyed by exactly these strings -- if this changes, regenerate v14_nevents.py."""
    if category in DATA_CATEGORIES:
        # "/<PD>/<era>_<leaf>/PFNANOV14" -- PD first so get_primary_dataset works.
        leaf = sname[len(category) + 1:] if sname.startswith(category + "_") else sname
        return f"/{category}/{era}_{leaf}/PFNANOV14"
    kind = "PFNANOSIG" if category in SIGNAL_CATEGORIES else "PFNANOSIM"
    return f"/{sname}/{era}_PFNanoV14/{kind}"


def _samples_for(era, kind):
    """kind: 'Data' | 'Sig' | 'Bkg'"""
    idx = _load_index()
    out = []
    for category, cd in sorted(idx.get(era, {}).items()):
        if kind == "Data" and category not in DATA_CATEGORIES:
            continue
        if kind == "Sig" and category not in SIGNAL_CATEGORIES:
            continue
        if kind == "Bkg" and (category in DATA_CATEGORIES or category in SIGNAL_CATEGORIES):
            continue
        for sname, files in sorted(cd.items()):
            if not files:
                continue
            # Probe ONE file per sample rather than trusting the marker blindly or
            # stat'ing all 181k. A marker covers an (era, kind), but staging can
            # legitimately skip a whole category inside it -- the data pass omits
            # Tau/BTagMu because they route to no channel. Without this probe those
            # samples get /cmsuf paths that do not exist, and since the executable
            # skips xrdcp for /cmsuf inputs they fail with no fallback. Staging is
            # all-or-nothing per sample, so one probe settles the whole file list.
            mapped = [_local_or_remote(u, era, kind.lower()) for u in files]
            if mapped[0].startswith(STAGE_ROOT) and not os.path.isfile(mapped[0]):
                mapped = list(files)
            out.append(FilelistSample(
                dataset=dataset_name(era, category, sname),
                filelist=mapped,
                # Entries are either fully-qualified root:// URLs or absolute
                # /cmsuf paths -- no path rewriting wanted either way.
                use_xrootd=False,
            ))
    return out


def get_groups():
    """Return {registry_name: (samples, metadata)} for all era x type combinations."""
    groups = {}
    for era in ERAS:
        for kind in ("Bkg", "Data", "Sig"):
            samples = _samples_for(era, kind)
            if not samples:
                continue
            # Era is folded into 'run' so make_unique_key() yields a distinct tag
            # per era: Run3_2022EE_Bkg_v14_<version>_<channel>.
            groups[f"v14_{era}_{kind.lower()}"] = (
                samples,
                {"run": f"Run3_{era}", "type": kind, "nano": "v14"},
            )
    return groups


def summarize():
    """Print an era x type table of sample and file counts."""
    idx = _load_index()
    print(f"{'group':24s} {'samples':>8s} {'files':>9s}")
    tot_s = tot_f = 0
    for name, (samples, md) in sorted(get_groups().items()):
        nf = sum(len(s.get_files()) for s in samples)
        print(f"{name:24s} {len(samples):8d} {nf:9d}")
        tot_s += len(samples); tot_f += nf
    print(f"{'TOTAL':24s} {tot_s:8d} {tot_f:9d}")


if __name__ == "__main__":
    summarize()
