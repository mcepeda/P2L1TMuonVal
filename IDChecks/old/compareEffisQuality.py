#!/usr/bin/env python 
from ROOT import *

import tdrstyle

#set the tdr style
tdrstyle.setTDRStyle()

fNOCUT= TFile( 'effi_example__NOCUT_Pt2-5_DoubleMu_GMTIso_ID.root') 
fWP98 = TFile( 'effi_example__Q98_Pt2-5_DoubleMu_GMTIso_ID.root')
fWP95 = TFile( 'effi_example__Q95_Pt2-5_DoubleMu_GMTIso_ID.root')
fWP90 = TFile( 'effi_example__Q90_Pt2-5_DoubleMu_GMTIso_ID.root')
fWP85 = TFile( 'effi_example__Q85_Pt2-5_DoubleMu_GMTIso_ID.root')

def plotHistos(name,xtitle):
	c=TCanvas("c"+name)
        histoRef=fNOCUT.Get("effi_gmtTkMuon__NOCUT_Pt2-5__"+name)
        histoRef.SetLineColor(kBlack)
        histoRef.SetMarkerColor(kBlack)
        histoRef.SetMarkerStyle(20)
        histoRef.SetLineWidth(2)

        histoWP98=fWP98.Get("effi_gmtTkMuon__Q98_Pt2-5__"+name) 
        histoWP98.SetLineColor(kAzure)
        histoWP98.SetMarkerColor(kAzure)
        histoWP98.SetMarkerStyle(21)
        histoWP98.SetLineWidth(2)

        histoWP95=fWP95.Get("effi_gmtTkMuon__Q95_Pt2-5__"+name)
        histoWP95.SetLineColor(kAzure+1)
        histoWP95.SetMarkerColor(kAzure+1)
        histoWP95.SetMarkerStyle(23)
        histoWP95.SetLineWidth(2)

        histoWP90=fWP90.Get("effi_gmtTkMuon__Q90_Pt2-5__"+name)
        histoWP90.SetLineColor(kAzure+2)
        histoWP90.SetMarkerColor(kAzure+2)
        histoWP90.SetMarkerStyle(26)
        histoWP90.SetLineWidth(2)

        histoWP85=fWP85.Get("effi_gmtTkMuon__Q85_Pt2-5__"+name)
        histoWP85.SetLineColor(kAzure+4)
        histoWP85.SetMarkerColor(kAzure+4)
        histoWP85.SetMarkerStyle(26)
        histoWP85.SetLineWidth(2)

	histoRef.SetXTitle(xtitle)
        histoRef.SetYTitle("Efficiency")
	histoRef.GetYaxis().SetRangeUser(0.,1)

	histoRef.Draw()
        histoWP98.Draw("sames")
        histoWP95.Draw("sames")
        histoWP90.Draw("sames")
        histoWP85.Draw("sames")

	leg =TLegend(0.8,0.150,0.99,0.4,"","brNDC");
	leg.SetFillStyle(0)
	leg.SetBorderSize(0)
	entry=leg.AddEntry(histoRef,"No Iso","lp");
        entry=leg.AddEntry(histoWP98,"WP98","lp");
        entry=leg.AddEntry(histoWP95,"WP95","lp");
	entry=leg.AddEntry(histoWP90,"WP90","lp");
        entry=leg.AddEntry(histoWP85,"WP85","lp");
	leg.Draw()

	c.SaveAs("Effi_Pt2-5_Qual_"+name+"_.png")

plotHistos("Eta","Muon #eta")
plotHistos("Pt","Muon P_{T}")

plotHistos("Eta_NStubs2","Muon #eta")
plotHistos("Pt_NStubs2","Muon P_{T}")

