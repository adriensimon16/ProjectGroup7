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

len(dist)

# %%


