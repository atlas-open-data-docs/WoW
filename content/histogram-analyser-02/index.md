---
title: "App @13 TeV"
date: 2020-11-23T04:51:13+01:00
draft: false
hideLastModified: true
summaryImage: "images/handmade_event_display.png"
keepImageRatio: false
tags: ["Histograms", "Apps", "JavaScript"]
summary: "Histogram Analyser only simulated data @13 TeV"
showInMenu: false
---


# Higgs to WW - only simulated data

Physicists use **cuts** to select events of interest.  Cuts preferentially remove the unwanted processes (background) but leave as much as possible of the desired process (signal).
It is useful to have a good understanding of the physics processes involved when applying cuts.

We have created two Histogram Analysers, to help visualise the data. Both histogram analysers display four physics processes.

The four processes are $$H\rightarrow W^+W^-\, WW, t\bar t, Z$$  
These processes are discussed in the [dedicated documentation](http://opendata.atlas.cern/release/2020/documentation/visualization/the_display_histograms_13TeV.html). Each process is represented by a different colour in Histogram Analyser.

## Make cuts using your cursor.

* Use the cursor to select a specific range in one of the histograms.  
* The selected ranges will be coloured, whilst non-selected ranges will be greyed out.
* When you make cuts on a variable the relative contributions of the four processes will change.

**To clear your selection on a specific histogram click on the white background within the histogram area.**

&nbsp;

---
## **Higgs to WW - simulated data**
Histogram Analyser displays nine histograms.
* *The histograms can take about 30 seconds to load.*
* *Whilst loading you'll only see the histogram titles.*
* *Once loaded you'll see the histograms appear under their titles.*

{{< rawhtml >}}

<p align="center">
<iframe name="analyzer" style="overflow:hidden;height: 950px; width:100%"  src="https://atlas-opendata.web.cern.ch/release/2020/documentation/visualization/CrossFilter/13TeV_crossfilter.html" frameborder="0" allowfullscreen></iframe>
</p>

{{< /rawhtml >}}

---

# Follow this video for a complete explanation

{{< youtube X1PyNTUwffI >}}
---

### and to continue the exercise...
---

## ...follow the instructions about this app in its [dedicated documentation](http://opendata.atlas.cern/release/2020/documentation/visualization/histogram-analyser-2_13TeV.html)!

---

**Note**: This app does ***not*** re-scale well in mobile devices. Please, use it in a desktop computer or laptop for a complete experience.
