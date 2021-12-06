#%%
from itertools import combinations
from download import download
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import json
from DistancesGPS import *

#%%
#Nous allons tester nos fonctions avec des cas particuliers notamment les sorties "problématiques" 
#comme Pamiers Nord ou les sorties aux extremités du réseau d'autoroutes.
prix=pd.read_csv("Data_prix.csv")
#%%
def test_transformN():
    assert transformN('Le palays')==33 and transformN('Vendargues')==0

#%%
def test_transformNum():
    assert transformNum(42)=='Sesquieres' and transformNum(5)=='Peage de Montpellier St-Jean'

# %%
def test_prixab():
    assert prixab(12,37)==15.6


# %%
def test_Finale():
    assert Finale(7,22,4)==[['Agde Pezenas','Beziers ouest','Lezignan','Carcassone est','Carcassone ouest'],7.9,3]

# %%
