
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
df_p
# %%
''' transformation du dataframe en fichier csv '''
df_p.to_csv('data_prix_nettoye.csv')
# %%
