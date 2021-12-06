#%%
# importer les packages
from download import download
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import json
#%%
# Importer la base de données 
url = 'https://raw.githubusercontent.com/SENEAssane/ProjectGroup7/main/Package/Data/Base.csv'
path = os.path.join(os.getcwd(),'Base.csv')
download(url, path, replace=True)
data = pd.read_csv('./Base.csv')
X = data['X']
Y = data['Y']

# %%
# Créer le vecteur GPS
GPS = [] 
for i in range (len(data)):
 GPS.append((X[i],Y[i]))

# %%
# Créer la matrice des distance
#  qui contient des zéros par défaut

Dist_Matrice = np.zeros(shape=(len(GPS),len(GPS)))

# Puisque notre matrice est symétrique on va calculer juste la partie 
# triangulaire supérieure pour le but de minimiser le temps de calcul

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

# Construire la matrice des distance à partir de la somme de 
# Dist_Matrice avec sans transposé

Matrice = Dist_Matrice + Dist_Matrice.T
#%%
# La création de la base de données data_distance.csv 
# qui contient tout les distances entre les 37 sorties 
#  
Distance = pd.DataFrame(Matrice)
Distance.rename(columns=data['NOMGARE'], inplace=True)
Distance.set_index(data['NOMGARE'], inplace=True)
Distance.to_csv('./data_distance.csv')




