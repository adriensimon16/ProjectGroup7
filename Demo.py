#%%
from download import download
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Package.Script.Carte_interactif import *
from Package.Script.Opti_traj import *
from Package.Script.distribution_prix_km import *
from ipywidgets import interact

#%%
# importer la base de données Base.csv
url = 'https://raw.githubusercontent.com/SENEAssane/ProjectGroup7/main/Package/Data/Base.csv'
path = os.path.join(os.getcwd(),'Base.csv')
download(url, path, replace=True)
geo = pd.read_csv('./Base.csv')
geo = geo.rename(columns={' NOMGARE ':'NOM GARE'})

# importer la base de données dataprixnettoye.csv
url = 'https://raw.githubusercontent.com/SENEAssane/ProjectGroup7/main/Package/Data/dataprixnettoye.csv'
path = os.path.join(os.getcwd(),'dataprixnettoye.csv')
download(url, path, replace=True)
prix = pd.read_csv('./dataprixnettoye.csv')


# Crée une liste qui contient le nom de toutes les villes
villes = sorted(geo.NOMGARE.unique())
villes1 = [] 
for i in range (len(S)):
 villes1.append(prix.columns[S[i]+1])
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
       print('Vous n\'avez sélectionné aucune sortie intermédiaire', end = "\n " )
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
    
interact(itineraire, DEPART = villes, ARRIVEE = villes)
interact(Optimisation_trajet, DEPART = villes1, ARRIVEE = villes1,Nombre=Sorties_Possibles)
interact(kde_explore,entree=villes1 ,sortie=villes1, bw=(0.001, 2, 0.01))
