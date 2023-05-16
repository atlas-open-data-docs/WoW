---
title: "Dataset details"
date: 2020-11-23T04:51:13+01:00
draft: false
hideLastModified: true
keepImageRatio: false
showInMenu: false
---

# Dataset Details

An important aspect of the data samples is that they were prepared specifically for educational purposes. To this end, precision has been traded for simplicity of use. The introduced simplifications are:

* No facilities to estimate systematic uncertainties have been included as these quickly introduce large complexities. 

* The b-tagging scale factor is computed for a specific working point (MV1@70% efficiency). The
user, however, is free to specify the b-tagging weight used for tagging jets allowing for a potential mismatch of the definition considered in the scale factor calculation and the one being actually applied.


* No QCD simulated samples were prepared as they would have been insufficient in statistics while introducing large set of additional samples. 


* The description of the $$W$$ boson properties in simulated $$W$$ + jets events is not ideal. 
Corrections are only available
for samples produced with the Monte Carlo generator Alpgen
but not for those produced with
Sherpa generator.  However, using
Alpgen would have introduced a prohibitively large number of samples.  Sherpa was therefore used.


* The missing transverse momentum was calculated using the object preselection.
A recalculation of the missing transverse momentum is not implemented into the tools provided
for simplicity reasons. Therefore, changes in the object selection are not reflected in the missing
transverse momentum leading to potential mis-modeling of variables relying on it.

* The simulated data takes into account the pile-up and vertex position profile of the whole 2012
data taking, although the measured data is taken from a small list of runs from period D. This
introduces a certain mismatch regarding the number of vertices and the primary vertex position.




## Details of the available simulated Monte Carlo datasets


The datasets have been reduced in size to optimise the storage requirements. The available number of events in the samples is given in the column N events, which is after the preselection cuts.

The factor FE denotes the filter efficiency for a given sample and $$f_k$$ is used for rescaling the leading order estimate to next to leading order in perturbative QCD.

The following samples represent about 6.5 Gb.
         
|process | DataSet ID | Generator | $$\sigma$$*FE [pb] | $$f_k$$ | L [$$fb^{-1}$$] | N events | size/Mb|
| -- | -- | -- | -- | -- | -- | -- | -- |
|ttbar -> l + X                | 117050       | PowHeg+Pythia   | 114.51     | 1.2   | 26.236 | 1500000  |   291 |  
|ttbar -> Jets                | 117049       | PowHeg+Pythia   |  96.35     | 1.2   | 85.027 |   25170  |   5.7 |
|single top t-chan top                                | 110090       | PowHeg+Pythia   |  17.52     | 1.05  |  24.21 |  150000  |    21 |
|single top t-chan antitop                            | 110091       | PowHeg+Pythia   |   9.4      | 1.06  |  43.23 |  150000  |    15 |
|single top s-chan                                    | 110119       | PowHeg+Pythia   |  1.64      | 1.107 | 167.73 |  100000  |    15 |
|single top Wt-chan                                   | 110140       | PowHeg+Pythia   | 20.46      | 1.09  |  28.50 |  150000  |    26 |
|Z+Jets ee                                            | 147770       | Sherpa          | 1207.4     | 1.028 |  10.08 |  7500000 |   938 |
|Z+Jets mumu                                          | 147771       | Sherpa          | 1207.4     | 1.028 |   9.63 |  7500000 |   918 |
|Z+Jets tautau                                        | 147772       | Sherpa          | 1207.1     | 1.028 |  11.08 |   750000 |    93  |
|Drell-Yan ee M08to15                                 | 173041       | Sherpa          |  92.15     | 1.0   |  45.95 |   400000 |    57 |
|Drell-Yan ee M15to40                                 | 173042       | Sherpa          | 279.19     | 1.0   |  47.22 |   750000 |   100 |
|Drell-Yan mumu M08to15                               | 173043       | Sherpa          |  92.08     | 1.0   |  51.93 |   500000 |    74 |
|Drell-Yan mumu M15to40                               | 173044       | Sherpa          |  279.2     | 1.0   |  41.01 |   750000 |   103 |
|Drell-Yan tautau M08to15                             | 173045       | Sherpa          |  92.12     | 1.0   |  27.13 |     9993 |   1.5 |
|Drell-Yan tautau M15to40                             | 173046       | Sherpa          | 279.11     | 1.0   |  49.54 |    32393 |   4.5 |
|W+Jets enu with b                                    | 167740       | Sherpa          | 140.34     | 1.1   | 12.333 |   750000 |    86 |
|W+Jets enu with jets, bveto                          | 167741       | Sherpa          | 537.84     | 1.1   |  9.563 |  2600000 |   296 |
|W+Jets enu no jets, bveto                            | 167742       | Sherpa          | 10295      | 1.1   |  1.971 |  8000000 |   722 |                  
|W+Jets munu with b                                   | 167743       | Sherpa          | 140.39     | 1.1   | 11.935 |   750000 |    84 |
|W+Jets munu with jets, bveto                         | 167744       | Sherpa          | 466.47     | 1.1   | 10.582 |  2500000 |   287 |
|W+Jets munu no jets, bveto                           | 167745       | Sherpa          | 10368      | 1.1   |  1.719 |  7500000 |   666 |
|W+Jets taunu with b                                  | 167746       | Sherpa          | 140.34     | 1.1   | 18.245 |   100000 |    13 |
|W+Jets taunu with jets, bveto                        | 167747       | Sherpa          | 506.45     | 1.1   |  9.821 |   250000 |    31 |
|W+Jets taunu no jets, bveto                          | 167748       | Sherpa          | 10327      | 1.1   |  1.945 |   550000 |    55 |                                                                                   
|WW                                                   | 105985       | Herwig          | 12.42      | 1.683 |  46.32 |   500000 |    63 |
|ZZ                                                   | 105986       | Herwig          | 0.992      | 1.55  | 151.19 |   125000 |    20 |
|WZ                                                   | 105987       | Herwig          | 3.667      | 1.9   | 138.44 |   500000 |    68 |

The $$Z'$$ and Higgs samples represent a further 150 Mb.
         
|process                                              | DataSet ID  | Generator       | $$\sigma$$*FE [pb] | $$f_k$$ | L [$$fb^{-1}$$] | N events     | size/Mb |
| -- | -- | -- | -- | -- | -- | -- | -- | -- |
|Z' -> ttbar [ 400] GeV | 110899 | Pythia | 4.259    | 1.0  | 23.48  |   18307  | 4.3  |
|Z' -> ttbar [ 500] GeV | 110901 | Pythia | 3.925    | 1.0  | 25.48  |   19737  | 4.7  |
|Z' -> ttbar [ 750] GeV | 110902 | Pythia | 1.243    | 1.0  | 80.45  |   21051  | 5.3  |
|Z' -> ttbar [1000] GeV | 110903 | Pythia | 0.394    | 1.0  | 253.81 |   20649  | 5.5  |
|Z' -> ttbar [1250] GeV | 110904 | Pythia | 0.139    | 1.0  | 719.43 |   19274  | 5.5  |
|Z' -> ttbar [1500] GeV | 110905 | Pythia | 0.0524   | 1.0  | 1908   |   17695  | 5.4  |
|Z' -> ttbar [1750] GeV | 110906 | Pythia | 0.0211   | 1.0  | 4739   |   15949  | 5.1  |
|Z' -> ttbar [2000] GeV | 110907 | Pythia | 0.00894  | 1.0  | 11186  |   14455  | 4.9  |
|Z' -> ttbar [2250] GeV | 110908 | Pythia | 0.00394  | 1.0  | 25381  |   13389  | 4.7  |
|Z' -> ttbar [2500] GeV | 110909 | Pythia | 0.00180  | 1.0  | 55556  |   12723  | 4.5  |
|Z' -> ttbar [3000] GeV | 110910 | Pythia | 0.000434 | 1.0  | 230415 |   12387  | 4.3  |
|gg-> H->  WW-> llnunu         ; M(H) = 125 GeV   | 161005 | PowHeg+Pythia   | 6.463      | 1.0 | 32.13   | 100000  |  14     |
|VBF H->  WW-> llnunu ; M(H) = 125 GeV    | 161055 | PowHeg+Pythia   | 0.819      | 1.0 | 229.93  | 100000  |  18     |
|gg-> H->  ZZ -> 4l            ; M(H) = 125 GeV         | 160155 | PowHeg+Pythia   | 13.17      | 1.0 | 14.31   | 100000  |  15     |
|VBF H->  ZZ -> 4l    ; M(H) = 125 GeV          | 160205 | PowHeg+Pythia   | 1.617      | 1.0 | 104.96  | 100000  |  19     |

# Navigation
Jump back to the [summary page]({{< ref "/8TevDocOverview" >}} "Summary page").