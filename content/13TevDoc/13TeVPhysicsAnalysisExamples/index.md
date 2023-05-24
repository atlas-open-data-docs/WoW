---
title: "13 TeV Physics Analysis Examples"
date: 2023-05-23T04:51:13+01:00
draft: false
hideLastModified: true
keepImageRatio: false
showInMenu: false
---

# 13 TeV ATLAS Open Data physics analysis examples

The general aim of the 13 TeV ATLAS Open Data and tools released is to provide a straightforward interface to replicate the procedures used by high-energy-physics researchers and enable users to experience the analysis of particle physics data in educational environments. Therefore, it is of significant interest to check the correct modelling of several SM process by the 13 TeV ATLAS Open Data MC simulation.

Hence, **twelve examples of physics analysis** (as reported in official release document [ATL-OREACH-PUB-2020-001](https://cds.cern.ch/record/2707171)) using the 13 TeV ATLAS Open Data inspired by and following as closely as possible the procedures and selections taken in already published ATLAS Collaboration physics results are introduced:

- **four high statistics** analyses with a selection of:
    - W-boson leptonic-decay events,
    - single-Z-boson events, where the Z boson decays into an electron–positron or muon–antimuon pair,
    - single-Z-boson events, where the Z boson decays into a tau-lepton pair with a hadronically decaying tau-lepton accompanied by a tau-lepton that decays leptonically,
    - top-quark pairs in the single-lepton final state. Each of these analyses have sufficiently high event yields to study the SM processes in detail, and are intended to show the general good agreement between the released 13 TeV data and MC prediction. They also enable the study of SM observables, such as the mass of the W and Z bosons, and that of the top quark.

- **three low statistics** analyses with a selection of single top-quarks produced in the single-lepton t-channel, diboson WZ events produced in the tri-lepton final state and diboson ZZ events produced in the fully-leptonic final states. These analyses illustrate the statistical limitations of the released dataset given the low production cross-section of the rare processes, where the variations between data and MC prediction are attributed to sizeable statistical fluctuations.

- **three SM Higgs boson** analyses with a selection of events in the H → WW, H &rarr ZZ and H &rarr $\gamma \gamma$  decay channels, which serve as examples to implement simplified analyses in different final-state scenarios and "re-discover" the production of the SM Higgs boson.

- **two BSM physics** analyses searching for new hypothetical particles: one implementing the selection criteria of a search for direct production of superpartners of SM leptons, and the second one implementing the selection criteria of a search for new heavy particles that decay into top-quark pairs, provided to implement a simplified analysis for searching for new physics using different physics objects.