#!/usr/bin/env python 
from ROOT import *

import tdrstyle

#set the tdr style
tdrstyle.setTDRStyle()

fDec = TFile( 'rate_MinBias_muontree.root') # this is only Pt 2-5 GeV
fMike = TFile('rate_Merged_MinBias_GMTRev_2.root') 

def plotHistosStubs(fileDec,fileMike,name,xtitle):
	c=TCanvas("c"+name)
        c.SetLogy()
        c.SetGrid()

        histo=fileDec.Get("rateTkGlb"+name)
        histo.SetLineColor(kBlue)
        histo.SetMarkerColor(kBlue)
        histo.SetMarkerStyle(3)
	histo.SetLineWidth(2)
        histo.SetLineStyle(kDashed)

        histo2=fileDec.Get("rateGMTTkMuon"+name)
        histo2.SetLineColor(kBlue)
        histo2.SetMarkerColor(kBlue)
        histo2.SetMarkerStyle(34)
        histo2.SetLineWidth(2)

        histo3=fileMike.Get("rateTkGlb"+name)
        histo3.SetLineColor(kRed)
        histo3.SetMarkerColor(kRed)
        histo3.SetMarkerStyle(25)
        histo3.SetLineWidth(2)
        histo3.SetLineStyle(kDashed)

        histo4=fileMike.Get("rateGMTTkMuon"+name)
        histo4.SetLineColor(kRed)
        histo4.SetMarkerColor(kRed)
        histo4.SetMarkerStyle(34)
        histo4.SetLineWidth(2)


	histo.SetXTitle(xtitle)
        histo.SetYTitle("rate, kHz")
	histo.GetYaxis().SetRangeUser(0.1,5e5)
        histo.GetXaxis().SetRangeUser(0,60)
        histo.GetYaxis().SetTitleOffset(1.6)
        histo.GetXaxis().SetTitleOffset(1.6)

	histo.Draw("hist")
        histo2.Draw("sames,hist")
        histo3.Draw("sames,hist")
        histo4.Draw("sames,hist")


#        histo.Draw("sames,p")
#        histo2.Draw("sames,p")
#        histo3.Draw("sames,p")

        #histo4.Draw("sames,hist")

	leg =TLegend(0.5,0.95,0.9,0.60,"","brNDC");
	leg.SetFillStyle(0)
	leg.SetBorderSize(0)
        entry=leg.AddEntry(histo2,"GMTTkMuon, Standard","l");
	entry=leg.AddEntry(histo,"tkGlbMuon, Standard","l");
        entry=leg.AddEntry(histo4,"GMTTkMuon, GMTrev","l");
        entry=leg.AddEntry(histo3,"tkGlbMuon, GMTrev","l");


	leg.Draw()

	c.SaveAs("rateBranchComparison_"+name+".png")

plotHistosStubs(fDec,fMike,"Barrel","Muon P_{T}, BARREL")
plotHistosStubs(fDec,fMike,"Overlap","Muon P_{T}, OVERLAP")
plotHistosStubs(fDec,fMike,"Endcap","Muon P_{T}, ENDCAP")



