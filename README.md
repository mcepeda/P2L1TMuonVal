# P2L1TMuonVal

This repository will contain an example tree and python analysis code to perform P2 L1TMuon checks for gmtMuons (with and without tracks) 

Existing ntuples (in 12_3 and using the extended branches for ID tuning): /eos/user/c/cepeda/trigger/ (DoubleMuGun for signal and MinBias for backgound)


## For 12_5_X samples

```
cmsrel CMSSW_12_5_2_patch1
cd CMSSW_12_5_2_patch1/src
cmsenv
git cms-init

git cms-merge-topic -u cms-l1t-offline:l1t-phase2-v3.4.53

cd L1Trigger
git clone https://github.com/mcepeda/P2L1TMuonVal Phase2L1GMTNtuples  

scram b -j 8
```

The tag for the l1toffline code is taken from [the SWGuideL1TPhase2Instructions twiki](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideL1TPhase2Instructions#CMSSW_12_5_2_patch1) : it might need to be synched again in the future.


To run (using as input one of the new production samples in 12_5, DYToLL_M10To50, as an example):
```
cmsRun test/myconfig125OnlyRead.py
```


