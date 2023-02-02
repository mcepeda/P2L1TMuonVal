// -*- C++ -*-
//
// Package:    UserCode/L1TriggerDPG
// Class:      L1GMTTkMuonTreeProducer
//
/**\class L1GMTTkMuonTreeProducer L1GMTTkMuonTreeProducer.cc UserCode/L1TriggerDPG/src/L1GMTTkMuonTreeProducer.cc

//This is a tree producer for L1 TDR Step 1 Menu - for the extended version, go for L1PhaseIITreeProducer.cc

Description: Produce L1 Extra tree

Implementation:

*/
//
// Original Author:  Alex Tapper
//         Created:
// $Id: L1PhaseIITreeProducer.cc,v 1.5 2013/01/06 21:55:55 jbrooke Exp $
//
//

// system include files
#include <memory>

// framework
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "DataFormats/L1TMuonPhase2/interface/SAMuon.h"
#include "DataFormats/L1TMuonPhase2/interface/MuonStub.h"
#include "DataFormats/L1TMuonPhase2/interface/TrackerMuon.h"

// ROOT output stuff
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TTree.h"

#include "L1Trigger/Phase2L1GMTNtuples/interface/L1AnalysisGMTTkMuon.h"
#include "L1Trigger/Phase2L1GMTNtuples/interface/L1AnalysisGMTTkMuonDataFormat.h"

#include "DataFormats/L1TMuonPhase2/interface/Constants.h"


//
// class declaration
//
class L1GMTTkMuonTreeProducer : public edm::one::EDAnalyzer<> {
public:
  explicit L1GMTTkMuonTreeProducer(const edm::ParameterSet&);
  ~L1GMTTkMuonTreeProducer() override;

private:
  void beginJob(void) override;
  void analyze(const edm::Event&, const edm::EventSetup&) override;
  void endJob() override;

public:
  L1Analysis::L1AnalysisGMTTkMuon* l1Extra;
  L1Analysis::L1AnalysisGMTTkMuonDataFormat* l1ExtraData;

private:
  unsigned maxL1Extra_;

  // output file
  edm::Service<TFileService> fs_;

  // tree
  TTree* tree_;

  edm::EDGetTokenT<std::vector<l1t::TrackerMuon> > gmtTkMuonToken_;
//  edm::EDGetTokenT<std::vector<l1t::PFCandidate>> l1PFCandidates_;

};

L1GMTTkMuonTreeProducer::L1GMTTkMuonTreeProducer(const edm::ParameterSet& iConfig) {
  gmtTkMuonToken_ = consumes<std::vector<l1t::TrackerMuon> >(iConfig.getParameter<edm::InputTag>("gmtTkMuonToken"));
//  l1PFCandidates_ = consumes<std::vector<l1t::PFCandidate>>(iConfig.getParameter<edm::InputTag>("l1PFCandidates"));
  maxL1Extra_ = iConfig.getParameter<unsigned int>("maxL1Extra");

  l1Extra = new L1Analysis::L1AnalysisGMTTkMuon();
  l1ExtraData = l1Extra->getData();

  // set up output
  tree_ = fs_->make<TTree>("L1PhaseIITree", "L1PhaseIITree");
  tree_->Branch("L1PhaseII", "L1Analysis::L1AnalysisGMTTkMuonDataFormat", &l1ExtraData, 32000, 3);
}

L1GMTTkMuonTreeProducer::~L1GMTTkMuonTreeProducer() {
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)
}

//
// member functions
//

// ------------ method called to for each event  ------------
void L1GMTTkMuonTreeProducer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
  l1Extra->Reset();

  edm::Handle<std::vector<l1t::TrackerMuon> > gmtTkMuon;
  iEvent.getByToken(gmtTkMuonToken_, gmtTkMuon);


//  edm::Handle<std::vector<l1t::PFCandidate>> l1PFCandidates;
//  iEvent.getByToken(l1PFCandidates_, l1PFCandidates);


  if (gmtTkMuon.isValid()) {
      l1Extra->SetGmtTkMuon(gmtTkMuon, maxL1Extra_);
//    l1Extra->SetGmtTkMuon(gmtTkMuon,l1PFCandidates, maxL1Extra_);
  } else {

    edm::LogWarning("MissingProduct") << "L1PhaseII gmtTkMuons not found. Branch will not be filled" << std::endl;

  }



  tree_->Fill();
}

// ------------ method called once each job just before starting event loop  ------------
void L1GMTTkMuonTreeProducer::beginJob(void) {}

// ------------ method called once each job just after ending the event loop  ------------
void L1GMTTkMuonTreeProducer::endJob() {}

//define this as a plug-in
DEFINE_FWK_MODULE(L1GMTTkMuonTreeProducer);
