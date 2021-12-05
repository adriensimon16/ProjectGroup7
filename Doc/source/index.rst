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
   :scale: 75
   :align: center
   :class: with-shadow
   :alt: Carte

   
Méthode
--------
Nous avons trois objectifs majeurs :

 * Afficher une carte cliquable du réseau d'autoroutes
 * Afficher une distribution des prix selon les portions de route
 * Concevoir un algorithme permettant de calculer les points de sortie optimaux pour un trajet donné pour minimiser le prix du trajet

 
Nous allons également fournir deux dataframes avec les prix entre sorties et les distances entre sorties. Ainsi qu'un readme.md explicatif pour utiliser le programme.

Lien github 
-----------

lien pour cloner le répositoire :   https://github.com/SENEAssane/ProjectGroup7.git 
 
Packages et prérequis
---------------------

..  Note ::
 Packages nécessaires au fonctionnement du programme :
 ``requests`` ``json`` ``pandas`` ``pyproj`` ``geopandas`` ``osmnx`` ``numpy`` ``dowload``


.. toctree::
   :maxdepth: 2
   :caption: Contents:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
