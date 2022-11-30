#!/usr/bin/env python 
from ROOT import *

import tdrstyle

#set the tdr style
tdrstyle.setTDRStyle()

fNoCut= TFile( 'effi_example__all__NoCut_Pt15_DoubleMu_GMTIso_ID.root') 
fWP98 = TFile( 'effi_example__all__Q98_Pt15_DoubleMu_GMTIso_ID.root')
fDef  = TFile( 'effi_example__all__NoCutsInGaps_Pt15_DoubleMu_GMTIso_ID.root')

def plotHistos(name,xtitle):
	c=TCanvas("c"+name)
        histoRef=fNoCut.Get("effi_gmtTkMuon__all__NoCut_Pt15__"+name)
        histoRef.SetLineColor(kBlack)
        histoRef.SetMarkerColor(kBlack)
        histoRef.SetMarkerStyle(20)
        histoRef.SetLineWidth(2)

        histoWP98=fWP98.Get("effi_gmtTkMuon__all__Q98_Pt15__"+name) 
        histoWP98.SetLineColor(kAzure)
        histoWP98.SetMarkerColor(kAzure)
        histoWP98.SetMarkerStyle(21)
        histoWP98.SetLineWidth(2)

        histoDef=fDef.Get("effi_gmtTkMuon__all__NoCutsInGaps_Pt15__"+name) 
        histoDef.SetLineColor(kRed)
        histoDef.SetMarkerColor(kRed)
        histoDef.SetMarkerStyle(22)
        histoDef.SetLineWidth(2)


	histoRef.SetXTitle(xtitle)
        histoRef.SetYTitle("Efficiency")
	histoRef.GetYaxis().SetRangeUser(0.,1)

	histoRef.Draw()
        histoWP98.Draw("sames")
        histoDef.Draw("sames")

	leg =TLegend(0.7,0.50,0.99,0.65,"","brNDC");
	leg.SetFillStyle(0)
	leg.SetBorderSize(0)
	entry=leg.AddEntry(histoRef,"No Iso","lp");
        entry=leg.AddEntry(histoWP98,"WP98","lp");
        entry=leg.AddEntry(histoDef,"Relax in Gaps","lp");

	leg.Draw()

	c.SaveAs("Effi_Qual_98HighPt_"+name+"_.png")

plotHistos("Eta","Muon #eta")
plotHistos("Pt","Muon P_{T}")

plotHistos("Eta_NStubs2","Muon #eta")
plotHistos("Pt_NStubs2","Muon P_{T}")

