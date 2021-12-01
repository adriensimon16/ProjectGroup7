#importer les packages 
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import pickle

#lire la base de données 
df = pd.read_csv('Data_prix.csv',sep=';')
df

# voir les valeurs manquantes
df.info()

#Combien des valeur manquante 
df.isnull().sum().sort_values(ascending=False)

#calculer le min, max, la moyenne .......
df.describe()

