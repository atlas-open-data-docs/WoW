---
title: "Histogram Analyser (simulation + data)"
date: 2023-05-23T04:51:13+01:00
draft: false
hideLastModified: true
keepImageRatio: false
showInMenu: false
---

# Higgs to WW - simulated + real data

The second Histogram Analyser includes data. This is shown by the black dots, with error bars.

This second Histogram Analyser also includes minor backgrounds, labelled as 'Other' in purple. Minor backgrounds are required for data to match the total simulation. 'Other' includes single top production, \\(WZ\\) and \\(ZZ\\) diboson production, \\(W\\) boson production and \\(H \rightarrow ZZ^* \rightarrow \ell^+\ell^-\ell^+\ell^-\\) decay.

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
    <td valign="bottom">Transverse Mass</td>
    <td valign="bottom">Reconstructed Dilepton Mass</td>
    <td valign="bottom">Number of Jets</td>
  </tr>
  <tr>
    <td><div id="hist1" title="Transverse Mass:  transverse mass is analogous to invariant mass but neglects the longitudinal momenta of the decay products."></div></td>
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
    <td><div id="hist9" title="Expected Number of Events for 10/fb: the number of events expected to be detected, reconstructed and recorded by ATLAS for 10 inverse femtobarn of data.  Numbers taken from simulation. The significance of the H &rarr; WW events quantifies how 'significant' the Higgs sample is with respect to the background. (Number of H &rarr; WW events)/Number of background events. The larger the significance value is, the better job you have done extracting the Higgs signal."></div></td>
 </table>
</div>

    <script charset="utf-8" type="text/javascript" src="interactive/d3.js"></script>
    <script charset="utf-8" type="text/javascript" src="interactive/crossfilter.js"></script>
    <script charset="utf-8" type="text/javascript" src="interactive/dc.js"></script>
    <script charset="utf-8" type="text/javascript">

      d3.csv("interactive/13TeV_TransData.csv", function(error, events) {

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
             return [0,0,0,0,0];
          }
          
          var colorScale = d3.scale.ordinal().range(["#1C5EA8","#F66A00","#2A9000","#C31318","#9F58C2"]);
          var ndx                       = crossfilter(events),
              njetDimension             = ndx.dimension(function(d) {return +d.NJets;}),
              typeDimension             = ndx.dimension(function(d) {return +d.type;}),
              METDimension              = ndx.dimension(function(d) {return +Math.floor(d.MET*0.1)*10;}),
              DeltaPhiMETLLDimension    = ndx.dimension(function(d) {return +Math.floor(Math.abs(d.METLLDeltaPhi*0.31813*18))*10;}),
              SumLepPtDimension         = ndx.dimension(function(d) {return +Math.floor(d.SumLepPt*0.1)*10;}),
              ZWindowDimension          = ndx.dimension(function(d) {return +Math.floor(d.Mll*0.2)*5;}),
              TransMassDimension        = ndx.dimension(function(d) {return +Math.floor(d.TransMass*0.1)*10;}),
              DeltaPhiDimension         = ndx.dimension(function(d) {return +Math.floor(d.LepDeltaPhi*0.31813*18)*10;})
              BTagDimension             = ndx.dimension(function(d) {return +d.BTags})
              NJetGroup                 = njetDimension.group().reduce(add_by_channel,remove_by_channel, initial),
              DeltaPhiMETLLGroup        = DeltaPhiMETLLDimension.group().reduce(add_by_channel,remove_by_channel, initial),
              SumLepPtGroup             = SumLepPtDimension.group().reduce(add_by_channel,remove_by_channel, initial),
              ZWindowGroup              = ZWindowDimension.group().reduce(add_by_channel,remove_by_channel, initial),
              TransMassGroup            = TransMassDimension.group().reduce(add_by_channel,remove_by_channel, initial),
              BTagGroup                 = BTagDimension.group().reduce(add_by_channel,remove_by_channel, initial),
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
	      if (i == "5") return "Other";
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
                  .group(group, "H \u2192 WW", sel_stack('1'))
                  .stack(group, "WW",          sel_stack('2'))
                  .stack(group, "ttbar",       sel_stack('3'))
                  .stack(group, "Z",           sel_stack('4'))
		  .stack(group, "Other",       sel_stack('5'))
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
                                            

          var transMassChart = make_barchart("#hist1", [0,300], "Transverse Mass [GeV]", TransMassDimension, TransMassGroup)
          transMassChart.xUnits(dc.units.fp.precision(10));

          var ZWindowChart = make_barchart("#hist2", [0,105], "M(ll) [GeV]", ZWindowDimension, ZWindowGroup)
          ZWindowChart.xUnits(dc.units.fp.precision(5));

          var njetChart = make_barchart("#hist3", [-0.5,10], "N(Jets)", njetDimension, NJetGroup, true)
          njetChart.centerBar(true)
          njetChart.legend(dc.legend().x(200).y(10).itemHeight(20).gap(5))


          var METChart     = make_barchart("#hist6", [0,200], "MET [GeV]", METDimension, METGroup)
          METChart.xUnits(dc.units.fp.precision(10));

          var DeltaPhiMETLLChart    = make_barchart("#hist7", [0, 180],"DeltaPhi(MET,ll) [deg]" ,DeltaPhiMETLLDimension, DeltaPhiMETLLGroup)
          DeltaPhiMETLLChart.xUnits(dc.units.fp.precision(10));

          var deltaphiChart = make_barchart("#hist8", [0,180], "DeltaPhi(l,l) [deg]", DeltaPhiDimension, DeltaPhiGroup)
          deltaphiChart.xUnits(dc.units.fp.precision(10));

          var sumlepptChart = make_barchart("#hist5", [0,200], "PT(ll) [GeV]", SumLepPtDimension, SumLepPtGroup)
          sumlepptChart.xUnits(dc.units.fp.precision(10));

          var BTagChart = make_barchart("#hist4", [0,2.5], "BTag", BTagDimension, BTagGroup)
          BTagChart.xAxis().tickFormat(function(d){if(d == 0.5){return "no"}; if(d == 1.5){return "yes"}});
          BTagChart.xAxis().tickValues([0, 0.5,1,1.5,2]);

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

Here we will just be looking at the electron-muon channel. Before, we had 124 Higgs candidates (see **Events per Channel** histogram below), now we are looking at just 66 Higgs candidates (see **Expected Number of Events** histogram above). However, the \\(Z\\) background is much reduced, so that makes it a good choice.



![](images/HWWcandidates_13TeV.png)




The numbers shown in Number of Expected Events is calculated by the simulated Monte Carlo, as before.

We have also added a new histogram, transverse mass. Transverse mass is analogous to invariant mass, but neglects the longitudinal momenta of the decay products.

![](images/TransverseMass_13TeV.png)




Transverse mass, \\(m_T\\), is a useful quantity to define for use in particle physics as it is invariant under Lorentz boost along the z direction. In natural units it is:

\\(m_T^2 = m^2 + p_x^2 + p_y^2 = E^2 - p_z^2\\)

where the z-direction is along the beam pipe and so \\(p_x\\) and \\(p_y\\) are the momentum perpendicular to the beam pipe and \\(m\\) is the invariant mass.

In this study, transverse mass is defined as

\\(m_T = ((E_T^{ll} + E_T^{miss})^2 - | p_T^{ll} + E_T^{miss} |^2 ) ^{1/2} \\)

where
\\( E_T^{ll} = (|p_T^{ll}|^2 + m_{ll}^2 )^{1/2} \\)

If you select just the Higgs events by clicking on the \\(H \rightarrow WW\\) in 'Expected Number of Events' histogram, you will see the transverse mass of the Higgs. As expected, it peaks at the mass of the Higgs, 125 GeV.


![](images/TransverseMassHWW_13TeV.png)



Select events fewer than 2 jets by using your cursor to select N(Jets)<2. You will notice that both the data points and the simulated Monte Carlo distributions change. The data and simulated Monte Carlo are not exactly the same, but the general agreement is very good. This shows that these processes are well understood and well modelled.

![](images/Njets2DataMC_13TeV.png)




As before, make some selections to separate the Higgs boson signal from the background.

Can you increase the significance to over 0.6 ?

Below is an event display, where a Higgs candidate has been identified decaying into an electron and muon.




![](images/CandidateEvent1.jpg)

# Navigation

Go to the [previous section]({{< ref "/13TeVDocHistoAnalyserSim" >}} "Histogram Analyser simulation only"), the [next section]({{< ref "/13TeVDocSeperateSignals" >}} "Seperate signals") or jump back to the [summary page]({{< ref "/13TeVDocDataVisualisation" >}} "Summary page").