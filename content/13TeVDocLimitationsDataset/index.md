---
title: "Limitations of the released 13 TeV Open Datasets"
date: 2023-06-21T04:51:13+01:00
draft: false
hideLastModified: true
keepImageRatio: false
showInMenu: false
---

An important aspect of the 13 TeV ATLAS Open Data is that it is prepared specifically for educational purposes. To this end, precision has been traded for simplicity of use. The simplifications are:

- Scale factors implementing corrections for different object efficiencies are calculated using the preselection cuts. This selection does not have to coincide with the actual object selection defined by the user; therefore, discrepancies may arise due to non-matching object definitions.

- The per-jet b-tagging scale factor (scaleFactor_BTAG) is computed for a specific working point given a specific b-tagging algorithm (MV2c10) with a 70% b-jet efficiency. In case a different operating point for the MV2c10 b-tagging algorithm is specified, this introduces a potential mismatch between data and MC simulation.

- No data-driven estimation of the multijet background is provided, and the contributing effects of fake or non-prompt leptons may be countered using strict object definitions such as lepton identification, isolation and transverse momentum requirements. However, any residual disagreement might be understood as a sign that the multijet contribution to the electron and muon channels are not taken into account. 

- In order to provide ground for systematic-uncertainty estimation studies, but reduce large complexities, only a simplified single-component systematic-uncertainty estimate related to object transverse-momentum reconstruction is included in the datasets.

- The current content does not support the creation of unfolded distributions or searches for signals that are not supported by signal datasets made available by the ATLAS Collaboration.

# Navigation

Go to the [previous section]({{< ref "/13TeVDocGenerCapab" >}} "General capabilities of the released 13 TeV Open Datasets"), the [next section]({{< ref "/13TeVDocEvolOfData" >}} "Evolution of the ATLAS Open Data from the 8 TeV release (2016) to the 13 TeV release (2020)") or jump back to the [summary page]({{< ref "/13TeVDocDatasetOverview" >}} "Summary page").