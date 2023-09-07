---
title: "Histogram Analyser (rare top processes)"
date: 2023-05-23T04:51:13+01:00
draft: false
hideLastModified: true
keepImageRatio: false
showInMenu: false
---

# \\(t\bar t Z\\) - simulated + real data

Physicists use **cuts** to select events of interest.  Cuts preferentially remove the unwanted processes (background) but leave as much as possible of the desired process (signal).  It is useful to have a good understanding of the physics processes involved when applying cuts.

We have created another Histogram Analyser, to help visualise rare top-quark data. This Histogram Analyser searches for rare top-quark processes. Data are shown by the black dots, with error bars.

The three main processes are \\(t\bar t Z\\), \\(t\bar t\\) and \\(Z\\).

This Histogram Analyser also includes minor backgrounds, labelled as 'Other' in red. Minor backgrounds are required for data to match the total simulation. 'Other' includes single top production, \\(WZ\\) and \\(ZZ\\) diboson production and \\(t\bar t W\\).

Each process is represented by a different colour in Histogram Analyser.

## Make cuts using your cursor.

Use the cursor to select a specific range in one of the histograms.
The selected ranges will be coloured, whilst non-selected ranges will be greyed out.  When you make cuts on a variable the relative contributions of the four processes will change.

**To clear your selection on a specific histogram click on the white background within the histogram area. **

**To clear all your selections, reload your page** 

## The histograms explained

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
    <td valign="bottom">Number of b-tagged Jets</td>
    <td valign="bottom">Total Lepton Transverse Momentum</td>
    <td valign="bottom">Missing Transverse Momentum (MET)</td>
  </tr>
  <tr>
    <td><div id="hist4" title="Number of b-tagged Jets (N(BJets)): number of b-tagged jets in the event."></div></td>
    <td><div id="hist5" title="Total Lepton Transverse Momentum (PT(ll)): this is the vectorial sum of the transverse momenta of the observed charged leptons."></div></td>
    <td><div id="hist6" title="Missing Transverse Momentum (MET) : MET is used to infer the presence of non-detectable particles such as the neutrino."></div></td>
  </tr>
  <tr style="height: 50px">
    <td valign="bottom">Separation Between Leptons</td>
    <td valign="bottom">Opening Angle Between Leptons</td>
    <td valign="bottom">Expected Number of Events for 10/fb</td>
  </tr>
  <tr>
    <td><div id="hist7" title="Separation Between Leptons (DeltaR(l,l)): this is the angular distance separation between the two leptons."></div></td>
    <td><div id="hist8" title="Opening Angle Between Leptons (DeltaPhi(l,l)): this is the angle, measured in phi (&phi;), between the two leptons. The azimuthal angle &phi; is measured from the x-axis, around the beam."></div></td>
    <td><div id="hist9" title="Expected Number of Events for 10/fb: the number of events expected to be detected, reconstructed and recorded by ATLAS for 10 inverse femtobarn of data.  Numbers taken from simulation. The significance of the ttZ quantifies how 'significant' the ttZ sample is with respect to the background. (Number of ttZ events)/Number of background events. The larger the significance value is, the better job you have done extracting the ttZ signal."></div></td>
  </table>
</div>

    <script charset="utf-8" type="text/javascript" src="interactive/d3.js"></script>
    <script charset="utf-8" type="text/javascript" src="interactive/crossfilter.js"></script>
    <script charset="utf-8" type="text/javascript" src="interactive/dc.js"></script>
    <script charset="utf-8" type="text/javascript">

      d3.csv("interactive/13TeV_ttZ.csv", function(error, events) {

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
             return [0,0,0,0];
          }
          
          var colorScale = d3.scale.ordinal().range(["#1C5EA8","#F66A00","#2A9000","#C31318"]);
          var ndx                       = crossfilter(events),
              njetDimension             = ndx.dimension(function(d) {return +d.NJets;}),
              typeDimension             = ndx.dimension(function(d) {return +d.type;}),
              METDimension              = ndx.dimension(function(d) {return +Math.floor(d.MET*0.1)*10;}),
              LepDeltaRDimension        = ndx.dimension(function(d) {return +Math.floor(d.LepDeltaR*2)*0.5;}),
              SumLepPtDimension         = ndx.dimension(function(d) {return +Math.floor(d.SumLepPt*0.1)*10;}),
              ZWindowDimension          = ndx.dimension(function(d) {return +Math.floor(d.Mll*0.2)*5;}),
              ChannelDimension          = ndx.dimension(function(d) {return +d.Channel;}),
	      DeltaPhiDimension         = ndx.dimension(function(d) {return +Math.floor(d.LepDeltaPhi*0.31813*18)*10;})
              nbjetDimension            = ndx.dimension(function(d) {return +d.NBJets})
              NJetGroup                 = njetDimension.group().reduce(add_by_channel,remove_by_channel, initial),
              LepDeltaRGroup            = LepDeltaRDimension.group().reduce(add_by_channel,remove_by_channel, initial),
              SumLepPtGroup             = SumLepPtDimension.group().reduce(add_by_channel,remove_by_channel, initial),
              ZWindowGroup              = ZWindowDimension.group().reduce(add_by_channel,remove_by_channel, initial),
              ChannelGroup              = ChannelDimension.group().reduce(add_by_channel,remove_by_channel, initial),
              NBJetGroup                = nbjetDimension.group().reduce(add_by_channel,remove_by_channel, initial),
              compGroup                 = typeDimension.group().reduceSum(function(d) {return +d.weight;}),
              mcstatGroup               = typeDimension.group().reduceCount(),
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
                      if (v.type !=0 && v.type != 1) p.bkg -= v.weight;
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
              if (i == "1") return "ttZ";
              if (i == "2") return "ttbar";
              if (i == "3") return "Z";
	      if (i == "4") return "Other";
              if (i == "0") return "data";
	      return "default"
           }
          
           function make_barchart( location, domain, label, dimension, group, centered = false ){
             var chart = dc.barChart(location)
             var endwid = 5 
             chart.width(270)
                  .height(250)
                  .x(d3.scale.linear().domain(domain))
                  .margins({left: 50, top: 10, right: 10, bottom: 35})
                  .brushOn(true)
                  .elasticY(true)
                  .xAxisLabel(label)
                  .yAxisLabel("Events")
                  .yAxisPadding("20%")
                  .clipPadding(10)
                  .dimension(dimension)
                  .group(group, "ttZ", sel_stack('1'))
                  .stack(group, "ttbar",       sel_stack('2'))
                  .stack(group, "Z",           sel_stack('3'))
		  .stack(group, "Other",       sel_stack('4'))
               .on('renderlet', function(chart) {
                 chart.selectAll('.x-axis-label').attr('transform', 'translate(270,238)').attr('text-anchor', 'end');
                 chart.selectAll('.y-axis-label').attr('transform', 'rotate(-90), translate(-30,12)');
                 var barWidth = chart.select('rect.bar').attr('width');
                 if (centered){
                     barWidth = 0
                 }
                 var bar = chart.g().select('g.chart-body').selectAll('g.errorbar')
                 .data(group.all())
                 .enter()
                   .append('g')
                   .attr('class', 'errorbar');
                 bar
                   .append('line')
                   .attr({
                     'class' : 'errorwidth',
                     'stroke-width': 1,
                     stroke: 'black',
                     x1: function(d) { return chart.x()(d.key)+barWidth*0.5;},
                     x2: function(d) { return chart.x()(d.key)+barWidth*0.5;},
                     y1: function(d) { return chart.y()(d.value[0] + Math.sqrt(d.value[0])); },
                     y2: function(d) { return chart.y()(d.value[0] - Math.sqrt(d.value[0])); }
                   });
                 bar.append('line')
                   .attr({
                     'class' : 'lowererror',
                     'stroke-width': 1,
                     stroke: 'black',
                     x1: function(d) { return chart.x()(d.key)+barWidth*0.5 - endwid;},
                     x2: function(d) { return chart.x()(d.key)+barWidth*0.5 + endwid; },
                     y1: function(d) { return chart.y()(d.value[0] - Math.sqrt(d.value[0]));},
                     y2: function(d) { return chart.y()(d.value[0] - Math.sqrt(d.value[0]));}
                   });
                 bar.append('line')
                   .attr({
                     'class' : 'uppererror',
                     'stroke-width': 1,
                     stroke: 'black',
                     x1: function(d) { return chart.x()(d.key)+barWidth*0.5 - endwid;},
                     x2: function(d) { return chart.x()(d.key)+barWidth*0.5 + endwid;},
                     y1: function(d) { return chart.y()(d.value[0] + Math.sqrt(d.value[0]));},
                     y2: function(d) { return chart.y()(d.value[0] + Math.sqrt(d.value[0]));}
                   });
                 bar.append('circle')
                   .attr({
                     stroke: 'black',
                     cx: function(d) { return chart.x()(d.key)+barWidth*0.5;},
                     cy: function(d) { return chart.y()(d.value[0]);},
                     r: function(d)  { return 2;}
                   });
               })
                   .on('pretransition', function(chart) {
                     var barWidth = chart.select('rect.bar').attr('width');
                     if (centered){
                         barWidth = 0
                     }
                     var bar = chart.g().select('g.chart-body').selectAll('g.errorbar')
                               .data(group.all())
                               .transition()
                               .duration(750)
                     
                     bar.select('circle').attr({cy: function(d) { return chart.y()(d.value[0]);}});
                     bar.select('line.errorwidth')
                       .attr({
                         y1: function(d) { return chart.y()(d.value[0] + Math.sqrt(d.value[0])); },
                         y2: function(d) { return chart.y()(d.value[0] - Math.sqrt(d.value[0])); }
                       });
                     bar.select('line.lowererror')
                       .attr({
                         y1: function(d) { return chart.y()(d.value[0] - Math.sqrt(d.value[0]));},
                         y2: function(d) { return chart.y()(d.value[0] - Math.sqrt(d.value[0]));}
                       });
                     bar.select('line.uppererror')
                       .attr({
                         y1: function(d) { return chart.y()(d.value[0] + Math.sqrt(d.value[0]));},
                         y2: function(d) { return chart.y()(d.value[0] + Math.sqrt(d.value[0]));}
                       });
                   })
             return chart
          }
                                            

	  var channelChart = make_barchart("#hist1", [0,3], "Channel", ChannelDimension, ChannelGroup)
          channelChart.xAxis().tickFormat(function(d){if(d == 0.5){return "ee"}; if(d == 1.5){return "μμ"};if(d == 2.5){return "eμ";}});

          var ZWindowChart = make_barchart("#hist2", [0,105], "M(ll) [GeV]", ZWindowDimension, ZWindowGroup)
          ZWindowChart.xUnits(dc.units.fp.precision(5));

          var njetChart = make_barchart("#hist3", [-0.5,10], "N(Jets)", njetDimension, NJetGroup, true)
          njetChart.centerBar(true)
          njetChart.legend(dc.legend().x(200).y(10).itemHeight(20).gap(5))


          var METChart     = make_barchart("#hist6", [0,200], "MET [GeV]", METDimension, METGroup)
          METChart.xUnits(dc.units.fp.precision(10));

          var LepDeltaRChart    = make_barchart("#hist7", [0, 5],"DeltaR(l,l)" ,LepDeltaRDimension, LepDeltaRGroup)
          LepDeltaRChart.xUnits(dc.units.fp.precision(0.5));

          var deltaphiChart = make_barchart("#hist8", [0,180], "DeltaPhi(l,l) [deg]", DeltaPhiDimension, DeltaPhiGroup)
          deltaphiChart.xUnits(dc.units.fp.precision(10));

          var sumlepptChart = make_barchart("#hist5", [0,200], "PT(ll) [GeV]", SumLepPtDimension, SumLepPtGroup)
          sumlepptChart.xUnits(dc.units.fp.precision(10));

          var nbjetChart = make_barchart("#hist4", [-0.5,10], "N(BJets)", nbjetDimension, NBJetGroup, true)
	  nbjetChart.centerBar(true)

          function remove_data(source_group) {
              return {
                  all:function () {
                      return source_group.all().filter(function(d) {
                          return d.key != 0;
                      });
                  }
              };
          }


          var mcCompChart = dc.rowChart("#hist9")
          mcCompChart.width(270).height(250)
                     .margins({left: 5, top: 10, right: 10, bottom: 57})
                     .x(d3.scale.ordinal().domain([1,2,3,4]))
                     .dimension(typeDimension)
                     .group(remove_data(compGroup))
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
      
      function AddXAxis(chartToUpdate, displayText) {
          chartToUpdate.svg()
              .append("text")
              .attr("class", "x-axis-label")
              .attr("text-anchor", "end")
              .attr("x", chartToUpdate.width())
              .attr("y", chartToUpdate.height()-22)
              .text(displayText);
      }

      /*AddXAxis(mcCompChart, "Expected Number of Events for 10/fb");*/      
      });

    </script>

  </body>
</html>
{{< /rawhtml >}}

You can select just the \\(t\bar t Z\\) events by clicking on the \\(t\bar t Z\\) in the 'Expected Number of Events' histogram.

## Expected Number of Events for 10/fb

This histogram shows the number of events expected to be detected, reconstructed and recorded by ATLAS for 10 inverse femtobarn (10/fb) of data.
Ten inverse femtobarns correspond to approximately 1000 trillion proton-proton collisions.

The expected number of events reconstructed and recorded by ATLAS is different to the number of events produced.
Some events will not be reconstructed due to the way the detector is constructed, the resolution of the sub-detectors, reconstruction efficiency and other inefficiencies.

With no cuts, we have 75 \\(t\bar t Z\\) events, with many more background events.  The majority of the background is \\(Z\\) boson production.

The **significance** of the \\(t\bar t Z\\) events quantifies how "significant" the \\(t\bar t Z\\) sample is with respect to the background.  It is calculated by \\((\text{Number of } t\bar t Z \text{events}) / \sqrt{\text{Number of background events}}\\).
**The larger the significance value is, the better job you have done extracting the \(t\bar t Z\) signal**.

## Channel

The leptonic decay channels are shown here: dielectron \\(ee\\), dimuon \\(\mu\mu\\) and electron-muon \\(e\mu\\).
Decays to taus or hadrons are not considered in Histogram Analyser.

## Reconstructed Dilepton Mass [GeV]

This histogram displays the mass reconstructed from the two leptons in the final state.

With no cuts, this peaks at 90 GeV, due the huge [\\(Z\\) boson](http://pdg.lbl.gov/2012/listings/rpp2012-list-z-boson.pdf) contribution.

![](images/MassCut80-100.png)
![](images/NumbersMassCut80-100.png)

We can remove a large number of \\(t\bar t\\) events by selecting **Reconstructed Dilepton Mass** to be between 80 and 100 GeV, whilst hardly touching our \\(t\bar t Z\\) signal.
The \\(t\bar t Z\\) sample significance increases with this cut.
It is thus a useful quantity to use to reduce the \\(t\bar t\\) background.

You will notice that both the data points and the simulated Monte Carlo distributions change. The data and simulated Monte Carlo are not exactly the same, but the general agreement is very good. This shows that these processes are well understood and well modelled.

## Number of Jets

Number of jets found in the event. Events with 0, 1 or 2 jets haven't been saved to make the file smaller and thus the Histogram Analyser will run quicker.

![](images/6plusJets.png)
![](images/Nevents6plusJets.png)

When selecting six or more jets we see that the background contributions decrease and the \\(t\bar{t}Z\\) contribution becomes more important. The blue \\(t\bar t Z\\) contribution is now more noticeable in the histograms.

## Number of b-tagged Jets?

Jets originating from \\(b\\)-quarks are identified and labelled, or **tagged**, using so-called b-tagging algorithms.

![](images/2plusbJets.png)
![](images/Nevents2plusbJets.png)

\\(b\\)-tagged jets are expected in top quark decays, but not in leptonic \\(W\\) or \\(Z\\) boson decays.

Selecting 'Number of b-tagged Jets' at least 2, the \\(t\bar t Z\\) contribution is now more noticeable in the histograms.

## Total Lepton Transverse Momentum [GeV]

This is the [vectorial sum](https://en.wikipedia.org/wiki/Euclidean_vector#Addition_and_subtraction) of the transverse momenta of the observed charged leptons.

![](images/PTZ.png)
![](images/PTttbar.png)
![](images/PTttZ.png)

For \\(Z\\) boson events, total lepton transverse momentum peaks at low values since the transverse momenta of both leptons mostly cancel each other.
For the other processes this cancellation is not as pronounced.
Their distributions peak at between 60 and 90 GeV.

## Missing Transverse Momentum (MET) [GeV]

In the LHC, the initial energy of the colliding partons (quarks or gluons) along the beam axis is not known.
This is due to the energy of each proton being shared and constantly exchanged between its constituents.

However, the initial momentum of particles travelling transverse to the beam axis is zero.
Therefore, any net momentum in the transverse direction indicates missing transverse momentum.

Missing transverse momentum is used to infer the presence of non-detectable particles such as the neutrino.
It is also expected to be a signature of many predicted physics events beyond the Standard Model, for example the lightest [supersymmetric](http://home.cern/scientists/updates/2013/10/supersymmetry-searches-atlas) particle.

The standard abbreviation for missing transverse momentum is MET, for historical reasons.

\\(t\bar t\\) decays to two leptons have two neutrinos in the final state while \\(Z\\) boson decays to charged leptons do not.
That is why requiring low missing transverse momentum removes \\(t\bar t\\) events.

In combination with other cuts, select missing transverse momentum and watch how the ratio of \\(t\bar t Z\\) and \\(t\bar t\\) to \\(Z\\) events changes.

## Opening Angle Between Leptons \\([\phi]\\)

![](images/OpeningAngleLeptons.jpg)

This is the opening angle, measured in phi \\(\phi\\), between the two leptons.
The azimuthal angle \\(\phi\\) is measured from the \\(x\\)-axis, around the beam.

In the event display above, two lepton tracks are displayed in red and the opening angle between the two leptons is marked in blue.

![](images/OpeningAngleLeptonsZ.png)
![](images/OpeningAngleLeptonsttbar.png)
![](images/OpeningAngleLeptonsttZ.png)

If the leptons are emitted back-to-back, this is displayed on the histogram as 180 degrees.
\\(Z\\) events show a peak at high values in contrast to all other processes.


## Separation Between Leptons

Separation, \\((\Delta R)\\), is calculated using the following equation:

\\((\Delta R)^2 = (\Delta\phi)^2 + (\Delta\eta)^2\\)

where \\(\phi\\) is the azimuthal angle between leptons and \\(\eta\\) is the [pseudorapidity](http://opendata.atlas.cern/release/2020/documentation/atlas/GLOSSARY.html). 

\\(t\bar t Z\\) events show a peak at lower values than other processes.



## Your challenge

Make some selections to separate the \\(t\bar t Z\\) signal from the background.

Can you increase the significance to over 0.9?

Below is an event display, where a \\(t\bar t Z\\) candidate has been identified decaying into 2 muons and a number of jets.

![](images/ttZ_3l_event.png)









