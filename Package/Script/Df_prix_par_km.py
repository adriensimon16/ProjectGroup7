
#%%
''' importation des packages '''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from download import download 
from ipywidgets import widgets, interact, interactive, fixed, interact_manual
from download import download  
from IPython import get_ipython
import requests
import json

#%%
''' importation des données '''
data = pd.read_csv("C:/Users/33751/Downloads/Base.csv")
X = data['X']
Y = data['Y']

# %%
''' Créer le vecteur GPS '''
GPS = [] 
for i in range (len(data)):
 GPS.append((X[i],Y[i]))

# %%
''' Créer la matrice des distance
    qui contient des zéros par défaut '''

Dist_Matrice = np.zeros(shape = (len(GPS),len(GPS)))

''' Puisque notre matrice est symétrique on va calculer juste la partie 
    triangulaire supérieure pour le but de minimiser le temps de calcul '''

for i in range (len(GPS)):
     x,y = GPS[i]
     for j in range (i,len(GPS)):
       x1,y1 = GPS[j]
       r = requests.get(f"http://router.project-osrm.org/route/v1/car/{x},{y};{x1},{y1}?overview=false""")
       routes1 = json.loads(r.content)
       route_1 = routes1.get("routes")[0]
       A = round(route_1['distance']/1000)

       r2 = requests.get(f"http://router.project-osrm.org/route/v1/car/{x1},{y1};{x},{y}?overview=false""")
       routes2 = json.loads(r2.content)
       route_2 = routes2.get("routes")[0]
       B = round(route_2['distance']/1000)

       Dist_Matrice[i][j] = min (A,B)
#%%

''' Construire la matrice des distance à partir de la somme de 
Dist_Matrice avec sans transposé '''

Matrice = Dist_Matrice + Dist_Matrice.T
#%%
''' La création de la base de données data_distance.csv 
    qui contient tout les distances entre les 37 sorties 
'''  
Distance = pd.DataFrame(Matrice)
Distance.rename(columns = data['NOMGARE'], inplace = True)
Distance.set_index(data['NOMGARE'], inplace = True)
Distance.to_csv('./data_distance.csv')
#Distance
#%%
''' importation des données '''
df_p = pd.read_csv("C:/Users/33751/Downloads/Data_prix.csv", sep = ';')

''' remplacement des NAN par 0.0 dans le dataframe '''
df_p = df_p.fillna(0.0)

''' suppression des colonnes (ou des sorties) où l'on ne peut pas sortir '''
del df_p['Peage de Montpellier St-Jean']

del df_p['Peage du Perthus']

del df_p['Le Boulou (peage sys ouvert)']

del df_p['Peage de pamiers']

del df_p['Peage de Toulouse sud/ouest']

del df_p['Peage de Toulouse sud/est']

df_p = df_p.drop(index = [5, 17, 18, 28, 32, 34])

df_p.set_index(' ', inplace = True)


# %%
''' remplacement de 0 par 0.0 et 8.58,5 par 8.5 dans les colonnes 
    Vendargues et Narbonne sud du dataframe '''
df_p['Vendargues'] = df_p['Vendargues'].replace(['0', '0', '0', '0', '0', '22'], ['0.0', '0.0', '0.0', '0.0', '0.0', '22.0'])
df_p['Narbonne sud'] = df_p['Narbonne sud'].replace(['0', '8.58,5'], ['0.0', ' 8.5'])
#df_p
# %%
''' creation d'une matrice (numpy array) dont le type des elements
    est float
'''
df_pnmp = np.array(df_p, dtype = 'float64')
#df_pnmp
#%%
''' transformation de Distance_nmp en matrice (numpy array) '''
Distance_nmp = Distance.to_numpy()
#Distance_nmp

''' division des deux matrices pour avoir le prix/km '''
div = df_pnmp / Distance_nmp

''' transformation de la matrice div en dataframe '''
df_div = pd.DataFrame(div)

''' remplacement des NAN par 0.0 dans le dataframe 
    et nommer NOMGARE la ligne et colonne qui contient les sorties.
'''
df_div = df_div.fillna(0.0)
df_div.rename(columns = data['NOMGARE'], inplace = True)
df_div.set_index(data['NOMGARE'], inplace = True)
df_div
#%%
''' transformation du dataframe en fichier csv '''
df_div.to_csv('data_prix_par_km.csv')


# %%
