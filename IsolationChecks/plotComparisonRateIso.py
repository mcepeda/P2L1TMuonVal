# EXAMPLE RATE COMPARISON PLOT

#!/usr/bin/env python 
from ROOT import *

import tdrstyle

#set the tdr style
tdrstyle.setTDRStyle()

filename="checks_MinBias_GMTIso_EXAMPLE"
filepath="allroots/"

plotLabel="RateExample" 
histoNames=["All","IsoRel0p2","IsoRel0p5","IsoRel1","IsoRelTKT"]
colors=[kBlack,kAzure,kAzure+1,kAzure+2,kPink+2]
markers=[26,21,23,25,24]
leglabels=["No Iso","PFIsoRel, I<0.2","PFIsoRel, I<0.5","PFIsoRel, I<1","TKIso, TightRel, hwIso>=12"]

fileInput = TFile(filepath+filename+'.root')

def plotHistos(xtitle):
	c=TCanvas("c")
        c.SetLogy()
        c.SetGrid()
	leg =TLegend(0.5,0.40,0.99,0.95,"","brNDC")
	leg.SetFillStyle(0)
	leg.SetBorderSize(0)

	histos={}

	for i in range(0,len(histoNames)):
		histos[i]=fileInput.Get(histoNames[i])
		histos[i].SetLineColor(colors[i])
		histos[i].SetMarkerColor(colors[i])
		histos[i].SetMarkerStyle(markers[i])
		histos[i].SetLineWidth(2)
        	histos[i].SetXTitle(xtitle)
        	histos[i].SetYTitle("rate, kHz")
        	histos[i].GetYaxis().SetRangeUser(0.8,6e4)
        	histos[i].GetXaxis().SetRangeUser(0,60)
        	histos[i].GetYaxis().SetTitleOffset(1.6)
        	histos[i].GetXaxis().SetTitleOffset(1.6)
		entry=leg.AddEntry(histos[i],leglabels[i],"l")
		if i==0:
			histos[i].Draw("hist")
		else: 
			histos[i].Draw("hist,same")	

	leg.Draw()

	c.SaveAs(plotLabel+".png")


plotHistos("Rate, PF Isolation check (DR=0.2), GeV") 
