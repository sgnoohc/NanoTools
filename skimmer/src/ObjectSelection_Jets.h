#ifndef OBJECTSELECTION_JETS_H
#define OBJECTSELECTION_JETS_H

// NanoTools
#include "Base.h"
#include "Config.h"
#include "Config.h" // gconf
#include "ElectronSelections.h"
#include "MuonSelections.h"
#include "Nano.h"

#include "arbol.h"
#include "arbusto.h"
#include "cutflow.h"
#include "hepcli.h"
#include <cmath>
// Custom skimmer
#include "JetId.h"
#include "ObjectSelection_Base.h"
#include "utilities.h" // Utilities::Variables
// ROOT
#include "TBranch.h"
#include "TString.h"
#include "TTree.h"

typedef std::vector<LorentzVector> LorentzVectors;
typedef std::vector<double> Doubles;
typedef std::vector<int> Integers;
typedef std::vector<unsigned int> Indices;

// Max array sizes (must match NanoCORE Nano.h)
#define JETID_NJET_MAX 250
#define JETID_NFATJET_MAX 40

// The extra NanoAODv15 jet-ID inputs (Jet_chMultiplicity, Jet_neMultiplicity and
// the seven FatJet_* fractions/multiplicities) are not in NanoCORE, so the
// skimmer reads them itself. Doing that naively corrupts the output.
//
// Arbusto shares buffers between input and output: init() calls
// next_ttree->CopyAddresses(ttree), and fill() is orig_ttree->GetEntry(entry)
// followed by ttree->Fill(). Whatever address an input branch holds at fill()
// time is what reaches the file. Pointing the INPUT branch at a private array
// therefore orphans the OUTPUT buffer, which then writes uninitialised memory --
// the denormal floats and negative multiplicities seen in the v42 skims.
//
// Two approaches were tried and rejected. Saving and restoring the address
// around each read is unreliable: the shared address can still be null when we
// bind, so there is nothing to restore. Opening a second TFile on the same file
// is worse: open()/close() run once per tree, and on a 77-file job it segfaulted
// after 55 trees.
//
// What works is to bind ONE buffer to BOTH branches. The input branch fills it
// on GetEntry, the output branch writes from it on Fill, and the two cannot
// disagree because there is only one buffer.
static inline void bindJetIdBranch(TTree *in_tree, TTree *out_tree,
                                   const char *name, void *buf, TBranch **out_br)
{
    *out_br = in_tree ? in_tree->GetBranch(name) : nullptr;
    if (!*out_br) return;
    (*out_br)->SetAddress(buf);
    if (out_tree)
    {
        TBranch *ob = out_tree->GetBranch(name);
        if (ob) ob->SetAddress(buf);   // same buffer -> output cannot be orphaned
    }
}

class JetSelection : public ObjectSelection
{
  public:
    // JetId evaluator (correctionlib-based)
    std::unique_ptr<JetIdEvaluator> jetIdEval_;

    // TBranch pointers and arrays for NanoAODv15 variables not in NanoCORE
    // AK4 jets: multiplicity variables (UChar_t in NanoAODv15)
    TBranch *b_Jet_chMultiplicity_ = nullptr;
    TBranch *b_Jet_neMultiplicity_ = nullptr;
    UChar_t Jet_chMultiplicity_[JETID_NJET_MAX];
    UChar_t Jet_neMultiplicity_[JETID_NJET_MAX];

    // AK8 fat jets: energy fraction and multiplicity variables
    TBranch *b_FatJet_chHEF_ = nullptr;
    TBranch *b_FatJet_neHEF_ = nullptr;
    TBranch *b_FatJet_chEmEF_ = nullptr;
    TBranch *b_FatJet_neEmEF_ = nullptr;
    TBranch *b_FatJet_muEF_ = nullptr;
    TBranch *b_FatJet_chMultiplicity_ = nullptr;
    TBranch *b_FatJet_neMultiplicity_ = nullptr;
    float FatJet_chHEF_[JETID_NFATJET_MAX];
    float FatJet_neHEF_[JETID_NFATJET_MAX];
    float FatJet_chEmEF_[JETID_NFATJET_MAX];
    float FatJet_neEmEF_[JETID_NFATJET_MAX];
    float FatJet_muEF_[JETID_NFATJET_MAX];
    Short_t FatJet_chMultiplicity_[JETID_NFATJET_MAX];
    Short_t FatJet_neMultiplicity_[JETID_NFATJET_MAX];

    // Input branches we read ourselves for jet-ID recomputation
    std::vector<TBranch *> jetIdBranches_;

    bool hasJetMultBranches_ = false;
    bool hasFatJetIdBranches_ = false;
    bool jetIdBranchesCreated_ = false;

    JetSelection(Arbusto &arbusto_ref, Nano &nt_ref, HEPCLI &cli_ref, Utilities::Variables &cutflow_globals_ref) : ObjectSelection(arbusto_ref, nt_ref, cli_ref, cutflow_globals_ref)
    {
    };

    // DeltaR calculation
    float deltaR(const LorentzVector &v1, const LorentzVector &v2)
    {
        float dEta = v1.eta() - v2.eta();
        float dPhi = v1.phi() - v2.phi();
        if (dPhi > M_PI) dPhi -= 2 * M_PI;
        if (dPhi < -M_PI) dPhi += 2 * M_PI;
        return std::sqrt(dEta * dEta + dPhi * dPhi);
    }

    // Veto Jets that overlap with a veto lepton
    bool passLeptonDRCut(const LorentzVector &jet, const LorentzVectors &leptons, double minDr = 0.4)
    {
        for (const auto &lep : leptons)
        {
            if (deltaR(jet, lep) <= minDr) return false;
        }
        return true;
    }

    // Initialize TTree branch addresses for NanoAODv15 variables not in NanoCORE
    void initTree(TTree *tree)
    {
        // Initialize correctionlib jet ID evaluator using year-aware JSON path
        std::string dsname = cli.input_tchain->GetCurrentFile()->GetName();
        std::string jsonPath = JetIdEvaluator::getJsonPath(gconf.year, dsname);
        if (jsonPath.empty() && gconf.year >= 2016 && gconf.year <= 2018)
        {
            std::cout << ">>> JetId: Using manual cut-based PUPPI jet ID for Run2 year " << gconf.year << std::endl;
        }
        else if (jsonPath.empty())
        {
            std::cout << ">>> WARNING: No jetid JSON available for year " << gconf.year << "; Jet_jetId/FatJet_jetId will not be computed." << std::endl;
        }
        else
        {
            std::cout << ">>> JetId JSON: " << jsonPath << std::endl;
        }
        jetIdEval_ = std::make_unique<JetIdEvaluator>(jsonPath, gconf.year);

        // Bind each extra input to a buffer shared with the matching OUTPUT branch,
        // so Arbusto's copy and our read can never diverge (see note above).
        jetIdBranches_.clear();
        TTree *out = arbusto.ttree;
        auto bind = [&](const char *name, void *buf) -> TBranch *
        {
            TBranch *b = nullptr;
            bindJetIdBranch(tree, out, name, buf, &b);
            if (b) jetIdBranches_.push_back(b);
            return b;
        };

        b_Jet_chMultiplicity_ = bind("Jet_chMultiplicity", Jet_chMultiplicity_);
        b_Jet_neMultiplicity_ = bind("Jet_neMultiplicity", Jet_neMultiplicity_);
        hasJetMultBranches_ = (b_Jet_chMultiplicity_ && b_Jet_neMultiplicity_);

        b_FatJet_chHEF_          = bind("FatJet_chHEF",          FatJet_chHEF_);
        b_FatJet_neHEF_          = bind("FatJet_neHEF",          FatJet_neHEF_);
        b_FatJet_chEmEF_         = bind("FatJet_chEmEF",         FatJet_chEmEF_);
        b_FatJet_neEmEF_         = bind("FatJet_neEmEF",         FatJet_neEmEF_);
        b_FatJet_muEF_           = bind("FatJet_muEF",           FatJet_muEF_);
        b_FatJet_chMultiplicity_ = bind("FatJet_chMultiplicity", FatJet_chMultiplicity_);
        b_FatJet_neMultiplicity_ = bind("FatJet_neMultiplicity", FatJet_neMultiplicity_);
        hasFatJetIdBranches_ = (b_FatJet_chHEF_ && b_FatJet_neHEF_ && b_FatJet_chEmEF_
                                && b_FatJet_neEmEF_ && b_FatJet_muEF_
                                && b_FatJet_chMultiplicity_ && b_FatJet_neMultiplicity_);

        // Only create Jet_jetId/FatJet_jetId output branches if the input has the needed v15 branches
        if (!jetIdBranchesCreated_ && (hasJetMultBranches_ || hasFatJetIdBranches_))
        {
            if (hasJetMultBranches_)
            {
                arbusto.newVecBranch<float>("Jet_jetId");
            }
            if (hasFatJetIdBranches_)
            {
                arbusto.newVecBranch<float>("FatJet_jetId");
            }
            jetIdBranchesCreated_ = true;
        }
    }

    // Load the extra NanoAODv15 branches for the current entry
    void loadEntry(int entry)
    {
        for (TBranch *b : jetIdBranches_) b->GetEntry(entry);
    }

    // Compute Jet_jetId and FatJet_jetId using correctionlib and store in output branches
    void computeJetIds()
    {
        if (!jetIdEval_ || !jetIdEval_->isInitialized()) return;

        // Compute AK4 Jet_jetId
        if (hasJetMultBranches_)
        {
            std::vector<float> jetIds;
            unsigned int nJets = std::min(static_cast<unsigned int>(nt.nJet()), static_cast<unsigned int>(nt.Jet_eta().size()));
            for (unsigned int i = 0; i < nJets; i++)
            {
                int chMult = static_cast<int>(Jet_chMultiplicity_[i]);
                int neMult = static_cast<int>(Jet_neMultiplicity_[i]);
                int mult = chMult + neMult;
                float id = jetIdEval_->evalJetId(nt.Jet_eta().at(i), nt.Jet_chHEF().at(i), nt.Jet_neHEF().at(i), nt.Jet_chEmEF().at(i), nt.Jet_neEmEF().at(i), nt.Jet_muEF().at(i), chMult, neMult, mult);
                jetIds.push_back(id);
            }
            arbusto.setVecLeaf<float>("Jet_jetId", jetIds);
        }

        // Compute AK8 FatJet_jetId
        if (hasFatJetIdBranches_)
        {
            std::vector<float> fatJetIds;
            unsigned int nFatJets = std::min(static_cast<unsigned int>(nt.nFatJet()), static_cast<unsigned int>(nt.FatJet_eta().size()));
            for (unsigned int i = 0; i < nFatJets; i++)
            {
                int chMult = static_cast<int>(FatJet_chMultiplicity_[i]);
                int neMult = static_cast<int>(FatJet_neMultiplicity_[i]);
                int mult = chMult + neMult;
                float id = jetIdEval_->evalFatJetId(nt.FatJet_eta().at(i), FatJet_chHEF_[i], FatJet_neHEF_[i], FatJet_chEmEF_[i], FatJet_neEmEF_[i], FatJet_muEF_[i], chMult, neMult, mult);
                fatJetIds.push_back(id);
            }
            arbusto.setVecLeaf<float>("FatJet_jetId", fatJetIds);
        }
    }

    void selectVVHJets()
    {
        selectVVHAK4Jets();
        selectVVHAK8Jets();
    }

    void selectVVHAK4Jets()
    {
        LorentzVectors jet_p4s = {};
        LorentzVectors vvh_veto_lep_p4s = globals.getVal<LorentzVectors>("vvh_veto_lep_p4s");
        for (unsigned int jet_i = 0; jet_i < nt.nJet(); jet_i++)
        {
            LorentzVector jet_p4 = nt.Jet_p4().at(jet_i);
            if (jet_p4.pt() > 15) //&& passLeptonDRCut(jet_p4, vvh_veto_lep_p4s))
            {
                jet_p4s.push_back(jet_p4);
            }
        }
        globals.setVal<LorentzVectors>("vvh_veto_jet_p4s", jet_p4s);
        globals.setVal<int>("n_vvh_veto_jets", jet_p4s.size());
    }

    void selectVVHAK8Jets()
    {
        LorentzVectors fatjet_p4s = {};
        for (unsigned int fatjet_i = 0; fatjet_i < nt.nFatJet(); fatjet_i++)
        {
            LorentzVector fatjet_p4 = nt.FatJet_p4().at(fatjet_i);
            if (fatjet_p4.pt() > 200 && nt.FatJet_msoftdrop().at(fatjet_i) > 20)
            {
                fatjet_p4s.push_back(fatjet_p4);
            }
        }
        globals.setVal<LorentzVectors>("vvh_veto_fatjet_p4s", fatjet_p4s);
        globals.setVal<int>("n_vvh_veto_fatjets", fatjet_p4s.size());
    }
};
#endif
