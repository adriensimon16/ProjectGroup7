#%%
# Importer les packages 
from itertools import combinations
from download import download
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import json
from Opti_traj import *

#%%
#Nous allons tester nos fonctions avec des cas particuliers notamment les sorties "problématiques" 
#comme Pamiers Nord ou les sorties aux extremités du réseau d'autoroutes.

url = 'https://raw.githubusercontent.com/SENEAssane/ProjectGroup7/main/Package/Data/dataprixnettoye.csv'
path = os.path.join(os.getcwd(),'dataprixnettoye.csv')
download(url, path, replace=True)
prix = pd.read_csv('./dataprixnettoye.csv')
#%%
def test_transformN():
    assert transformN('Le palays')==28 and transformN('Vendargues')==0

#%%
def test_transformNum():
    assert transformNum(36)=='Sesquieres' 

# %%
def test_prixab():
    assert prixab(13,6)==9.5


# %%
def test_Finale():
    assert Finale(7,22,4) == [['Agde Pezenas','Beziers ouest','Lezignan','Carcassone est','Carcassone ouest'],7.9,3]

# %%
def test_Distab():
    assert Distab(9,12)==31.0
    
    
# %%

