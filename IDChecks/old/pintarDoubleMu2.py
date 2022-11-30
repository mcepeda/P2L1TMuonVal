#!/usr/bin/env python 
from ROOT import *

import tdrstyle

#set the tdr style
tdrstyle.setTDRStyle()

fMB = TFile( 'checks_MB_GMTIso_ID.root') 
fDoubleMuGun = TFile('checks_DoubleMu_GMTIso_ID_Matched.root') 


def plotHistosStubs(fileMB,fileDoubleMuGun,name,xtitle, maxY=1,logY=False):
	c=TCanvas("c"+name)
	if logY==True:
	        c.SetLogy()
#        c.SetGrid()

        histo=fileDoubleMuGun.Get(name)
        histo.SetLineColor(kBlue)
        histo.SetMarkerColor(kBlue)
        histo.SetMarkerStyle(3)
	histo.SetLineWidth(3)

        histo2=fileMB.Get(name)
        histo2.SetLineColor(kRed)
        histo2.SetMarkerColor(kRed)
        histo2.SetMarkerStyle(34)
        histo2.SetLineWidth(3)

	histo.SetXTitle(xtitle)
        histo.SetYTitle("a.u.")
	histo.GetYaxis().SetRangeUser(0.1,maxY)
#        histo.GetXaxis().SetRangeUser(0,60)
        histo.GetYaxis().SetTitleOffset(1.6)
        histo.GetXaxis().SetTitleOffset(1.6)

	histo.Scale(1./histo.Integral())
        histo2.Scale(1./histo2.Integral())

	if histo2.GetMaximum()>histo.GetMaximum():
		histo.SetMaximum(histo2.GetMaximum()*1.1)

	histo.Draw("hist")
        histo2.Draw("sames,hist")

	leg =TLegend(0.5,0.95,0.9,0.60,"","brNDC");
	leg.SetFillStyle(0)
	leg.SetBorderSize(0)
        entry=leg.AddEntry(histo,"DoubleMuGun","l");
	entry=leg.AddEntry(histo2,"Min Bias","l");


	leg.Draw()

	c.SaveAs("count_MBvsDoubleMu_"+name+".png")

plotHistosStubs(fMB,fDoubleMuGun,"muonPtBin","Muon P_{T} BIN",1.2,1)
plotHistosStubs(fMB,fDoubleMuGun,"muonEtaBin","Muon #eta BIN",0.4)
plotHistosStubs(fMB,fDoubleMuGun,"muonQuality","Muon Quality",0.4)



