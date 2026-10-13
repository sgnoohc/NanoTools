#ifndef BASE_H
#define BASE_H

namespace SS {
    enum IDLevel {
        IDdefault = -1,
        IDveto = 0,
        IDfakableNoIso = 1,
        IDfakable = 2, // for fake background + jet cleaning
        IDtightNoIso = 3,
        IDtight = 4 // for analysis
    };
}

namespace ttH {
    enum IDLevel {
        IDveto = 0,
        IDfakable = 1, // for fake background + jet cleaning
        IDtight = 2 // for analysis
    };
}

namespace WWZ {
    enum IDLevel {
        IDveto = 0,
        IDfakable = 1, // for fake background + jet cleaning
        IDtight = 2 // for analysis
    };
}

namespace VVH {
    enum IDLevel {
        IDveto = 0,
        IDfakable = 1,
        IDtight = 2,
        IDskim = 3 // loose WP used by the skimmer for lepton counting (mirrors cmstas/run3-vbsvvh _looseElectrons/_looseMuons)
        ,
        // Deliberately looser WP for the opt-in 4LepLoose channel ("Tier B").
        // Drops ISOLATION and IMPACT-PARAMETER entirely -- the two cuts that bias
        // non-prompt, displaced and boosted-overlap studies -- and lowers pT to
        // the NanoAOD storage floor, keeping only enough quality to reject track
        // junk. Measured on Summer24 v15: >=4 lepton acceptance rises from
        // 0.008% to 3.6% (ttbar) and 0.002% to 0.75% (DY), i.e. 300-440x.
        // NOT a physics-analysis WP: expect large heavy-flavour/fake content.
        IDloose4L = 4
    };
}

#endif
