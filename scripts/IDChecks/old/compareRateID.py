#!/usr/bin/env python 
from ROOT import *

import tdrstyle

#set the tdr style
tdrstyle.setTDRStyle()

fRef = TFile( 'rate_MB_GMTIso_ID_NSTUBS.root')
fNS3= TFile( 'rate_MB_GMTIso_ID_NSTUBS3.root')        
fTRel = TFile( 'rate_MB_GMTIso_ID_NSTUBS_QUAL98.root')        
fMRel = TFile( 'rate_MB_GMTIso_ID_NSTUBS_QUAL64.root')        

def plotHistos(name,xtitle):
	c=TCanvas("c"+name)
        c.SetLogy()
        c.SetGrid()

        histoRef=fRef.Get(name)
        histoRef.SetLineColor(kBlack)
        histoRef.SetMarkerColor(kBlack)
        histoRef.SetMarkerStyle(26)
        histoRef.SetLineWidth(2)

        histoNS=fNS3.Get(name)
        histoNS.SetLineColor(kPink)
        histoNS.SetMarkerColor(kPink)
        histoNS.SetMarkerStyle(20)
        histoNS.SetLineWidth(2)

        histoTRel=fTRel.Get(name) 
        histoTRel.SetLineColor(kAzure)
        histoTRel.SetMarkerColor(kAzure)
        histoTRel.SetMarkerStyle(21)
        histoTRel.SetLineWidth(2)

        histoMRel=fMRel.Get(name)
        histoMRel.SetLineColor(kAzure+1)
        histoMRel.SetMarkerColor(kAzure+1)
        histoMRel.SetMarkerStyle(23)
        histoMRel.SetLineWidth(2)

        histoRef.SetXTitle(xtitle)
        histoRef.SetYTitle("rate, kHz")
        histoRef.GetYaxis().SetRangeUser(0.1,5e5)
        histoRef.GetXaxis().SetRangeUser(0,60)
        histoRef.GetYaxis().SetTitleOffset(1.6)
        histoRef.GetXaxis().SetTitleOffset(1.6)


	# Scale to total rate
	histoRef.Scale(31038.0)
	histoNS.Scale(31038.0)
	histoTRel.Scale(31038.0)
	histoMRel.Scale(31038.0)

	histoRef.Draw("hist")
        histoNS.Draw("hist,sames")
        histoTRel.Draw("hist,sames")
        histoMRel.Draw("hist,sames")

	leg =TLegend(0.5,0.60,0.99,0.95,"","brNDC");
	leg.SetFillStyle(0)
	leg.SetBorderSize(0)
	entry=leg.AddEntry(histoRef,"NStubs>=2","l");
        entry=leg.AddEntry(histoNS,"NStubs>=3","l");
        entry=leg.AddEntry(histoMRel,"NStubs>=2, Qual>64","l");
        entry=leg.AddEntry(histoTRel,"NStubs>=2, Qual>98","l");
	leg.Draw()

	c.SaveAs("Rate_"+name+"_ID.png")


#plotHistos("rateGMTTkMuonAllEta","AllEta Rate, Rel Isolation check, GeV")
plotHistos("rateGMTTkMuonBarrel","Barrel Rate, Rel Isolation check, GeV") 
plotHistos("rateGMTTkMuonEndcap","Endcap Rate, Rel Isolation check, GeV")
plotHistos("rateGMTTkMuonOverlap","Overlap Rate, Rel Isolation check, GeV")
