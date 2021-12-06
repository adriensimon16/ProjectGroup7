
#%%
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
df_p = pd.read_csv("C:/Users/33751/Downloads/Data_prix.csv", sep=';')
df_p = df_p.fillna(0.0)


del df_p['Peage de Montpellier St-Jean']

del df_p['Peage du Perthus']

del df_p['Le Boulou (peage sys ouvert)']

del df_p['Peage de pamiers']

del df_p['Peage de Toulouse sud/ouest']

del df_p['Peage de Toulouse sud/est']

df_p = df_p.drop(index=[5, 17, 18, 28, 32, 34])

df_p.set_index(' ', inplace=True)


# %%
df_p['Vendargues'] = df_p['Vendargues'].replace(['0','0','0','0','0','22'], ['0.0','0.0','0.0','0.0','0.0','22.0'])
df_p['Narbonne sud'] = df_p['Narbonne sud'].replace(['0', '8.58,5'], ['0.0', ' 8.5'])
#df_p
# %%
df_pnmp = np.array(df_p,dtype='float64')
df_pnmp
# %%
