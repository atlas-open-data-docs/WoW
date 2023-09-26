---
title: "Histogram Analyser (simulation only)"
date: 2023-05-23T04:51:13+01:00
draft: false
hideLastModified: true
keepImageRatio: false
showInMenu: false
---

# Histogram Analyser

## Recap: What is the major difference between a histogram and a bar graph?

The x variable of a histogram is continuous, grouped into **ranges or ‘bins’**.

Physicists use **cuts** to select events of interest.  Cuts preferentially remove the unwanted processes (background) but leave as much as possible of the desired process (signal).  It is useful to have a good understanding of the physics processes involved when applying cuts.

We have created two Histogram Analysers, to help visualise the data:
The first Histogram Analyser displays just simulated (MC) events.  
The second Histogram Analyser displays both real data and simulated events.  

Both histogram analysers display four physics processes.  These are: \\(H\rightarrow W^+W^-\\), \\(WW\\), \\(t\bar t\\) and \\(Z\\).  Each process is represented by a different colour in Histogram Analyser. A more in depth discussion of them can be found in the next chapter. 

## Make cuts using your cursor.

Use the cursor to select a specific range in one of the histograms. These will be coloured, whilst non-selected ranges will be greyed out.  When you make cuts on a variable, the relative contributions of each of the four processes will change.

**To clear your selection on a specific histogram:** click on the white background within the histogram area. 

**To clear all your selections:** click on "Histogram Analyser" under Get Started in the main top menu.

## The histograms explained

**Higgs to WW - simulated data**
Histogram Analyser displays nine histograms.  The description of each follows.

The histograms can take about 30 seconds to load. Whilst loading you'll only see the histogram titles. Once loaded you'll see the histograms appear under their titles.

We think it really helps to be able to see all nine histograms on your screen at the same time. So if this isn't the case to start with, we suggest decreasing the zoom in your web browser until you can see all nine (e.g 67%).

{{< rawhtml >}}
<html lang="en">
  <head>
    <title>Crossfilter for ATLAS Outreach Prototype</title>
    <meta charset="UTF-8">
    <link rel="stylesheet" type="text/css" href="interactive/dc.css"/>
  </head>
  <style>
  .dc-chart g.row text {
      fill: black;
      font-size: 110%;
  }
  table { border-collapse:collapse; }
  table thead th { border-bottom: 1px solid #000; }
 </style>

  <body>
    <div style="width:1050px">
<table style="width:50%">
  <tr style="height: 50px">
    <td valign="bottom">Channel</td>
    <td valign="bottom">Reconstructed Dilepton Mass</td>
    <td valign="bottom">Number of Jets</td>
  </tr>
  <tr>
    <td><div id="hist1" title="Channel: The leptonic decay channels are shown here: dielectron (ee), dimuon (μμ) and electron-muon (eμ)"></div></td>
    <td><div id="hist2" title="Reconstructed Dilepton Mass (M(ll)): the mass reconstructed from the two leptons in the final state."></div></td>
    <td><div id="hist3" title="Number of Jets (N(Jets)): number of jets in the event."></div></td>
  </tr>
  <tr style="height: 50px">
    <td valign="bottom">Are Jets b-tagged?</td>
    <td valign="bottom">Total Lepton Transverse Momentum</td>
    <td valign="bottom">Missing Transverse Momentum (MET)</td>
  </tr>
  <tr>
    <td><div id="hist4" title="Are Jets b-tagged? (BTag) : jets originating from b-quarks are identified and labelled, or tagged, using so-called b-tagging algorithms."></div></td>
    <td><div id="hist5" title="Total Lepton Transverse Momentum (PT(ll)): this is the vectorial sum of the transverse momenta of the observed charged leptons."></div></td>
    <td><div id="hist6" title="Missing Transverse Momentum (MET) : MET is used to infer the presence of non-detectable particles such as the neutrino."></div></td>
  </tr>
  <tr style="height: 50px">
    <td valign="bottom">Opening Angle Between MET and Leptons</td>
    <td valign="bottom">Opening Angle Between Leptons</td>
    <td valign="bottom">Expected Number of Events for 10/fb</td>
  </tr>
  <tr>
    <td><div id="hist7" title="Opening Angle Between MET and Leptons (DeltaPhi(MET,ll)): This is the opening angle, measured in phi (&phi;), between the missing transverse momentum (MET) and the two leptons."></div></td>
    <td><div id="hist8" title="Opening Angle Between Leptons (DeltaPhi(l,l)): this is the angle, measured in phi (&phi;), between the two leptons. The azimuthal angle &phi; is measured from the x-axis, around the beam."></div></td>
    <td><div id="hist9" title="Number of Expected Events: the number of events expected to be detected, reconstructed and recorded by ATLAS for 10 inverse femtobarn of data.  Numbers taken from simulation. The significance of the H &rarr; WW events quantifies how 'significant' the Higgs sample is with respect to the background. (Number of H &rarr; WW events)/Number of background events. The larger the significance value is, the better job you have done extracting the Higgs signal."></div></td>

 </table>
</div>

    <script charset="utf-8" type="text/javascript" src="interactive/d3.js"></script>
    <script charset="utf-8" type="text/javascript" src="interactive/crossfilter.js"></script>
    <script charset="utf-8" type="text/javascript" src="interactive/dc.js"></script>
    <script charset="utf-8" type="text/javascript">

      d3.csv("interactive/13TeV_outreach.csv", function(error, events) {

          events.forEach(function(x) {
             x.weight = +x.weight;
          });
         

          function add_by_channel(p, v) {
                 p[v.type] = (p[v.type] || 0) + v.weight;
                 return p;
          }

          function remove_by_channel(p, v) {
                 p[v.type] = (p[v.type] || 0) - v.weight;
                 return p;
          }

          function initial(p, v) {
             return {};
          }
          
          var colorScale = d3.scale.ordinal().range(["#1C5EA8","#F66A00","#2A9000","#C31318"]);
          var ndx                       = crossfilter(events),
              njetDimension             = ndx.dimension(function(d) {return +d.NJets;}),
              typeDimension             = ndx.dimension(function(d) {return +d.type;}),
              METDimension              = ndx.dimension(function(d) {return +Math.floor(d.MET*0.1)*10;}),
              DeltaPhiMETLLDimension    = ndx.dimension(function(d) {return +Math.floor(Math.abs(d.METLLDeltaPhi*0.31813*18))*10;}),
              SumLepPtDimension         = ndx.dimension(function(d) {return +Math.floor(d.SumLepPt*0.1)*10;}),
              ZWindowDimension          = ndx.dimension(function(d) {return +Math.floor(d.Mll*0.2)*5;}),
              ChannelDimension          = ndx.dimension(function(d) {return +d.Channel;}),
              DeltaPhiDimension         = ndx.dimension(function(d) {return +Math.floor(d.LepDeltaPhi*0.31813*18)*10;})
              BTagDimension             = ndx.dimension(function(d) {return +d.BTags})
              NJetGroup                 = njetDimension.group().reduce(add_by_channel,remove_by_channel, initial),
              DeltaPhiMETLLGroup        = DeltaPhiMETLLDimension.group().reduce(add_by_channel,remove_by_channel, initial),
              SumLepPtGroup             = SumLepPtDimension.group().reduce(add_by_channel,remove_by_channel, initial),
              ZWindowGroup              = ZWindowDimension.group().reduce(add_by_channel,remove_by_channel, initial),
              BTagGroup                 = BTagDimension.group().reduce(add_by_channel,remove_by_channel, initial),
              compGroup                 = typeDimension.group().reduceSum(function(d) {return +d.weight;}),
              mcstatGroup               = typeDimension.group().reduceCount(),
              ChannelGroup              = ChannelDimension.group().reduce(add_by_channel,remove_by_channel, initial),
              METGroup                  = METDimension.group().reduce(add_by_channel,remove_by_channel, initial),
              DeltaPhiGroup             = DeltaPhiDimension.group().reduce(add_by_channel,remove_by_channel, initial),
              SignificanceGroup         = typeDimension.groupAll().reduce(
                  function (p, v) {
                      if (v.type == 1) p.sig += v.weight;
                      if (v.type != 0 && v.type != 1) p.bkg += v.weight;
                      return p;
                  },
                  function (p, v) {
                      if (v.type == 1) p.sig -= v.weight;
                      if (v.type != 0 && v.type != 1) p.bkg -= v.weight;
                      return p;
                  },
                  function () { return {sig:0, bkg:0}; }
              );
            
           function sel_stack(i) {
               return function(d) {
                   return d.value[i];
               };
           }
          
           function type(i){
              if (i == "1") return "H \u2192 WW";
              if (i == "2") return "WW";
              if (i == "3") return "ttbar";
              if (i == "4") return "Z";
              return "default"
           }
          
           function make_barchart( location, domain, label, dimension, group ){
             var chart = dc.barChart(location)
             chart.width(270)
                  .height(250)
                  .x(d3.scale.linear().domain(domain))
                  .margins({left: 55, top: 10, right: 10, bottom: 35})
                  .brushOn(true)
                  .elasticY(true)
                  .xAxisLabel(label)
                  .yAxisLabel("Events")
                  .clipPadding(10)
                  .dimension(dimension)
                  .group(group, "H \u2192 WW", sel_stack('1'))
                  .stack(group, "WW",          sel_stack('2'))
                  .stack(group, "ttbar",       sel_stack('3'))
                  .stack(group, "Z",           sel_stack('4'))
                  .on('renderlet', function (chart) {
                      chart.selectAll('.x-axis-label').attr('transform', 'translate(270,238)').attr('text-anchor', 'end');
                      chart.selectAll('.y-axis-label').attr('transform', 'rotate(-90), translate(-30,12)');
                  });
             return chart
          }
                                            
          var njetChart = make_barchart("#hist3", [-0.5,10], "N(Jets)", njetDimension, NJetGroup)
          njetChart.centerBar(true)
          njetChart.legend(dc.legend().x(200).y(10).itemHeight(20).gap(5))


          var channelChart = make_barchart("#hist1", [0,3], "Channel", ChannelDimension, ChannelGroup)
          channelChart.xAxis().tickFormat(function(d){if(d == 0.5){return "ee"}; if(d == 1.5){return "μμ"};if(d == 2.5){return "eμ";}});

          var ZWindowChart = make_barchart("#hist2", [0,104.9], "M(ll) [GeV]", ZWindowDimension, ZWindowGroup)
          ZWindowChart.xUnits(dc.units.fp.precision(5));

          var METChart     = make_barchart("#hist6", [0,200], "MET [GeV]", METDimension, METGroup)
          METChart.xUnits(dc.units.fp.precision(10));

          var DeltaPhiMETLLChart    = make_barchart("#hist7", [0, 180],"DeltaPhi(MET,ll) [deg]" ,DeltaPhiMETLLDimension, DeltaPhiMETLLGroup)
          DeltaPhiMETLLChart.xUnits(dc.units.fp.precision(10));

          var deltaphiChart = make_barchart("#hist8", [0,180], "DeltaPhi(l,l) [deg]", DeltaPhiDimension, DeltaPhiGroup)
          deltaphiChart.xUnits(dc.units.fp.precision(10));

          var sumlepptChart = make_barchart("#hist5", [0,200], "PT(ll) [GeV]", SumLepPtDimension, SumLepPtGroup)
          sumlepptChart.xUnits(dc.units.fp.precision(10));

          var BTagChart = make_barchart("#hist4", [0,3], "BTag", BTagDimension, BTagGroup)
          BTagChart.xAxis().tickFormat(function(d){if(d == 0.5){return "no"}; if(d == 1.5){return "yes"}});
          BTagChart.xAxis().tickValues([0, 0.5,1,1.5,2]);

          var mcCompChart = dc.rowChart("#hist9")
          mcCompChart.width(270).height(250)
                     .margins({left: 5, top: 10, right: 10, bottom: 57})
                     .x(d3.scale.log().domain([0,1000]))
                     .title("Process")
                     .dimension(typeDimension)
                     .group(compGroup)
                     .label(function(d) {
                            val = type(d.key) + " (" + d.value.toFixed(0) + ")"
                            return (d.key != 1) ? val : val + "    Significance: " + significance(SignificanceGroup.value()).toFixed(3)
                     })
          
                     .elasticX(true)
                     .colors(colorScale)
                     .on('renderlet', function (chart) {
                         chart.selectAll('g.axis text').attr('transform', 'translate(-10,10) rotate(315)');
                     });
         
      var significance = function(d) {
          return d.sig/Math.sqrt(d.bkg);
       };


      dc.renderAll();

      });

    </script>

  </body>
</html>
{{< /rawhtml >}}

**Would you like to make more detailed cuts, increase the number of bins, or include a larger set of data?** Try [coding your data analysis](https://github.com/atlas-outreach-data-tools/notebooks-collection-opendata)!

## Expected Number of Events for 10/fb

This histogram shows the number of events expected to be detected, reconstructed and recorded by ATLAS for 10 inverse femtobarn (10/fb) of data.  
Ten inverse femtobarns correspond to approximately 1000 trillion proton-proton collisions.

The expected number of events reconstructed and recorded by ATLAS is different to the number of events produced.  
Some events will not be reconstructed due to the way the detector is constructed, the resolution of the sub-detectors, reconstruction efficiency and other inefficiencies.

![](images/NumbersNoSelection_13TeV.png)

With no cuts, we have 124 \\(H\rightarrow W^+W^-\\) events, with a total background of 7342087 events.  The majority of the background is \\(Z\\) boson production.

The **significance** of the  \\(H\rightarrow W^+W^-\\) events quantifies how "significant" the Higgs sample is with respect to the background.  It is calculated by \\((\text{Number of } H\rightarrow W^+W^- \text{events}) / \sqrt{\text{Number of background events}}\\).  
**The larger the significance value is, the better job you have done extracting the Higgs signal**.

## Channel

![](images/channel_13TeV.png)

The leptonic decay channels are shown here: dielectron \\(ee\\), dimuon \\(mm\\) and electron-muon \\(em\\).  
Decays to taus or hadrons are not considered in Histogram Analyser.

Histogram Analyser showing just simulated data, displays three leptonic channels.  Histogram Analyser showing simulated and real data, displays just the electron-muon channel, so this histogram is not displayed.

## Reconstructed Dilepton Mass [GeV]

This histogram displays the mass reconstructed from the two leptons in the final state.

![](images/DiLeptonMassNoCuts_13TeV.png)

With no cuts, this peaks at 90 GeV, due the huge [\\(Z\\) boson](http://pdg.lbl.gov/2012/listings/rpp2012-list-z-boson.pdf) contribution.

![](images/MassCutLess75_13TeV.png)  
![](images/NumbersMassCutLess75_13TeV.png)

We can remove a large number of \\(Z\\) boson events by selecting **Reconstructed Dilepton Mass** to be less than 75 GeV, whilst hardly touching our Higgs signal.  
The \\(H\rightarrow W^+W^-\\) sample significance increases from 0.046 to 0.250 with this cut.  
It is thus a useful quantity to use to reduce the huge \\(Z\\) boson background.

## Number of Jets

Number of jets found in the event.

![](images/2plusJets_13TeV.png)

![](images/Nevents2plusJets_13TeV.png)

When selecting two or more jets we see that the \\(Z\\) boson contribution decreases (from 7281608 to 1527242) and the \\(t\bar{t}\\) contribution becomes more important.

Selecting two or more jets, the ratio of ttbar to \\(Z\\) events increases from 49730/7281608 = 0.0007 to 36958/1527242 = 0.02 and the green ttbar contribution is now noticeable in the histograms.

Top-quark pair production leads to \\(WW\\)+jets final states.

## Are Jets b-tagged?

Jets originating from \\(b\\)-quarks are identified and labelled, or **tagged**, using so-called b-tagging algorithms.

![](images/Btag_13TeV.png)   
![](images/BtaggedYes_13TeV.png)  
![](images/nEventsBtagged_13TeV.png)

\\(b\\)-tagged jets are expected in top quark decays, but not in leptonic \\(W\\) or \\(Z\\) boson decays.

Selecting 'Are Jets b-tagged' as yes, the ratio of ttbar to \\(Z\\) events increases from 49730/7281608 = 0.0007 to 44532/169454 = 0.26 and the green ttbar contribution is now noticeable in the histograms.

## Missing Transverse Momentum (MET) [GeV]

In the LHC, the initial energy of the colliding partons (quarks or gluons) along the beam axis is not known.  
This is due to the energy of each proton being shared and constantly exchanged between its constituents.

However, the initial momentum of particles travelling transverse to the beam axis is zero.  
Therefore, any net momentum in the transverse direction indicates missing transverse momentum.

Missing transverse momentum is used to infer the presence of non-detectable particles such as the neutrino.  It is also expected to be a signature of many predicted physics events beyond the Standard Model, for example, the lightest [supersymmetric](http://home.cern/scientists/updates/2013/10/supersymmetry-searches-atlas) particle.

The standard abbreviation for missing transverse momentum is MET, for historical reasons.

![](images/MET100_13TeV.png)  
![](images/NeventsMET100_13TeV.png)

\\(Z\\) boson decays to charged leptons do not have any neutrinos in the final state while the other processes do.  
That is why requiring missing transverse momentum removes \\(Z\\) boson events.

Select missing transverse momentum and watch how the ratio of \\(WW\\) and ttbar to \\(Z\\) events changes.

## Total Lepton Transverse Momentum [GeV]

This is the [vectorial sum](https://en.wikipedia.org/wiki/Euclidean_vector#Addition_and_subtraction) of the transverse momenta of the observed charged leptons.

![](images/PTZ_13TeV.png)

For \\(Z\\) boson events, total lepton transverse momentum peaks at zero since the transverse momenta of both leptons cancel each other.

![](images/PTttbar_13TeV.png)

![](images/PTWW_13TeV.png)  
![](images/PTHWW_13TeV.png)

For the other processes this cancellation is not as pronounced.  
Their distributions peak at between 30 and 80 GeV.

## Opening Angle Between Leptons \\([\phi]\\)

![](images/OpeningAngleLeptons.jpg)

This is the opening angle, measured in phi \\(𝜙\\), between the two leptons.  
The azimuthal angle \\(\phi\\) is measured from the \\(x\\)-axis, around the beam.

In the event display above, two lepton tracks are displayed in red and the opening angle between the two leptons is marked in blue.

![](images/OpeningAngleLeptonsZ_13TeV.png)
![](images/OpeningAngleLeptonsWWttbar_13TeV.png)
![](images/OpeningAngleLeptonsHWW_13TeV.png)

If the leptons are emitted back-to-back, this is displayed on the histogram as 180 degrees.  
\\(H\rightarrow W^+W^-\\) events show a peak at low values in contrast to all other processes.

## Opening Angle Between MET and Leptons \\([\phi]\\)

This is the opening angle, measured in phi \\(𝜙\\), between the missing transverse momentum \\(MET\\) and the two leptons.

![](images/OpeningAngleMETleptoms.jpg)

In the event display above, missing transverse energy is displayed by the dotted yellow line.  The midline between the two lepton tracks (the direction of the vectorial sum of their transverse momenta) is represented by the dotted red line. The opening angle between the MET and leptons is shown in yellow.

Events with \\(t\bar t\\) and \\(Z\\) show a relatively flat distribution in this variable whereas \\(H\rightarrow W^+W^-\\) and \\(WW\\) peak at large values.

This is a useful discriminant to remove background events.

## Recap: Should significance be maximized or minimized?

Maximized.

# Navigation

Go to the [previous section]({{< ref "/13TeVDocDataAndSimulatedData" >}} "Histogram Analyser (simulation only)"), the [next section]({{< ref "/13TeVDocHistoAnalyserSimData" >}} "Histogram Analyser (simulation + data)") or jump back to the [summary page]({{< ref "/13TeVDocDataVisualisation" >}} "Summary page").