#!/usr/bin/env python 
from ROOT import *
from ROOT import TH1F 

file = TFile( 'dimuon_example__FullEta_Pt5_DY_M50_12_5.root')
filelow = TFile( 'dimuon_example__FullEta_Pt5_DYLowMass_12_5.root')

gStyle.SetOptStat(0)

# Get Plots
gmttk=file.Get("ZMass_GmtTk")
gmt=file.Get("ZMass_Gmt")
gen=file.Get("ZMass_Gen")

gmttklow=filelow.Get("ZMass_GmtTk")
genlow=filelow.Get("ZMass_Gen")
genlow.SetName("ZMass_Gen_Low")
gmttklow.SetName("ZMass_GmtTk_Low")

# Scale 
Lumi=1000

# XSecs from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#DY_Z
# Scale to 14 TeV from Guillelmo's ratio to 7TeV : https://ceballos.web.cern.ch/ceballos/random/xsec_ecm.txt
scale13To14=2.029/1.95695 
Xsec50=6077.22*scale13To14
Xsec10To50=18610*scale13To14

#N50=298950
N50=193120
N10To50=99360

gmttk.Scale(Xsec50*Lumi/N50)
gmt.Scale(Xsec50*Lumi/N50)
gen.Scale(Xsec50*Lumi/N50)
gmttklow.Scale(Xsec10To50*Lumi/N10To50)
genlow.Scale(Xsec10To50*Lumi/N10To50)

# combined?

nbins=gen.GetNbinsX()
min=gen.GetXaxis().GetXmin()
max=gen.GetXaxis().GetXmax()

genfullRange=TH1F("genfullRange","genfullRange",nbins,min,max)
genfullRange.Add(genlow)
genfullRange.Add(gen)

gmttkfullRange=TH1F("gmttkfullRange","gmttkfullRange",nbins,min,max)
gmttkfullRange.Add(gmttklow)
gmttkfullRange.Add(gmttk)


# Colors
gen.SetLineColor(kBlue+3)
genlow.SetLineColor(kGreen+3)
genfullRange.SetLineColor(kBlack)

gmt.SetLineColor(kRed)
gmt.SetMarkerColor(kRed)

gmttk.SetLineColor(kBlue)
gmttklow.SetLineColor(kGreen+2)
gmttk.SetMarkerColor(kBlue)
gmttklow.SetMarkerColor(kGreen+2)
gmttkfullRange.SetLineColor(kBlue)
gmttkfullRange.SetMarkerColor(kBlue)
gmttkfullRange.SetMarkerStyle(20)

gen.SetLineWidth(3)
genlow.SetLineWidth(3)
genfullRange.SetLineWidth(3)

gen.SetTitle("")
gen.SetXTitle("M_{#mu#mu} [GeV]")
gen.SetYTitle("Events / 2 GeV / 1 fb^{-1}]")

genfullRange.SetTitle("")
genfullRange.SetXTitle("M_{#mu#mu} [GeV]")
genfullRange.SetYTitle("Events / 2 GeV / 1 fb^{-1}")

# to mix samples:
gen.GetXaxis().SetRangeUser(10,200)
genfullRange.GetXaxis().SetRangeUser(10,200)

#gmttk.GetXaxis().SetRangeUser(50,200)
#gmttklow.GetXaxis().SetRangeUser(10,50)

c1=TCanvas("c1")
c1.SetLogy()

gen.Draw("hist")
gmttk.Draw("sames")

genlow.Draw("hist,sames")
gmttklow.Draw("sames")

leg =TLegend(0.5,0.90,0.90,0.55,"","brNDC")
leg.SetFillStyle(0)
leg.SetBorderSize(0)
#entry=leg.AddEntry("NULL","DY M-50, 12_3_X","")
entry=leg.AddEntry("NULL","DY M-50, 12_5_X","")
entry=leg.AddEntry(gen,"Gen Muons","l")
entry=leg.AddEntry(gmttk,"P2 GMTTK","lp")
entry=leg.AddEntry("NULL","DY M 10-50, 12_5_X","")
entry=leg.AddEntry(genlow,"Gen Muons","l")
entry=leg.AddEntry(gmttklow,"P2 GMTTK","lp")
leg.Draw()

c1.SaveAs("massPlotDY.png")

c2=TCanvas("c2")
c2.SetLogy()

genfullRange.Draw("hist")
gmttkfullRange.Draw("sames")

line = TLine(50,genfullRange.GetMinimum(),50,genfullRange.GetMaximum()*2);
line.SetLineColor(kGray)
line.SetLineWidth(1)
line.Draw()


leg =TLegend(0.5,0.90,0.90,0.6,"","brNDC")
leg.SetFillStyle(0)
leg.SetBorderSize(0)
entry=leg.AddEntry("NULL","DY M10To50 + M50","")
entry=leg.AddEntry("NULL","Pt_{mu}> 5 GeV","")
entry=leg.AddEntry(genfullRange,"Gen Muons","l")
entry=leg.AddEntry(gmttkfullRange,"P2 GMTTK","lp")
leg.Draw()

c2.SaveAs("massPlotDY2.png")



