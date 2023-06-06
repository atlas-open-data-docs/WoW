---
title: "Example of physics analysis: the case of a search for BSM Z' → tt in the single-lepton boosted final state"
date: 2023-05-31T04:51:13+01:00
draft: false
hideLastModified: true
keepImageRatio: false
showInMenu: false
---

Despite the spectacular phenomenological and experimental success of the SM, searches for new physics phenomena at the LHC are constantly ongoing. As an example, with a mass close to the scale of electroweak symmetry breaking, the top quark, besides having a large coupling to the SM Higgs boson, is predicted to have large couplings to new particles hypothesised in many BSM models.

In the following, we focus on implementing the selection criteria of a search for new heavy particles that decay into top-quark pairs in events containing a single charged lepton, large-R jets and missing transverse momentum. A particular benchmark model chosen for this search produces a new gauge boson Z' with a mass of 1 TeV and width of 10 GeV that decays into a tt-pair

In order to identify these events, one needs to apply the standard object-selection criteria (defined in "Reconstructed physics objects"), with a stricter lepton pT requirement and tight lepton identification criteria, and an event-selection criteria defined as:

{{< rawhtml >}}
<CENTER>
<img src="images/SLB.png" width="800" />
</CENTER>
{{< /rawhtml >}}

At the end, one is able to compare data and MC prediction for the distribution of e.g. the approximate mass of the tt system, as seen below. The benchmark 1 TeV Z' model is overlaid, clearly showing the different kinematic properties of this particular BSM prediction.

{{< rawhtml >}}
<CENTER>
<img src="images/fig_11h.png" width="600" />
</CENTER>
{{< /rawhtml >}}

# Navigation
Go to the [previous example]({{< ref "/13TeVDocZtotautauLep" >}} "Z boson decaying into two tau leptons 13 TeV"), the [next example]({{< ref "/13TeVDocHtoGammaGammaChannel" >}} "Higgs to gamma gamma channel") or jump back to the [summary page for the analysis examples]({{< ref "/13TeVDocAnalysisExamples" >}} "Summary page") or the [general summary page]({{< ref "/13TeVDocOverview" >}} "Summary page").