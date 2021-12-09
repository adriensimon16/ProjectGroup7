# README

## Membres du Groupe

Assane Sene assane.sene@etu.umontpellier.fr

Abderrahim Ait Moulay abderrahim.ait-moulay01@etu.umontpellier.fr

Adrien Simon adrien.simon@etu.umontpellier.fr


## Autoroutes du Sud-Ouest de la France (asof)

Ce projet à pour but de créer un package python permettant à tout utilisateur de plannifer et optimiser un trajet sur les autoroutes A9, A61, A62, A66, A706, A75 et A620 entre Montpellier, Toulouse et Perpignan.

Il permettra, entre autres de minimiser le coût du trajet en sortant et re-entrant sur l'autoroute selon un nombre maximum de sorties choisi par l'utilisateur, d'afficher une carte cliquable du réseau autoroutier et de donner une distribution des prix entre sorties.

<p align="center">
  <img src="https://github.com/abderrahim-ait/ProjectGroup7/blob/main/Doc/source/carte.png" width="300" title="Autoroute">
</p>

## Méthode 

Nous avons trois objectifs majeurs :

- Afficher une carte cliquable du réseau d'autoroutes
- Afficher une distribution des prix selon les portions de route
- Concevoir un algorithme permettant de calculer les points de sortie optimaux pour un trajet donné pour minimiser le prix du trajet 


Nous avons également fourni deux dataframes avec les prix entre sorties et les distances entre sorties. Ainsi qu'un readme.md explicatif pour utiliser le programme. 

Nous nous sommes servis des packages suivants pour la conception du package : `requests` `json` `pandas` `pyproj` `geopandas` `osmnx` `numpy` `download` `networkX` `itertools`



## Lien SSH 

lien pour cloner le répositoire : git@github.com:SENEAssane/ProjectGroup7.git

## Packages et prérequis

### Packages nécessaires au fonctionnement du programme

Vous aurez besoin des packages suivants pour pouvoir utiliser le package : `itertools` `numpy` `ipywidgets` `pandas` `networkx` `geopandas`

### Indications et conseils d'utilisation

Parmi les sorties d'autoroutes qui sont incluses sur le réseau autoroutier qui nous intéresse pour ce projet, il y a plusieurs cas particuliers à traiter. D'apres le document disponible dans le lien : https://public-content.vinci-autoroutes.com/PDF/Tarifs-peage-asf-vf/ASF-C1-TARIFS-WEB-2021-maille-vf.pdf nous nous sommes rendus compte que certaines sorties ne pouvaient pas être utilisées selon la provenance de l'utilisateur. C'est le cas notamment des sorties Le Boulou et Pamiers Nord. Par exemple il est impossible de sortir de l'autoroute à Pamiers Nord en venant de Pamiers Sud, ni de prendre l'autoroute à Pamiers Nord pour aller vers Pamiers Sud. C'est pourquoi nous vous prions de bien faire attention avant d'utiliser ce package, de vérifier que le trajet que vous souhaitez plannifier est un trajet possible du point de vue logistique.


## Plan de travail

Chacun de nous s'occupera d'un des trois objectifs majeurs du projet avec des possibles contribution des autres membres du groupe.

Les tâches intermédiaires seront traitées en commun par nous tous, selon la pertinance de celles-ci avec notre charge de travail principale.



Abderrahim s'occupera de la carte et ses interfaces

Assane s'occupera des distributions des prix

Adrien s'occupera de l'algorithme d'optimisation de trajet

les conseils d'utilisation et la documentation sera remplie au fur et à mesure de l'avancement du projet.

Le projet sera présenté sous la forme d'une présentation orale et d'un Beamer explicatif qui accompagnera notre présentation.

## Documentation et références

Nous avons fait appel au site `router.project-osrm.org` pour calculer les coordonnées des sorties sur la portion d'autoroute qui nous intéresse. Nous nous sommes aussi appuyés sur le site `https://public-content.vinci-autoroutes.com/PDF/Tarifs-peage-asf-vf/ASF-C1-TARIFS-WEB-2021-maille-vf.pdf` pour calculer les prix entre chaque sortie. 
