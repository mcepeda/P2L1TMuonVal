#!/usr/bin/env python 
from ROOT import *

import tdrstyle

#set the tdr style
tdrstyle.setTDRStyle()

fIso = TFile('checks_MinBias_GMTIsoPFISODR02.root')

def plotHistos(xtitle):
	c=TCanvas("c")
        c.SetLogy()
        c.SetGrid()

        histoRef=fIso.Get("All")
        histoRef.SetLineColor(kBlack)
        histoRef.SetMarkerColor(kBlack)
        histoRef.SetMarkerStyle(26)
        histoRef.SetLineWidth(2)

        histoTRel=fIso.Get("IsoRel0p2") 
        histoTRel.SetLineColor(kAzure)
        histoTRel.SetMarkerColor(kAzure)
        histoTRel.SetMarkerStyle(21)
        histoTRel.SetLineWidth(2)

        histoMRel=fIso.Get("IsoRel0p5")
        histoMRel.SetLineColor(kAzure+1)
        histoMRel.SetMarkerColor(kAzure+1)
        histoMRel.SetMarkerStyle(23)
        histoMRel.SetLineWidth(2)


        histoLRel=fIso.Get("IsoRel1")
        histoLRel.SetLineColor(kAzure+2)
        histoLRel.SetMarkerColor(kAzure+2)
        histoLRel.SetMarkerStyle(25)
        histoLRel.SetLineWidth(2)

        histoTKT=fIso.Get("IsoRelTKT")
        histoTKT.SetLineColor(kPink+2)
        histoTKT.SetMarkerColor(kPink+2)
        histoTKT.SetMarkerStyle(25)
        histoTKT.SetLineWidth(2)


        histoRef.SetXTitle(xtitle)
        histoRef.SetYTitle("rate, kHz")
#        histoRef.GetYaxis().SetRangeUser(0.1,5e5)
        histoRef.GetXaxis().SetRangeUser(0,60)
        histoRef.GetYaxis().SetTitleOffset(1.6)
        histoRef.GetXaxis().SetTitleOffset(1.6)

	histoRef.Draw("hist")
        histoTKT.Draw("hist,sames")
        histoTRel.Draw("hist,sames")
        histoMRel.Draw("hist,sames")
	histoLRel.Draw("hist,sames")

	leg =TLegend(0.5,0.60,0.99,0.95,"","brNDC");
	leg.SetFillStyle(0)
	leg.SetBorderSize(0)
	entry=leg.AddEntry(histoRef,"No Iso","l");
        entry=leg.AddEntry(histoTRel,"PFIsoRel, <0.2","l");
        entry=leg.AddEntry(histoMRel,"PFIsoRel, <0.5","l");
	entry=leg.AddEntry(histoLRel,"PFIsoRel, <1","l");
        entry=leg.AddEntry(histoTKT,"TKIso, Tight Rel, hwIso>=12","l");

	leg.Draw()

	c.SaveAs("Rate_PFDR02_RELISO.png")

plotHistos("Rate, Rel Isolation check, GeV") 
