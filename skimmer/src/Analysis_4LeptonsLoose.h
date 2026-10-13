#ifndef ANALYSIS_4LEPTONSLOOSE_H
#define ANALYSIS_4LEPTONSLOOSE_H

// RAPIDO
#include "arbusto.h"
#include "cutflow.h"
#include "hepcli.h"
// ROOT
#include "TString.h"
// NanoCORE
#include "Config.h" // gconf
#include "Nano.h"
#include "Tools/goodrun.h"

#include "Analysis.h"
#include "ObjectSelection_Jets.h"
#include "ObjectSelection_Leptons.h"

typedef std::vector<LorentzVector> LorentzVectors;

// 4LepLoose -- deliberately loose >=4 lepton channel ("Tier B").
//
// Counts VVH::IDloose4L leptons instead of IDskim:
//    e : pT > 5,  |eta_SC| < 2.5,  cutBased >= 1 (Veto),  lostHits <= 1
//    mu: pT > 3,  |eta|    < 2.4,  (isGlobal || isTracker),  isPFcand
// NO isolation, NO dxy/dz, NO sip3d -- those are the cuts that bias non-prompt,
// displaced and boosted-overlap studies, so they move downstream.
//
// Measured on Summer24 v15 (2 files/sample): >=4 lepton acceptance goes from
// 0.0081% -> 3.61% on TTto2L2Nu and 0.0024% -> 0.75% on DYto2L, i.e. 300-440x
// more events kept than 4Lep. Projected output over run2_bkg+run3_bkg is
// ~0.8 TB (range 0.3-1.3) against ~0.002 TB for 4Lep.
//
// This is an OPT-IN channel (submit.py EXTRA_CHANNELS): it is NOT part of
// ALL_CHANNELS, so it never runs unless asked for with --channels 4LepLoose.
// Leaving it out of the default keeps every other campaign the size it is now.
//
// 4Lep is untouched and still counts IDskim leptons, so all existing skims keep
// their meaning.
class Analysis_4LeptonsLoose : public Analysis
{
  public:
    Analysis_4LeptonsLoose(Arbusto &arbusto_ref, Nano &nt_ref, HEPCLI &cli_ref, Cutflow &cutflow_ref)
        : Analysis(arbusto_ref, nt_ref, cli_ref, cutflow_ref) {}

    void initBranches() override { Analysis::initBranches(); }

    void initCutflow() override
    {
        Cut *cut_fourleptons_loose = new LambdaCut(
            "FourLeptonsLoose",
            [&]() { return (cutflow.globals.getVal<LorentzVectors>("vvh_loose4l_lep_p4s").size() >= 4); });
        vCutflowCuts_.push_back(cut_fourleptons_loose);

        finalSkimmerCut_ = "FourLeptonsLoose";
        Analysis::initCutflow();
    }
};

#endif
