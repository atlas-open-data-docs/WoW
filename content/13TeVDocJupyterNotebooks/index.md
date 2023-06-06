---
title: "Jupyter Notebooks"
date: 2020-11-23T04:51:13+01:00
draft: false
hideLastModified: true
keepImageRatio: false
showInMenu: false
---

# 13 TeV ATLAS Open Data Jupyter Notebooks

The release of the 13 TeV ATLAS Open Data is accompanied by a set of Jupyter notebooks that allow data analysis to be performed directly in a web browser by integrating the ROOT framework with the [Jupyter notebook](https://jupyter.org/) technology, a combination called "ROOTbook". **Also, multiple ROOT-independent examples are in place**.

Several notebooks with analysis examples and an interface to launch the framework mentioned above, are available using [SWAN](https://swan.web.cern.ch/) (Service for Web based ANalysis) and [Binder](https://mybinder.org) executable platforms.

<CENTER>
<hr>

| <h2><b>Visualisation</b></h2> | <h2><b>Code and Run</b></h2> |
| :---:        |          :---: |
| [![nbviewer](images/Jupyter-logo.jpg)](https://nbviewer.jupyter.org/github/atlas-outreach-data-tools/notebooks-collection-opendata/tree/master/) | [![GitHub](images/GitHub-logo.png)](https://github.com/atlas-outreach-data-tools/notebooks-collection-opendata) |
| Take a look at the notebooks in NBviewer | Check, clone and run the code from GitHub |
<hr>

## Go and execute the notebooks now!
### Pick one of the two cloud computing services
<iframe src="http://opendata.atlas.cern/ROOT_execute/ROOTBooks_execute_mainframe.html" height="720px" width="100%" style="padding: 0% 0% 0% 0%;" frameborder="0"></iframe>
</br>
<hr>
</CENTER>

# Notebooks with analysis examples

A simple analysis example of a **search for the Higgs boson in the Higgs into two photons decay channel** is prepared. The analysis example is written in *both C++ and Python* languages with Jupyter notebook and a ROOT kernel and PyROOT extension, and these notebooks are available under this [Github link](https://github.com/atlas-outreach-data-tools/notebooks-collection-opendata).

![](images/Hyy-cpp.png)

![](images/Hyy-python.png)


The analysis example implements a simplified selection criteria for single Higgs boson events decaying to a couple of photons:

+ Diphoton trigger is satisfied;
+ Exactly two photons with transverse energy E{{< rawhtml >}}<sub>T</sub> >{{< /rawhtml >}} 35 and 25 GeV, respectively;
+ Leading and subleading photon candidates are respectively required to have E{{< rawhtml >}}<sub>T</sub>{{< /rawhtml >}} / m{{< rawhtml >}}<sub>yy</sub>{{< /rawhtml >}} > 0.35 and 0.25;
+ Diphoton invariant mass m{{< rawhtml >}}<sub>yy</sub>{{< /rawhtml >}} between 105 GeV and 160 GeV.

The background is estimated from data, without the use of MC simulation, by fitting the diphoton invariant-mass distribution in a range (105 GeV <  m{{< rawhtml >}}<sub>yy</sub>{{< /rawhtml >}} < 160 GeV) with a [third-order polynomial](https://en.wikipedia.org/wiki/Cubic_function) function with free shape and normalisation parameters. Signal MC simulations of the five main Higgs-boson production mechanisms (ggF, VBF, WH, ZH, tttH) are used to model the shape of the invariant mass of the signal, modelled as a [Gaussian](https://en.wikipedia.org/wiki/Normal_distribution) function.

The final diphoton invariant-mass spectrum in the selected diphoton events is shown below. The solid red curve shows the fitted signal-plus-background model when the Higgs boson mass is constrained to be 125 GeV. The background component of the fit is shown with the dotted blue curve. The signal component of the fit is shown with a solid black curve.

![](images/fig_12b.png)

# Jupyter notebooks with ROOT and C++ framework interface

An interface to the [C++ analysis framework](../frameworks/cpp.md), written in *both C++ and Python* languages with Jupyter notebook and a ROOT kernel and PyROOT extension, is prepared and available under this [Github link](https://github.com/atlas-outreach-data-tools/demos-framework-software-notebooks).

![](images/demo13-cpp.png)

![](images/demo13-python.png)

From these two interfaces, the C++ based analysis framework for the 13 TeV ATLAS Open Data analysis can be executed online using the cloud computing services such as [SWAN](https://swan.web.cern.ch/) and [Binder](https://swan.web.cern.ch/) executable platforms.

# Navigation
Go to the next [section]({{< ref "/8TevDocHistoAnimation" >}} "Histogram animation") or jump back to the [summary page]({{< ref "/13TeVDocOverview" >}} "Summary page").