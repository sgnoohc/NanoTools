#!/usr/bin/env python3
"""
Pre-launch gate: assert every v14 sample that will produce jobs reads a staged file.

slurm_packed_executable.sh skips xrdcp entirely for inputs under /cmsuf, so a
path that is "local" but absent is handed straight to skim with no fallback and
the job dies. Staging is driven by manifests that intentionally cover a subset
(background first, then data, and never Tau/BTagMu which route to no channel),
so the mapping in vbsvvh_v14 has to be checked against reality before a launch,
not after.

The invariant is NOT "everything is local" -- samples that route to zero
channels are deliberately unstaged and correctly stay on xrootd. It is:

    every sample that will actually produce jobs resolves to a /cmsuf path
    that exists on disk.

Exit 0 if that holds, 1 otherwise.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

import samples
import sample_channels as sc

LEPTON_PDS = {"MuonEG", "DoubleEG", "DoubleMuon", "SingleMuon", "EGamma",
              "SingleElectron", "Muon", "Muon0", "Muon1",
              "EGamma0", "EGamma1", "EGamma2", "EGamma3"}
HADRONIC_PDS = {"MET", "JetHT", "JetMET", "JetMET0", "JetMET1", "SingleMuon"}
LEP_CH = ["4Lep", "3Lep", "2Lep2FJ", "2Lep1FJ", "2Lep4J", "1Lep1FJ"]
HAD_CH = ["0Lep3FJ", "0Lep2FJ", "0Lep1FJ", "0Lep0FJ"]
ERAS = ["2022", "2022EE", "2023", "2023BPix"]


def n_channels(dsname, kind):
    """How many channels this sample will be submitted to (0 => no jobs)."""
    if kind == "data":
        pd = dsname.strip("/").split("/")[0]
        if pd in LEPTON_PDS:
            return len(LEP_CH)
        if pd in HADRONIC_PDS:
            return len(HAD_CH)
        return 0                       # Tau / BTagMu -- submit.py UNUSED_PDS
    if kind == "sig":
        return 1
    return sum(1 for c in sc.CHANNELS[:9] if sc.is_mc_allowed(dsname, c))


def main():
    kinds = sys.argv[1:] or ["bkg", "data"]
    bad, checked, skipped = [], 0, 0
    for era in ERAS:
        for kind in kinds:
            try:
                ds, _ = samples.get_samples(f"v14_{era}_{kind}")
            except KeyError:
                continue
            for d in ds:
                name = d.get_datasetname()
                if n_channels(name, kind) == 0:
                    skipped += 1
                    continue
                files = d.get_files()
                if not files:
                    bad.append((era, kind, name[:50], "NO FILES"))
                    continue
                f = files[0]
                p = str(f.get_name() if hasattr(f, "get_name") else f)
                checked += 1
                if not p.startswith("/cmsuf/"):
                    bad.append((era, kind, name[:50], "not staged (remote)"))
                elif not os.path.isfile(p):
                    bad.append((era, kind, name[:50], "local path MISSING"))

    print(f"  job-producing samples checked : {checked}")
    print(f"  skipped (route to 0 channels) : {skipped}")
    print(f"  BAD                           : {len(bad)}")
    for era, kind, name, why in bad[:10]:
        print(f"    {era:9s} {kind:4s} {why:20s} {name}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
