#!/usr/bin/env python
from ROOT import *
import math 

#filename="MinBias_muontree"
#filename="Merged_MinBias_GMTRev_2"
filename="Merged_DoubleMu_GMTRev_2"
#filename="DoubleMuGun_muontree"

#filename="Merged_DoubleMu_GMTRev_2"

f = TFile( '/scratch/cepeda/trigger/'+filename+'.root')
tree = f.Get("l1PhaseIITree/L1PhaseIITree")

#tree = f.Get("gmtTkMuonChecksTree/L1PhaseIITree")

totalcount=1.#31038.0 # 2760.0*11246/1000

entries=  tree.GetEntriesFast()

print (entries)

TH1.GetDefaultSumw2()

branch="gmtTkMuon"
etaMin=0
etaMax=2.5

eventNo=0

def formatHisto(name,title,bins=50,start=0,end=100, color=kBlack):
        histo = TH1F(name,title,bins,start,end)
        histo.SetLineColor(color)
        histo.SetMarkerColor(color)
        histo.SetMarkerStyle(20)
        histo.Sumw2()
        return histo

step=(100.-0)/50

countGMTTkMuonBarrel=formatHisto("countGMTTkMuonBarrel","Rate GMTTkMuon Barrel")
countTkGlbMuonBarrel=formatHisto("countTkGlbBarrel","Rate TkGlb Barrel")

countGMTTkMuonEndcap=formatHisto("countGMTTkMuonEndcap","Rate GMTTkMuon Endcap")
countTkGlbMuonEndcap=formatHisto("countTkGlbEndcap","Rate TkGlb Endcap")

countGMTTkMuonOverlap=formatHisto("countGMTTkMuonOverlap","Rate GMTTkMuon Overlap")
countTkGlbMuonOverlap=formatHisto("countTkGlbOverlap","Rate TkGlb Overlap")


# gmtTkMuonIdLUTEta = (vector<unsigned int>*)0x3379c80
# gmtTkMuonIdLUTPt = (vector<unsigned int>*)0x3379c98
# gmtTkMuonIdLUTQuality = (vector<unsigned int>*)0x3379cb0

for event in tree: 

	vectorGMTTkPt=getattr(event, "gmtTkMuonPt")
        vectorTkGlbPt=getattr(event, "tkGlbMuonPt")
        vectorGMTTkEta=getattr(event, "gmtTkMuonEta")
        vectorTkGlbEta=getattr(event, "tkGlbMuonEta")


	# GMT Muons
	for i in range(vectorGMTTkPt.size()):
		if abs(vectorGMTTkEta[i])<0.83:
        		countGMTTkMuonBarrel.Fill(vectorGMTTkPt[i])
		elif abs(vectorGMTTkEta[i])<1.24:
                        countGMTTkMuonOverlap.Fill(vectorGMTTkPt[i])
		else:
			countGMTTkMuonEndcap.Fill(vectorGMTTkPt[i])

        # GMT Muons
        for i in range(vectorTkGlbPt.size()):
                if abs(vectorTkGlbEta[i])<0.83:
                        countTkGlbMuonBarrel.Fill(vectorTkGlbPt[i])
                elif abs(vectorTkGlbEta[i])<1.24:
                        countTkGlbMuonOverlap.Fill(vectorTkGlbPt[i])
                else:
                        countTkGlbMuonEndcap.Fill(vectorTkGlbPt[i])



out=TFile("count_"+filename+".root","RECREATE")
out.cd()

countTkGlbMuonBarrel.Write()
countTkGlbMuonOverlap.Write()
countTkGlbMuonEndcap.Write()

countGMTTkMuonBarrel.Write()
countGMTTkMuonOverlap.Write()
countGMTTkMuonEndcap.Write()



