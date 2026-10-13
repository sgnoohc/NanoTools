#!/usr/bin/env python3
"""
Measure >=4 lepton pass rates for candidate loose-lepton working points.

Applies the WPs directly to NanoAOD with RDataFrame rather than going through
the skim binary, so tiers can be compared before any channel is implemented.

Tiers (see the plan):
  CURRENT  VVH::IDskim, i.e. what 4Lep counts today
  A        acceptance only -- no ID, no isolation, no impact parameter
  B        minimal quality, no isolation, no IP
  C        current shape, dialled down

Output size is estimated as  input_size x (events_passing / events_total),
which is the right scaling because the skim keeps whole events with the full
branch content; it does not prune collections.

Usage:
  python3 measure_4lep_tiers.py <file.root> [more.root ...] [--label NAME]
"""
import argparse
import os
import sys

import ROOT

ROOT.gROOT.SetBatch(True)
ROOT.gErrorIgnoreLevel = ROOT.kError

# --- electron selections -----------------------------------------------------
E_CURRENT = """
   Electron_pt > 10 && abs(Electron_eta + Electron_deltaEtaSC) < 2.5
&& Electron_cutBased >= 2
&& ( (abs(Electron_eta + Electron_deltaEtaSC) <= 1.479
        && abs(Electron_dxy) <= 0.05 && abs(Electron_dz) < 0.1)
   || (abs(Electron_eta + Electron_deltaEtaSC) >  1.479
        && abs(Electron_dxy) <= 0.10 && abs(Electron_dz) < 0.2) )
"""
E_A = "Electron_pt > 5 && abs(Electron_eta + Electron_deltaEtaSC) < 2.5"
E_B = E_A + " && Electron_cutBased >= 1 && Electron_lostHits <= 1"
E_C = """
   Electron_pt > 7 && abs(Electron_eta + Electron_deltaEtaSC) < 2.5
&& Electron_cutBased >= 1
&& ( (abs(Electron_eta + Electron_deltaEtaSC) <= 1.479
        && abs(Electron_dxy) <= 0.05 && abs(Electron_dz) < 0.1)
   || (abs(Electron_eta + Electron_deltaEtaSC) >  1.479
        && abs(Electron_dxy) <= 0.10 && abs(Electron_dz) < 0.2) )
"""

# --- muon selections ---------------------------------------------------------
M_CURRENT = """
   Muon_pt > 10 && abs(Muon_eta) < 2.4 && Muon_looseId
&& Muon_pfIsoId >= 2 && abs(Muon_sip3d) < 8
&& abs(Muon_dxy) < 0.2 && abs(Muon_dz) < 0.5
"""
M_A = "Muon_pt > 3 && abs(Muon_eta) < 2.4"
M_B = M_A + " && (Muon_isGlobal || Muon_isTracker) && Muon_isPFcand"
M_C = "Muon_pt > 5 && abs(Muon_eta) < 2.4 && Muon_looseId && abs(Muon_sip3d) < 15"

TIERS = [("CURRENT", E_CURRENT, M_CURRENT),
         ("A",       E_A,       M_A),
         ("B",       E_B,       M_B),
         ("C",       E_C,       M_C)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--label", default=None)
    args = ap.parse_args()

    files = [f for f in args.files if os.path.isfile(f)]
    if not files:
        sys.exit("no readable input files")
    size = sum(os.path.getsize(f) for f in files)

    df = ROOT.RDataFrame("Events", files)
    total = df.Count()

    counts, nlep_means = {}, {}
    for name, esel, msel in TIERS:
        d = (df.Define(f"ne_{name}", f"Sum({esel})")
               .Define(f"nm_{name}", f"Sum({msel})")
               .Define(f"nl_{name}", f"ne_{name} + nm_{name}"))
        counts[name] = d.Filter(f"nl_{name} >= 4").Count()
        nlep_means[name] = d.Mean(f"nl_{name}")

    n_total = total.GetValue()
    label = args.label or os.path.basename(files[0])[:28]
    print(f"\n### {label}")
    print(f"  files={len(files)}  events={n_total:,}  input={size/1e9:.2f} GB")
    print(f"  {'tier':8s} {'<n lep>':>8s} {'pass >=4L':>11s} {'rate':>9s} "
          f"{'x CURRENT':>10s} {'est. out':>10s}")
    base = None
    for name, _, _ in TIERS:
        c = counts[name].GetValue()
        rate = c / n_total if n_total else 0.0
        if name == "CURRENT":
            base = c
        ratio = (c / base) if base else float("nan")
        est = size * rate
        print(f"  {name:8s} {nlep_means[name].GetValue():8.3f} {c:11,} "
              f"{rate:9.5%} {ratio:9.1f}x {est/1e6:9.1f} MB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
