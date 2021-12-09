.. Projet Groupe 7 documentation master file, created by
   sphinx-quickstart on Thu Dec  2 20:08:06 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.
Autoroutes du Sud-Ouest de la France
====================================

Ce projet à pour but de créer un package python permettant à tout utilisateur de plannifer et 
optimiser un trajet sur les autoroutes **A9**, **A61**, **A62**, **A66**, **A706**, **A75** et **A620** entre Montpellier, Toulouse et Perpignan.
Il permettra, entre autres de minimiser le coût du trajet en sortant et re-entrant sur l'autoroute selon 
un nombre maximum de sorties choisi par l'utilisateur, d'afficher une carte cliquable du réseau autoroutier et de donner une distribution des prix entre sorties.

.. figure:: carte.png
   :height: 350
   :width: 320
   :scale: 70
   :align: center
   :class: with-shadow
   :alt: Carte

Lien github 
-----------

lien pour cloner le répositoire :   https://github.com/SENEAssane/ProjectGroup7.git 
 
Packages et prérequis
---------------------

..  Note ::
 Packages nécessaires au fonctionnement du programme :
 ``requests`` ``json`` ``pandas`` ``pyproj`` ``geopandas`` ``osmnx`` ``numpy`` ``download``




Indications et conseils d'utilisation
======================================

Parmi les sorties d'autoroutes qui sont incluses sur le réseau autoroutier qui nous
intéresse pour ce projet, il y a plusieurs cas particuliers à traiter. 
D'apres le document disponible dans le lien : 
https://public-content.vinci-autoroutes.com/PDF/Tarifs-peage-asf-vf/ASF-C1-TARIFS-WEB-2021-maille-vf.pdf 
nous sommes rendus compte que certaines sorties ne pouvaient pas être utilisées selon la provenance de l'utilisateur. 
C'est le cas notamment des sorties Le Boulou et Pamiers Nord. Par exemple il est impossible de sortir de l'autoroute à Pamiers Nord en venant de Pamiers Sud,
ni de prendre l'autoroute à Pamiers Nord pour aller vers Pamiers Sud. C'est pourquoi nous vous prions de bien faire attention avant d'utiliser ce package, de vérifier que le trajet que vous souhaitez plannifier est un trajet possible du point de vue logistique.



.. toctree:: Carteinteractif/Carteinteractif
   :maxdepth: 2
   :caption: Carte interactive
.. toctree:: OptimisationTrajet/Optimisation
   :maxdepth: 2
   :caption: Optimisation du trajet
.. toctree:: Distributionprix/Distributionprix
   :maxdepth: 2
   :caption: KDE de Distribution des prix
.. toctree:: 
   :maxdepth: 2
   :caption: Contents

