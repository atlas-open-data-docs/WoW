---
title: "Custom datasets ..."
date: 2020-06-10T21:51:13+01:00
draft: false
hideLastModified: true
summaryImage: "images/handmade_event_display.png"
keepImageRatio: false
tags: ["8 TeV", "Experiment","datasets"]
summary: "Others datasets & collections"
showInMenu: false
---
{{< rawhtml >}}
<script async src="https://unpkg.com/mermaid@8.2.3/dist/mermaid.min.js"></script>

<CENTER>
<img src="images/incognito-jets.png" width="76%" alt="incognito-jets">
</CENTER>

{{< /rawhtml >}}

# **... and their associated projects**

---

# **A Public Dataset For Teaching Jet Reconstruction**

### Motivation
* Public datasets generally focus on “high-level” objects
  * Jets, electrons, muons, etc
  * This makes perfect sense for general use for most education
* However, this isn’t sufficient for teaching about reconstruction
  * How and why do we use certain reconstruction techniques?
  * What are the trade-offs of using different types of detectors?
  * How does pileup impact object reconstruction?
* We propose a new dataset which can be used to teach jet reconstruction
  * Most important contents: topoclusters and tracks (per-vertex)
  * Sample: Pythia8 dijets, ∼100k events/slice =⇒ O(1M) events
  * Merge slices to one sample, flat in pT

### Examples of studies supported by such a dataset
* Small-R pileup studies:
  * How does jet multiplicity depend on pileup?
  * How can tracks be used to suppress pileup jets?
  * Why don’t we build jets from tracks instead of clusters?
* Large-R substructure studies:
  * How does the jet algorithm impact the event interpretation?
  * How does the jet algorithm impact the jet mass?
  * How does the jet algorithm impact pileup stability?
* Many other interesting educational studies are possible
  * Such a dataset would have a large variety of pedagogical uses!
  * Lots of possible extentions if this is well received

### Dataset overview
* The dataset is now ready
  * Ten files of 102.9k events each (total 1.029M events), total 21 GB
  * Each file is 343 bins with 300 events each, and is 2.1 GB
  * Also this is only MC, no data (more on this later)
* You are welcome to check out the dataset
  * One of the ten files is [here](https://cernbox.cern.ch/index.php/s/ieHsllIjTtJIHTo) (password is “JetReco”)
  * A pair of exercises are also available [here](https://cernbox.cern.ch/index.php/s/0ws6P5MkNVzZInL) (password is “JetReco”)
* Following slides contain:
  * Details on the dataset contents
  * Examples of what can be done with these files (from the exercises)
  * A discussion on choices made and possible follow-ups

## Details on the dataset contents

---

The [ATLAS Open Data](http://opendata.atlas.cern) ...

---

## Are you looking for the [13 TeV](../samples-13tev/) samples?
or maybe
## the [8 TeV](../samples-8tev/) samples?

---

## <a name="atlas-disclaimer">Disclaimer</a>
This dataset is provided by the ATLAS Collaboration only for educational purposes and is not suited for scientific publications.
* The [ATLAS Open Data](http://opendata.atlas.cern) are released under the [Creative Commons CC0 waiver](http://creativecommons.org/publicdomain/zero/1.0/).
* Neither ATLAS nor CERN endorses any works produced using these data, which is intended only for educational use.
* All data sets will have a unique [DOI](https://en.wikipedia.org/wiki/Digital_object_identifier) that you are requested to cite in any (non-scientific) applications or publications.
* Despite being processed, the high-level primary datasets remain complex, and selection criteria need to be applied in order to analyse them, requiring some understanding of particle physics and detector functioning.
* The large majority of the data cannot be viewed in simple data tables for spreadsheet-based analyses.

---
