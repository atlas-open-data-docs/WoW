---
title: "Data and Simulated Data"
date: 2023-05-23T04:51:13+01:00
draft: false
hideLastModified: true
keepImageRatio: false
showInMenu: false
---

# Data and Simulated Data

## Data

The ATLAS collaboration has released 10 inverse femtobarns of data. (An inverse femtobarn is a measure of the number of particle collision [events](http://opendata.atlas.cern/release/2020/documentation/atlas/GLOSSARY.html) per femtobarn. A barn is defined as \\(10^{-28}\\) \\(m^2\\). A Femto is a prefix in the metric system denoting a factor of \\(10^{−15}\\)).
Ten inverse femtobarns correspond to approximately 1000 trillion proton-proton collisions.

The ATLAS datasets are available on this website and on the [CERN open data portal](http://opendata.cern.ch/education/ATLAS).

## Simulated data

Simulated data, commonly named [Monte Carlo](http://opendata.atlas.cern/release/2020/documentation/atlas/GLOSSARY.html) (MC, which is a reference to the Monte Carlo casino as they introduce randomness into the dataset), are a key feature for the LHC experiments. These events are simulated using current theoretical models and are used to compare theory with real data.

### The full simulation requires the following steps

* **Event generation**: Hadronic final states using the proton-proton collisions are generated using programs relying on theoretical calculations, phenomenological models and experimental inputs. (A phenomenological model is a scientific model that describes the empirical relationship of phenomena to each other).

* **Detector Simulation**: Interaction of the generated particles inside the ATLAS detector is simulated.

* **Digitisation**: The detector response is derived from the particle interactions and it is written in a format compatible with the real output of the detector. Also, because of the high rate of collisions in the LHC, digitised signals from several simulated events can be piled-up to create samples with a realistic experimental [background](http://opendata.atlas.cern/release/2020/documentation/atlas/GLOSSARY.html). 

* **Reconstruction**: Particle trajectories and energies from the detector are reconstructed. Such final samples are used by the physicists.

### Comparing real data and simulated data

Real data and simulated data do not always agree. This can be due to various reasons, such as

* the conditions not being exactly the same e.g. Energy, pile-up.

* not all background processes are included in the simulated data,

* the physics has not been exactly modeled by the theory.

If the data and simulated data does not agree, it is important that physicists understand why because it could lead to new discoveries.

## Recap: What is Monte Carlo data and what is their purpose?

Simulated data, whose events are simulated using current theoretical models.
These can be used to compare theory with real data.


## Recap: Why don’t we just use the simulations?

Real data and simulated data do not always agree. This can be due to various reasons.  If the data and simulated data do not agree, it is important that physicists understand why.

