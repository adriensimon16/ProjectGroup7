#%%
from download import download
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import json
from itertools import combinations
import networkx as nx
from ipywidgets import interact
from Opti_traj import *
import folium
from openrouteservice import convert
import openrouteservice
#%%
data = pd.read_csv("coordonnées.csv")

url = 'https://raw.githubusercontent.com/SENEAssane/ProjectGroup7/main/Package/Data/dataprixnettoye.csv'
path = os.path.join(os.getcwd(),'dataprixnettoye.csv')
download(url, path, replace=True)
prix = pd.read_csv('./dataprixnettoye.csv')


#%%
# Crée une liste qui contient le nom de toutes les villes
villes = [] 
for i in range (len(S)):
 villes.append(prix.columns[S[i]+1])
Sorties_Possibles= np.arange(26)
def Optimisation_trajet(DEPART, ARRIVEE, Nombre):
    i = transformN(DEPART)
    j = transformN(ARRIVEE)
    V = Finale(i,j,Nombre) 
    nbSort = nbSorties(i,j)

    if Nombre > (len(nbSorties(i,j))-2):
      print ("Veuillez verifier que le nombre de sorties ", end="\n ")
      print("intermédiaires que vous avez prévu est valide")
    elif Nombre == 0 : 
       print('Vous n\'avez sélectionné aucune sortie intermédiaire', end = " " )
       print('Votre trajet vous coûtera donc :' , end = " ")
       print(V[1], end="€. ")
    elif type(V) == "str":
       print(V)
    elif type(nbSort) == "str":
       print(nbSort)
    else :
     print ('Pour aller de ', end= " ")
     print (V[0][0], end = " ")
     print ('à ',end= " ")
     print (V[0][-1])
     print ('Nous vous conseillons les sorties suivantes :')
     print (V[0][1:-1])
     print ('Au lieu de payer', end=" ")
     print (prixab(i,j), end="€ ")
     print ('vous aurez payé', end=" " )
     print (round(V[1],2), end="€.\n")
     print ('Vous économisez', end=" ")
     print (round(prixab(i,j) - V[1],2) ,end="€. " )
    

interact(Optimisation_trajet, DEPART = villes, ARRIVEE = villes,Nombre=Sorties_Possibles)


# %%

