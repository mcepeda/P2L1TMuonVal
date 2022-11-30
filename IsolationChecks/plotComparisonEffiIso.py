# EXAMPLE EFFICIENCY COMPARISON 

#!/usr/bin/env python 
from ROOT import *

import tdrstyle

#set the tdr style
tdrstyle.setTDRStyle()

filepath="allroots/"

names=["EXAMPLE","EXAMPLE_TIGHTREL","EXAMPLE_MEDIUMREL","EXAMPLE_LOOSEREL"]
colors=[kBlack,kAzure,kAzure+1,kAzure+2]
markers=[20,21,25,25]
leglabels=["No Iso", "Tight Rel tkIso (hw)", "Medium Rel tkIso (hw)", "Loose Rel tkIso (hw)"]


files={}

for i in range(0,len(names)):
	print (names[i])
	files[i]=TFile( filepath+'effi_example__'+names[i]+'_DoubleMuon_GMTIso.root') 

def plotHistos(name,xtitle):
	c=TCanvas("c"+name)
	c.SetGrid()
	leg =TLegend(0.6,0.30,0.99,0.65,"","brNDC")
	leg.SetFillStyle(0)
	leg.SetBorderSize(0)

	histos={}
	for i in range(0,len(names)):
		histos[i]=files[i].Get("effi_gmtTkMuon__"+names[i]+"__"+name)
		histos[i].SetName("histo"+names[i])
		histos[i].SetLineColor(colors[i])
                histos[i].SetMarkerColor(colors[i])
		histos[i].SetMarkerStyle(markers[i])
        	histos[i].SetYTitle("Efficiency")
		histos[i].GetYaxis().SetRangeUser(0.8,1)
        	histos[i].GetYaxis().SetTitleOffset(1.5)
		entry=leg.AddEntry(histos[i],leglabels[i],"lp")
		if i==0:
			histos[i].Draw()
		else:
			histos[i].Draw("sames")

	leg.Draw()

	c.SaveAs("Effi_"+name+"_RELISO.png")

plotHistos("Eta","Muon #eta")
plotHistos("Pt","Muon P_{T}")

#plotHistos("Eta_NStubs2","Muon #eta")
#plotHistos("Pt_NStubs2","Muon P_{T}")



