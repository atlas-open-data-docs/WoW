---
title: "Application @13 TeV"
date: 2020-11-23T04:51:13+01:00
draft: false
hideLastModified: true
summaryImage: "images/handmade_event_display.png"
keepImageRatio: false
tags: ["Histograms", "Apps", "JavaScript"]
summary: "Histogram Analyser only simulated data @13 TeV"
showInMenu: false
---


# Higgs à WW - uniquement des données simulées

Les physiciens utilisent des **coupes** pour sélectionner des événements d'intérêt. Les coupes suppriment préférentiellement les processus indésirables (arrière-plan) mais laissent autant que possible le processus souhaité (signal).
Il est utile d'avoir une bonne compréhension des processus physiques impliqués lors de l'application des coupes.

Nous avons créé deux analyseurs d'histogrammes, pour aider à visualiser les données. Les deux analyseurs d'histogrammes affichent quatre processus physiques.

Les quatre processus sont $$H\rightarrow W^+W^-\, WW, t\bar t, Z$$  
Ces processus sont discutés dans la [documentation dédiée](http://opendata.atlas.cern/release/2020/documentation/visualization/the_display_histograms_13TeV.html). Chaque processus est représenté par une couleur différente dans l'analyse d'histogramme.

## Faites des coupes à l'aide de votre curseur.

* Utilisez le curseur pour sélectionner une plage spécifique dans l'un des histogrammes.
* Les plages sélectionnées seront colorées, tandis que les plages non sélectionnées seront grisées.
* Lorsque vous effectuez des coupes sur une variable, les contributions relatives des quatre processus changent.

**Pour effacer votre sélection sur un histogramme spécifique, cliquez sur le fond blanc dans la zone de l'histogramme.**

&nbsp;

---
## **Higgs à WW - données simulées**
L'analyseur d'histogramme affiche neuf histogrammes.
* *Le chargement des histogrammes peut prendre environ 30 secondes.*
* *Pendant le chargement, vous ne verrez que les titres de l'histogramme.*
* *Une fois chargé, vous verrez les histogrammes apparaître sous leurs titres.*

{{< rawhtml >}}

<p align="center">
<iframe name="analyzer" style="overflow:hidden;height: 950px; width:100%"  src="https://atlas-opendata.web.cern.ch/release/2020/documentation/visualization/CrossFilter/13TeV_crossfilter.html" frameborder="0" allowfullscreen></iframe>
</p>

{{< /rawhtml >}}

---

# Suivre cette vidéo pour une explication complète

{{< youtube X1PyNTUwffI >}}
---

### et pour continuer l'exercise...
---

## ... suivez les instructions concernant cette application dans sa [documentation dédiée](http://opendata.atlas.cern/release/2020/documentation/visualization/histogram-analyser-2_13TeV.html)!

---

**Remarque** : Cette application ne ***pas*** se redimensionne bien dans les appareils mobiles. Veuillez l'utiliser dans un ordinateur de bureau ou un ordinateur portable pour une expérience complète.
