#%%
from download import download
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import json
#%%
data = pd.read_csv("coordonnées.csv")


X=data['X']
Y=data['Y']

# %%
GPS=[] 
for i in range (len(data)):
 GPS.append((X[i],Y[i]))

# %%


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

# %%

#print(dist)

#len(dist)

# %%
data_prix=pd.read_csv('Data_prix.csv')

#print(data_prix)

def functOpti(entree,sortie,nbdeinout):
   return 




# %%
#Partie Algo:

prix=pd.read_csv("Data_prix.csv")

S  = [0,1,2,3,4,6,7,8,9,10,11,12,13,14
,15,16,19,20,21,22,23,24,25,26,27
,29,30,31,33,35,36,37,38,39,40,41,42]

P0 = [[0,1,2,3,4,6,7,8,9,10,11],[1,2],[]] #A9 1e partie
P1 = [[12,13,14,15,16,19],[],[0,2]] #A9 2e partie
P2 = [[20,21,22,23,24,25],[3,4],[0,1]] #A61 1e partie
P3 = [[26,27,29,30],[],[2,4]] #A66
P4 = [[31,33,35,36,37,38,39,40,41,42],[],[2,3]] #reste A61+A62

P = [P0,P1,P2,P3,P4]

def portion(x):
   for i in range(len(P)):
      if x in P[i][0]:
         return i

def position(y):
   for i in range(len(P[portion(y)][0])):
      if y ==P[portion(y)][0][i]:
         return i
lst=[]
#%%
def nbSorties(A,B):
   a=min(A,B)
   b=max(A,B)
   traj=[]
   if (A == 29 and B==30):
      return "vous ne pouvez pas entrer sur l'autoroute dans ce sens à la sortie Pamier Nord"
   if (A == 30 and B==29):
      return "vous ne pouvez pas sortir de l'autoroute dans ce sens à la sortie Pamier Nord"

   if portion(a)==portion(b):
      for i in range(position(a),position(b)+1):
         traj.append(P[portion(b)][0][i])
      if A>B:
         traj.reverse()

      return traj

   if portion(b) in P[portion(a)][1]:
      for i in range(position(a),len(P[portion(a)][0])):
         traj.append(P[portion(a)][0][i]) 

   if portion(b) in P[portion(a)][2]:
      for i in range(0,position(a)+1):
         traj.append(P[portion(a)][0][(position(a))-i])
      

   if (portion(b) in P[portion(a)][2])==False and (portion(b) in P[portion(a)][1])==False:
      if 2 in P[portion(a)][1]:
         for i in range(position(a),len(P[portion(a)][0])):
            traj.append(P[portion(a)][0][i])
         
      if 2 in P[portion(a)][2]: 
         for i in range(0,position(a)+1):
            traj.append(P[portion(a)][0][(position(a))-i])

      for i in range(len(P[2][0])):
         traj.append(P[2][0][i])

   for j in range(0,(position(b)+1)):
       traj.append(P[portion(b)][0][j]) 

   if A>B:
      traj.reverse()

   return traj





# %%


