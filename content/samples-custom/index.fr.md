
---
title: "A Public Dataset For Teaching Jet Reconstruction"
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


{{< /rawhtml >}}

### Motivation
* Les ensembles de données publics se concentrent généralement sur des objets « de haut niveau »
  * Jets, electrons, muons, etc
  * Cela est parfaitement logique pour une utilisation générale pour la plupart des études
* Cependant, cela ne suffit pas pour enseigner la reconstruction
  * Comment et pourquoi utilise-t-on certaines techniques de reconstruction ?
  * Quels sont les compromis liés à l'utilisation de différents types de détecteurs ?
  * Comment le pileup impacte-t-il la reconstruction d'objets ?
* Nous proposons un nouvel ensemble de données qui peut être utilisé pour enseigner la reconstruction de jets
  * Contenus les plus importants : topoclusters et pistes(per-vertex)
  *Échantillon : dijets Pythia8, ∼100 000 événements/tranche =⇒ événements O(1M)
  * Fusionner les tranches en un seul échantillon, à plat en pT

### Exemples d'études soutenues par un tel ensemble de données
* Études d'empilements petit-R:
  * Comment la multiplicité des jets dépend-elle du pileup?
  * Comment les chenilles peuvent-elles être utilisées pour supprimer les jets pileup
  * Pourquoi ne construisons-nous pas des jets à partir de chenilles au lieu de clusters ?
* Études de sous-structures de grand R:
  * Comment l'algorithme du jet affecte-t-il l'interprétation de l'événement?
  * Quel est l'impact de l'algorithme du jet sur la masse du jet?
  * Comment l'algorithme du jet affecte-t-il la stabilité de l'empilement?
* De nombreuses autres études pédagogiques intéressantes sont possibles
  * Un tel jeu de données aurait une grande variété d'utilisations pédagogiques !
  * Beaucoup d'extensions possibles si cela est bien reçu

### Présentation de l'ensemble de données
* Le jeu de données est maintenant prêt
  * Dix fichiers de 102.9k événements chacun (total 1.029M événements), total 21 GB
  * Chaque fichier contient 343 bacs avec 300 événements chacun et fait 2,1 GB
  * De plus, il ne s'agit que de MC, aucune donnée(plus à ce sujet plus tard)
* Vous êtes invités à consulter l'ensemble de données
  * L'un des dix fichiers est [ici](https://cernbox.cern.ch/index.php/s/ieHsllIjTtJIHTo) (le mot de passe est “JetReco”)
  *Une paire d'exercices est également disponible [ici](https://cernbox.cern.ch/index.php/s/0ws6P5MkNVzZInL) (le mot de passe est “JetReco”)
* Les diapositives suivantes contiennent:
  * Détails sur le contenu du jeu de données
  * Exemples de ce qui peut être fait avec ces fichiers (à partir des exercices)
  * Une discussion sur les choix effectués et les suites possibles

## Détails sur le contenu du jeu de données
---

### Contenu de l'ensemble de données, niveau élevé
* Ceci est l'aperçu de haut niveau du contenu
  * Un aperçu détaillé de chaque aspect se trouve sur les diapositives suivantes
* Informations générales au niveau de l'événement (VAN, etc.)
* Pistes, avec des sélections de jets standard appliquées
* Clusters, avec des sélections de jets standard appliquées
* Particules de vérité, avec des sélections de jets standard appliquées
* Différents types de jets reconstruits
  * Tous les jets reconstruits peuvent être reconstruits à partir de l'ensemble de données
  * Ils sont inclus pour aider l'utilisateur à démarrer et pour la validation
  
### Contenu de l'ensemble de données, informations au niveau de l'événement
* Numéro d'événement [non signé long long]
* RunNumber [non signé long long]
  * Pas très utile pour MC, mais utile au cas où des données seraient ajoutées plus tard
* EventWeight [float]
  * Quantité complexe, décrite plus loin, mais c'est le seul poids nécessaire
* mu moyen [flotteur]
* mu réel [flotteur]
  * Identique à la moyenne de mu dans MC, mais pour les données, nous pouvons vouloir les deux
* VAN [entier non signé]
  * Définition typique utilisée pour l'étalonnage du jet : nécessite deux pistes
* Notez que certaines variables communes ne sont PAS incluses
  * Pas de mcChannelNumber car nous avons fusionné plusieurs échantillons ici
  * Pas de poids individuel car tout est collé dans EventWeight
  * Pas de poids d'empilement - pas nécessaire pour MC uniquement

### Contenu du jeu de données, pistes
* Jet reco dans ATLAS applique certaines sélections standard aux pistes
  * pT > 500 MeV, bonne qualité, etc.
* Ceux-ci sont également appliqués aux pistes de cet ensemble de données
* Correspondance de sommet effectuée à l'aide d'outils d'association piste à sommet standard
* Pistes pt [vecteur<float>]
* Pistes eta [vector<float>]
* pistes phi [vector<float>]
* pistes m [vector<float>]
  * J'ai vérifié, c'est toujours fixé à la masse du pion comme prévu
  * ROOT compresse d'un facteur 2 par rapport à pt/eta/phi
  * Prend en charge l'utilisation des mêmes commandes quel que soit le type d'objet
* pistes vtx [vector<int>]
  * L'utilisateur doit parcourir les pistes et identifier les « sommets » à l'aide de ces indices
  * A décidé de le faire pour économiser de l'espace plutôt que de stocker des sommets
  * int non non signé car les pistes non associées à un sommet ont un index -1
 
### Contenu de l'ensemble de données, clusters
* Jet reco dans ATLAS applique une énergie de cluster > 0 cut
  * Ceci est appliqué aux clusters écrits ici
  * Ils sont tous écrits à l'échelle LCW (atténue le manque d'étalonnage du jet)
* Groupes pt [vector<float>]
* Groupes eta [vector<float>]
* Groupes phi [vector<float>]
* Groupes m [vector<float>]
  * J'ai vérifié, et c'est toujours zéro comme prévu
  * ROOT compresse d'un facteur ∼90 par rapport à pt/eta/phi
  * Prend en charge l'utilisation des mêmes commandes quel que soit le type d'objet
 
### Contenu de l'ensemble de données, particules de vérité
* Jet reco dans ATLAS applique un filtre sur les particules de vérité
  * Seules les particules stables (cτ > 10 mm), à l'exclusion des muons et des neutrinos
  * Ceci est également appliqué à l'aide des outils ATLAS standard.
* Particules pt [vector<float>]
* Particules eta [vector<float>]
* Particules phi [vector<float>]
* Particules m [vector<float>]
* Particules pdgID [vector<int>]
  * Permet des études de pions vs kaons vs etc.
  * Pas strictement nécessaire, mais utile et pourrait soutenir d'autres études
 
### Contenu du jeu de données, jets reconstruits
* Les jets sont stockés avec des coupes pT modérées pour économiser de l'espace
  * Ils peuvent être reconstruits jusqu'à un pT arbitrairement bas avec les objets d'entrée
  * Enregistré sans aucun calibrage : les étudiants peuvent parfaitement les reconstruire
* RecoJets R4 {pt,eta,phi,m,jvf}: [vector<float>]x5
  * Construit à partir de topoclusters, stocké pour pT > 15 GeV
* TrackJets R4 {pt,eta,phi,m}: [vector<float>]x4
  * Construit à partir des pistes du PV principal, stocké pour pT > 10 GeV
* RecoJets R10 {pt,eta,phi,m,D2beta1,tau32wta}: [vector<float>]x6
  * Construit à partir de topoclusters, stocké pour pT > 150 GeV
* RecoJets R10 Trimmed {pt,eta,phi,m,D2beta1,tau32wta}: [vector<float>]x6
  * Stocké pour pT > 150 GeV sur le jet non damé (garder le parallélisme des indices)
* TruthJets R4 {pt,eta,phi,m}: [vector<float>]x4
  * Construit à partir de particules de vérité, stockées pour pT > 5 GeV
* TruthJets R10 {pt,eta,phi,m,D2beta1,tau32wta}: [vector<float>]x6
  * Construit à partir de particules de vérité, stockées pour pT > 100 GeV
* TruthJets R10 Trimmed {pt,eta,phi,m,D2beta1,tau32wta}: [vector<float>]x6
  * Stocké pour pT > 100 GeV sur le jet non damé (garder le parallélisme des indices)
 
Pour plus d'informations cliquez [ici](http://opendata.cern.ch/record/15010)


 ---
 
## <a name="atlas-disclaimer">Avertissement</a>
Cet ensemble de données est fourni par la collaboration ATLAS uniquement à des fins éducatives et ne convient pas aux publications scientifiques.
* Le [ATLAS Open Data](http://opendata.atlas.cern) sont libérés sous le [Renonciation Creative Commons CC0](http://creativecommons.org/publicdomain/zero/1.0/).
* Ni ATLAS ni le CERN n'approuvent les travaux réalisés à partir de ces données, qui sont uniquement destinées à un usage pédagogique.
* Tous les ensembles de données auront un[DOI](https://en.wikipedia.org/wiki/Digital_object_identifier) que vous êtes invité à citer dans toute application ou publication (non scientifique).
* Malgré leur traitement, les ensembles de données primaires de haut niveau restent complexes et des critères de sélection doivent être appliqués afin de les analyser, ce qui nécessite une certaine compréhension de la physique des particules et du fonctionnement des détecteurs.
* La grande majorité des données ne peuvent pas être visualisées dans de simples tableaux de données pour des analyses basées sur des feuilles de calc

---
