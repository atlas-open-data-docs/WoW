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

### Dataset contents, high level
* This is the high-level overview of the contents
  * A detailed overview of each aspect is on the following slides
* General event-level information (NPV, etc)
* Tracks, with standard jet selections applied
* Clusters, with standard jet selections applied
* Truth particles, with standard jet selections applied
* Various types of reconstructed jets
  * All reconstructed jets can be rebuilt from the dataset
  * They are included to help the user get started and for validation
  
### Dataset contents, event-level info
* EventNumber [unsigned long long]
* RunNumber [unsigned long long]
  * Not very useful for MC, but useful in case data is added later
* EventWeight [float]
  * Complex quantity, described later, but it is the only weight needed
* mu average [float]
* mu actual [float]
  * The same as mu average in MC, but for data we may want both
* NPV [unsigned int]
  * Typical definition used for jet calibration: require two tracks
* Note that some common variables are NOT included
  * No mcChannelNumber as we merged several samples together here
  * No individual weights as it’s all stuck together into EventWeight
  * No pileup weight - not needed for MC only

### Dataset contents, tracks
* Jet reco in ATLAS applies some standard selections to tracks
  * pT > 500 MeV, good quality, etc
* These are also applied to the tracks in this dataset
* Vertex matching done using standard track-to-vertex association tools
* Tracks pt [vector<float>]
* Tracks eta [vector<float>]
* Tracks phi [vector<float>]
* Tracks m [vector<float>]
  * I checked, it’s always fixed to the pion mass as expected
  * ROOT compresses by factor of 2 compared to pt/eta/phi
  * Supports using the same commands regardless of the object type
* Tracks vtx [vector<int>]
  * User has to loop over tracks and identify “vertices” using these indices
  * Decided to do this to save space rather than storing vertices
  * int not unsigned as tracks not associated to a vertex have index -1

### Dataset contents, clusters
* Jet reco in ATLAS applies a cluster energy > 0 cut
  * This is applied to the clusters written out here
  * They are all written out at LCW scale (mitigates lack of jet calibration)
* Clusters pt [vector<float>]
* Clusters eta [vector<float>]
* Clusters phi [vector<float>]
* Clusters m [vector<float>]
  * I checked, and it’s always zero as expected
  * ROOT compresses by factor of ∼90 compared to pt/eta/phi
  * Supports using the same commands regardless of the object type
 
### Dataset contents, truth particles
* Jet reco in ATLAS applies a filter on truth particles
  * Only stable particles (cτ > 10 mm), excluding muons and neutrinos
  * This is applied using standard ATLAS tools here as well
* Particles pt [vector<float>]
* Particles eta [vector<float>]
* Particles phi [vector<float>]
* Particles m [vector<float>]
* Particles pdgID [vector<int>]
  * Allows for studies of pions vs kaons vs etc
  * Not strictly needed, but useful and could support other studies
 
### Dataset contents, reconstructed jets
* Jets are stored with moderate pT cuts to save space
  * They can be rebuilt down to arbitrarily low pT with the input objects
  * Saved without any calibration: students can perfectly rebuild them
* RecoJets R4 {pt,eta,phi,m,jvf}: [vector<float>]x5
  * Built from topoclusters, stored for pT > 15 GeV
* TrackJets R4 {pt,eta,phi,m}: [vector<float>]x4
  * Built from tracks from the leading PV, stored for pT > 10 GeV
* RecoJets R10 {pt,eta,phi,m,D2beta1,tau32wta}: [vector<float>]x6
  * Built from topoclusters, stored for pT > 150 GeV
* RecoJets R10 Trimmed {pt,eta,phi,m,D2beta1,tau32wta}: [vector<float>]x6
  * Stored for pT > 150 GeV on the ungroomed jet (keep index parallelism)
* TruthJets R4 {pt,eta,phi,m}: [vector<float>]x4
  * Built from truth particles, stored for pT > 5 GeV
* TruthJets R10 {pt,eta,phi,m,D2beta1,tau32wta}: [vector<float>]x6
  * Built from truth particles, stored for pT > 100 GeV
* TruthJets R10 Trimmed {pt,eta,phi,m,D2beta1,tau32wta}: [vector<float>]x6
  * Stored for pT > 100 GeV on the ungroomed jet (keep index parallelism)

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
