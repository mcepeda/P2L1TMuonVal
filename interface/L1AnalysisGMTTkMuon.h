#ifndef __L1Analysis_L1AnalysisGMTTkMuon_H__
#define __L1Analysis_L1AnalysisGMTTkMuon_H__

//-------------------------------------------------------------------------------
// Created 02/03/2010 - A.C. Le Bihan
//
//
// Original code : UserCode/L1TriggerDPG/L1ExtraTreeProducer - Jim Brooke
//-------------------------------------------------------------------------------

#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerReadoutRecord.h"

#include "DataFormats/L1TMuonPhase2/interface/SAMuon.h"
#include "DataFormats/L1TMuonPhase2/interface/MuonStub.h"
#include "DataFormats/L1TMuonPhase2/interface/TrackerMuon.h"

#include "L1Trigger/Phase2L1GMTNtuples/interface/L1AnalysisGMTTkMuonDataFormat.h"
#include "DataFormats/L1TParticleFlow/interface/PFCandidate.h"

namespace L1Analysis {
  class L1AnalysisGMTTkMuon {
  public:
    L1AnalysisGMTTkMuon();
    ~L1AnalysisGMTTkMuon();
    void Reset() { l1extra_.Reset(); }

    void SetGmtTkMuon(const edm::Handle<std::vector<l1t::TrackerMuon>> gmtTkMuon,unsigned maxL1Extra);
//    void SetGmtTkMuon(const edm::Handle<std::vector<l1t::TrackerMuon>> gmtTkMuon, const edm::Handle<vector<l1t::PFCandidate>> l1pfCandidates, unsigned maxL1Extra);

    L1AnalysisGMTTkMuonDataFormat* getData() { return &l1extra_; }

  private:
    L1AnalysisGMTTkMuonDataFormat l1extra_;

  };
}  // namespace L1Analysis
#endif
