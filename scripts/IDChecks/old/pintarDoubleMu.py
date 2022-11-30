#!/usr/bin/env python 
from ROOT import *

import tdrstyle

#set the tdr style
tdrstyle.setTDRStyle()

#fDec = TFile( 'count_MinBias_muontree.root') 
#fMike = TFile('count_Merged_MinBias_GMTRev_2.root') 

fDec = TFile( 'count_DoubleMuGun_muontree.root') 
fMike = TFile('count_Merged_DoubleMu_GMTRev_2.root') 


def plotHistosStubs(fileDec,fileMike,name,xtitle):
	c=TCanvas("c"+name)
        c.SetLogy()
#        c.SetGrid()

        histo=fileDec.Get("countTkGlb"+name)
        histo.SetLineColor(kBlue)
        histo.SetMarkerColor(kBlue)
        histo.SetMarkerStyle(3)
	histo.SetLineWidth(2)
        histo.SetLineStyle(kDashed)

        histo2=fileDec.Get("countGMTTkMuon"+name)
        histo2.SetLineColor(kBlue)
        histo2.SetMarkerColor(kBlue)
        histo2.SetMarkerStyle(34)
        histo2.SetLineWidth(2)

        histo3=fileMike.Get("countTkGlb"+name)
        histo3.SetLineColor(kRed)
        histo3.SetMarkerColor(kRed)
        histo3.SetMarkerStyle(25)
        histo3.SetLineWidth(2)
        histo3.SetLineStyle(kDashed)

        histo4=fileMike.Get("countGMTTkMuon"+name)
        histo4.SetLineColor(kRed)
        histo4.SetMarkerColor(kRed)
        histo4.SetMarkerStyle(34)
        histo4.SetLineWidth(2)


	histo4.SetXTitle(xtitle)
        histo4.SetYTitle("a.u.")
	histo4.GetYaxis().SetRangeUser(0.1,5e5)
        histo4.GetXaxis().SetRangeUser(0,60)
        histo4.GetYaxis().SetTitleOffset(1.6)
        histo4.GetXaxis().SetTitleOffset(1.6)

	histo4.DrawNormalized("hist")
        histo.DrawNormalized("sames,hist")
        histo3.DrawNormalized("sames,hist")
        histo2.DrawNormalized("sames,hist")


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

	c.SaveAs("countBranchComparison_"+name+".png")

plotHistosStubs(fDec,fMike,"Barrel","Muon P_{T}, BARREL")
plotHistosStubs(fDec,fMike,"Overlap","Muon P_{T}, OVERLAP")
plotHistosStubs(fDec,fMike,"Endcap","Muon P_{T}, ENDCAP")



