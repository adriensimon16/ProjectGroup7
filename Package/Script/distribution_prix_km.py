
#%%
''' Importation des packages '''
from download import download
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np
import os
from scipy.stats.kde import gaussian_kde
from ipywidgets import widgets, interact, interactive, fixed, interact_manual
from Opti_traj import *
#%%
''' importer la base de données Datadistance.csv '''
ur1 = 'https://raw.githubusercontent.com/SENEAssane/ProjectGroup7/main/Package/Data/Datadistance.csv'
path = os.path.join(os.getcwd(),'Datadistance.csv')
download(ur1, path, replace = True)
Dist = pd.read_csv('./Datadistance.csv')
''' importer la base de données dataprixnettoye.csv '''
ur1 = 'https://raw.githubusercontent.com/SENEAssane/ProjectGroup7/main/Package/Data/dataprixnettoye.csv'
path = os.path.join(os.getcwd(),'dataprixnettoye.csv')
download(ur1, path, replace = True)
prix = pd.read_csv('./dataprixnettoye.csv')

def Distribution_Prix(i,j):
   '''
   Parametres :
   ------------
               i : int
               j : int

   Return : 
   --------  
             le prix entre toutes les sorties successives parmi toutes
             les sorties qui se trouvent entre i et j.        
   '''
   V = nbSorties(i,j)
   Pr = []
   for i in range(len(V)-1):
      Pr.append(prixab(V[i],V[i+1]))
   return Pr

def Distab(a,b):
   '''
   Parametres :
   ------------
               a : int
               b : int

   Return : 
   -------- 
             la distance entre les points a et b. 
   '''
   return (Dist.iloc[a][b+1])

def Distribution_dist(i,j):
   '''
   Parametres :
   ------------
               i : int
               j : int

   Return :
   --------
             la distance entre toutes les sorties successives parmi toutes
             les sorties qui se trouvent entre i et j.    
   '''  
   V = nbSorties(i,j)
   Ds = []
   for i in range(len(V)-1):
      Ds.append(Distab(V[i],V[i+1]))
   return Ds   
#%%
def moyDist(i,j):
    '''
    Parametres :
    ------------
                i : int
                j : int

    Return :
    --------
              le prix par km entre toutes les sorties successives parmi toutes
              les sorties qui se trouvent entre i et j.              
    '''
    X = Distribution_Prix(i,j)
    Y = Distribution_dist(i,j)
    V = []
    for i in range(len(X)):
      V.append(float(X[i]/Y[i]))
    return V 
    

#%%
''' creation du vecteur villes '''
villes = [] 
for i in range (len(S)):
   villes.append(prix.columns[S[i]+1])

#%%
''' Kernel Density Estimation (KDE) '''

def kde_explore(entre = villes, sortie = villes,  bw = 0.3):
   '''
   Parametres :
   ------------
               entre : string
               sortie : string
               bw : float

   Return : 
   --------
             affiche la distribution (estimation de la densité) 
             des prix par km entre deux sorties choisies.             
   '''
   i = transformN(entre)
   j = transformN(sortie)
   V = moyDist(i,j)
   fig, ax = plt.subplots(1, 1, figsize = (5, 5))
   sns.kdeplot(np.asarray(V) , bw_adjust = bw, shade = True, cut = 0, ax = ax)
   plt.ylabel("Density level")
   plt.title("Distribution des prix")
   plt.tight_layout()
   plt.show()

interact(kde_explore, entre = villes, sortie = villes, bw = (0.001, 2, 0.01))
# %%