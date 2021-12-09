#%%
# Importation des packages 
from download import download
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import json
#%%

#Partie de calcul des coordonnées de chaque sortie

data = pd.read_csv("coordonnées.csv")
X = data['X']
Y = data['Y']
# Création d'une vecteur qui contient les coordonées GPS  
GPS = [] 
for i in range (len(data)):
 GPS.append((X[i],Y[i]))

# %%
# Le calcul du vecteur distance 
dist = []
for i in range (len(GPS)):
  if i-1 < 0:
     x,y = GPS[i]
  else:
     x,y = GPS[i-1]
  x1,y1=GPS[i]

  r = requests.get(f"http://router.project-osrm.org/route/v1/car/{x},{y};{x1},{y1}?overview=false""")


  routes =json.loads(r.content)
  route_1 = routes.get("routes")[0]
  dist.append(round(route_1['distance']/1000))
  
print(dist)


# %%
######################################
#la portion de code suivante traite de l'optimisation du trajet 

######################################

from itertools import combinations
import networkx as nx
from ipywidgets import interact

# Lecture de la base de données Data_prix 
data_prix=pd.read_csv('Data_prix.csv')

def functOpti(entree,sortie,nbdeinout):
   return 
 
######################################
#la portion de code suivante traite de l'optimisation du trajet 

######################################

from itertools import combinations
import networkx as nx
from ipywidgets import interact


url = 'https://raw.githubusercontent.com/SENEAssane/ProjectGroup7/main/Package/Data/dataprixnettoye.csv'
path = os.path.join(os.getcwd(),'dataprixnettoye.csv')
download(url, path, replace=True)
prix = pd.read_csv('./dataprixnettoye.csv')
#%%
S  = []
for i in range(37):
   S.append(i)
#%%  
P0 = [[0,1,2,3,4,5,6,7,8,9,10],[1,2],[]] #A9 1e partie
P1 = [[11,12,13,14,15,16],[],[0,2]] #A9 2e partie
P2 = [[17,18,19,20,21,22],[3,4],[0,1]] #A61 1e partie
P3 = [[23,24,25,26],[],[2,4]] #A66
P4 = [[27,28,29,30,31,32,33,34,35,36],[],[2,3]] #reste A61+A62

P = [P0,P1,P2,P3,P4]
class test:
   def __init__(self) -> None:
      pass
   def portion(x):
      '''Cette fonction donne la portion de route dans laquelle se trouve une sortie 'x' elle prend un entier en entrée'''
      for i in range(len(P)):
         if x in P[i][0]:
            return i

def position(y):
  '''Cette fonction donne la position à l'interieur de la portion de route correspondante de la sortie 'y'. Elle prend un entier en entrée'''
  for i in range(len(P[test.portion(y)][0])):
     if y == P[test.portion(y)][0][i]:
        return i

def nbSorties(A,B):
   '''Cette fonction calcule quelles sorties se trouvent entre le point d'entrée et le point de sortie de l'autoroute choisis. 
   Elle prend en argument les indices du point d'entrée et du point de sortie.'''
   a = min(A,B)
   b = max(A,B)
   traj = []
   if (A == 25 and B==26):
      return "vous ne pouvez pas entrer sur l'autoroute dans ce sens à la sortie Pamier Nord"
   if (A == 26 and B==25):
      return "vous ne pouvez pas sortir de l'autoroute dans ce sens à la sortie Pamier Nord"

   if test.portion(a)==test.portion(b):
      for i in range(position(a),position(b)+1):
         traj.append(P[test.portion(b)][0][i])
      if A>B:
         traj.reverse()

      return traj

   if test.portion(b) in P[test.portion(a)][1]:
      for i in range(position(a),len(P[test.portion(a)][0])):
         traj.append(P[test.portion(a)][0][i]) 

   if test.portion(b) in P[test.portion(a)][2]:
      for i in range(0,position(a)+1):
         traj.append(P[test.portion(a)][0][(position(a))-i])
      

   if (test.portion(b) in P[test.portion(a)][2])==False and (test.portion(b) in P[test.portion(a)][1])==False:
      if 2 in P[test.portion(a)][1]:
         for i in range(position(a),len(P[test.portion(a)][0])):
            traj.append(P[test.portion(a)][0][i])
         
      if 2 in P[test.portion(a)][2]: 
         for i in range(0,position(a)+1):
            traj.append(P[test.portion(a)][0][(position(a))-i])

      for i in range(len(P[2][0])):
         traj.append(P[2][0][i])

   for j in range(0,(position(b)+1)):
       traj.append(P[test.portion(b)][0][j]) 

   if A>B:
      traj.reverse()

   return traj



def transformN(a):
   '''Cette fonction permet de passer du nom de la sortie sous forme de string à son index dans le tableau des prix'''
   
   if a in ['Peage de Montpellier St-Jean','Peage du Perthus','Le Boulou (peage sys ouvert)','Peage de pamiers','Peage de Toulouse sud/ouest','Peage de Toulouse sud/est']:
      return "Cette sortie n'est pas valide"
   for i in range (len(prix.columns)):
      if  a == prix.columns[i]:
         return i-1
   
   return "Cette sortie n'est pas valide"
      
def transformNum(a):
   '''Cette fonction fait l'opération inverse de la fonction précédente'''
   return prix.columns[a+1]
#%%
def prixab(a,b):
   '''Cette fonction permet de calculer le prix entre deux sorties données, à partir du tableau des prix'''
   return (prix.iloc[a][b+1])

def march(A,B,k):
   '''Cette fonction permet de lister toutes les combinaisons de k sorties entre des sorties d'autoroutes données en entrée.
   Elle prend donc en arguments l'index du point d'entrée sur l'autoroute, l'index du point de sortie et le nombre exact de sorties intermédiaires que l'on souhaite effectuer.'''
   L = []
   for i in (combinations(nbSorties(A,B),k+2)):
      if list(i)[0]==A and list(i)[-1]==B:
         L.append(list(i))

   return L

def prixopt(A):
   '''Cette fonction calcule le prix le moins chère, pour un trajet entre deux sorties d'autoroute en exactement k sorties intermédiaires.
   Elle prend en argument une liste de listes.
   Nous l'avons utilisée en complément de la fonction march pour obtenir le résultat souhaité.'''
   L = []
   somm1 = 1000.0
   somm2 = 0.0
   for i in range(len(A)):
      for j in range(len(A[i])-1):
         somm2+=prixab(A[i][j],A[i][j+1])
      if somm2<somm1 :
         somm1=somm2
         somm2=0.0
         L=A[i]
      else:
         somm2=0.0
   return [L,somm1]


def Finale(A,B,k):
   '''Cette fonction permet de calculer le trajet le moins cher entre deux sorties d'autoroute avec au maximum k sorties intermédiaires.
   Nous l'avons utilisée en combinaison avec les fonctions prixopt et march.
   Elle prend en entrée l'index du point d'entrée sur l'autoroute, l'index du point de sortie et k : le nombre maximum de sorties intermédiaires autorisées.
   Cette fonction retourne la liste des sorties qui minimisent le coût du trajet, le prix que coûtera le trajet en sortant aux sorties indiquées et le nombre de sorties intermédiaires recommandées.'''
   L = []
   b = B
   if A==B:
      return "Vous devez choisir une sortie différente de votre point d'entrée"
   if B==0:
      b=1
   
   for i in range(k+1):
     L.append(prixopt(march(A,b,i)))
   a=prixopt(march(A,b,0))
   for j in range(len(L)):
      if L[j][1]<a[1]:
         a=L[j]
   a.append(len(a[0])-2)
   if B==0:
      a[0][-1]=0
   for x in range(len(a[0])):
      a[0][x]=transformNum(a[0][x])
   if a[1]==1000.0:
      return "Veuillez verifier que le trajet que vous avez prévu est un trajet valide"
   
   a[1]=round(a[1],2)

   return a

      

# %%

