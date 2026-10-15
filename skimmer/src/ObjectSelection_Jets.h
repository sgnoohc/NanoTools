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

// Reads the extra NanoAODv15 jet-ID inputs through an INDEPENDENT handle on the
// same file, so the tree Arbusto writes from is never touched.
//
// Why this indirection: Arbusto shares buffers between input and output.
// Arbusto::init() does next_ttree->CopyAddresses(ttree), and Arbusto::fill() is
// just orig_ttree->GetEntry(entry) followed by ttree->Fill() -- so whatever
// address an input branch holds at fill() time is what reaches the output file.
//
// Calling SetAddress() on those branches to read them ourselves orphaned the
// output buffers and wrote uninitialised memory: denormal floats and negative
// multiplicities in Jet_chMultiplicity, Jet_neMultiplicity and the seven
// FatJet_* branches of the v42 (2022/2023) skims. Saving and restoring the
// address is not reliable either, because the shared address can still be null
// when we bind, leaving nothing to restore.
//
// A second TFile handle sidesteps the whole problem: separate branch objects,
// separate buffers, zero interaction with the copy path. Entry numbering is
// identical (same tree in the same file), and only these nine small branches
// are enabled, so the extra I/O is negligible.
class JetIdInputReader
{
  public:
    TFile *file_ = nullptr;
    TTree *tree_ = nullptr;

    ~JetIdInputReader() { close(); }

    void close()
    {
        if (file_) { file_->Close(); delete file_; }
        file_ = nullptr;
        tree_ = nullptr;
    }

    // Open our own handle on the file backing `main_tree`. Returns false if
    // unavailable, in which case the caller must not use the buffers.
    bool open(TTree *main_tree)
    {
        close();
        TFile *src = main_tree->GetCurrentFile();
        if (!src) return false;
        // TFile::Open() makes the newly opened file the current directory. The
        // skimmer's output tree lives in the Arbusto output file, so leaving
        // gDirectory pointing here sends its basket writes to a read-only file
        // ("basket's WriteBuffer failed") and the output is lost. Restore it.
        TDirectory *prev = gDirectory;
        file_ = TFile::Open(src->GetName(), "READ");
        if (!file_ || file_->IsZombie()) { close(); if (prev) prev->cd(); return false; }
        tree_ = dynamic_cast<TTree *>(file_->Get(main_tree->GetName()));
        if (!tree_) { close(); if (prev) prev->cd(); return false; }
        tree_->SetBranchStatus("*", 0);
        if (prev) prev->cd();
        return true;
    }

    // Enable one branch and point it at our own buffer.
    bool bind(const char *name, void *buf)
    {
        if (!tree_ || !tree_->GetBranch(name)) return false;
        tree_->SetBranchStatus(name, 1);
        tree_->SetBranchAddress(name, buf);
        return true;
    }

    void loadEntry(int entry) { if (tree_) tree_->GetEntry(entry); }
};

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

    // Independent reader for the jet-ID input branches (never touches Arbusto's tree)
    JetIdInputReader jetIdInputs_;

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

        // Open our own handle on this file and bind the extra jet-ID inputs there,
        // so Arbusto's copy of these branches is left completely untouched.
        bool reader_ok = jetIdInputs_.open(tree);

        hasJetMultBranches_ = reader_ok
            && jetIdInputs_.bind("Jet_chMultiplicity", Jet_chMultiplicity_)
            && jetIdInputs_.bind("Jet_neMultiplicity", Jet_neMultiplicity_);

        hasFatJetIdBranches_ = reader_ok
            && jetIdInputs_.bind("FatJet_chHEF",          FatJet_chHEF_)
            && jetIdInputs_.bind("FatJet_neHEF",          FatJet_neHEF_)
            && jetIdInputs_.bind("FatJet_chEmEF",         FatJet_chEmEF_)
            && jetIdInputs_.bind("FatJet_neEmEF",         FatJet_neEmEF_)
            && jetIdInputs_.bind("FatJet_muEF",           FatJet_muEF_)
            && jetIdInputs_.bind("FatJet_chMultiplicity", FatJet_chMultiplicity_)
            && jetIdInputs_.bind("FatJet_neMultiplicity", FatJet_neMultiplicity_);

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
        jetIdInputs_.loadEntry(entry);
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
