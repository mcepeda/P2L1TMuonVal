#!/usr/bin/env python 
from ROOT import *

import tdrstyle

#set the tdr style
tdrstyle.setTDRStyle()

suffix='AllTest'

fQual = TFile('checks_ratesMulti_MB_GMTIso_IDQual_All.root')  #'checks_MB_GMTIso_IDQual_'+suffix+'.root')


def plotHistos(xtitle,Label):
	c=TCanvas("c")
        c.SetLogy()
        c.SetGrid()

        histoRef=fQual.Get("NoCut"+Label)
        histoRef.SetLineColor(kBlack)
        histoRef.SetMarkerColor(kBlack)
        histoRef.SetMarkerStyle(26)
        histoRef.SetLineWidth(2)

        histoTRel=fQual.Get("WP98"+Label) 
        histoTRel.SetLineColor(kAzure)
        histoTRel.SetMarkerColor(kAzure)
        histoTRel.SetMarkerStyle(21)
        histoTRel.SetLineWidth(2)

        histoMRel=fQual.Get("WP95"+Label)
        histoMRel.SetLineColor(kAzure+1)
        histoMRel.SetMarkerColor(kAzure+1)
        histoMRel.SetMarkerStyle(23)
        histoMRel.SetLineWidth(2)


        histoLRel=fQual.Get("WP90"+Label)
        histoLRel.SetLineColor(kAzure+2)
        histoLRel.SetMarkerColor(kAzure+2)
        histoLRel.SetMarkerStyle(25)
        histoLRel.SetLineWidth(2)

        histoTKT=fQual.Get("WP85"+Label)
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
	entry=leg.AddEntry(histoRef,"No Cut","l");
        entry=leg.AddEntry(histoTRel,"WP98","l");
        entry=leg.AddEntry(histoMRel,"WP95","l");
	entry=leg.AddEntry(histoLRel,"WP90","l");
        entry=leg.AddEntry(histoTKT,"WP85","l");

	leg.Draw()

	c.SaveAs("RateMulti_Qual_"+suffix+Label+".png")

plotHistos("Single Muon Rate, GeV","")
plotHistos("Double Muon Rate, GeV","_Double")
plotHistos("Triple Muon Rate, GeV","_Triple")
 