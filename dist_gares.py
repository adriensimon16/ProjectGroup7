#%% 
import numpy as np
import requests
import json
import pandas as pd
from pyproj import Proj, transform , CRS
import geopandas as gpd

#%%

df_brut = pd.read_csv('Gares-peage_2019.csv' , sep = ';')

X = df_brut['ROUTE']
A=[]
for i in range (len(X)):
    if X[i] not in ["A0009","A0061","A0062","A0066","A0075","A0620","A0709",] :
        df_brut.drop(i,0,inplace = True)
df_brut = df_brut.reset_index()

#%%
X = df_brut['X']
Y = df_brut['Y']
#%%
inProj = Proj("+proj=lcc +lat_1=49 +lat_2=44 +lat_0=46.5 +lon_0=3 +x_0=700000 +y_0=6600000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs")

outProj = Proj("+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs")

Coord = transform(inProj,outProj,X,Y)
print(Coord)
#%%

GPS=[]     
for i in range (len(df_brut)):
    GPS.append( transform(inProj, outProj, X[i], Y[i]))

#%%
dist = []

for i in range (len(GPS)):
    if i-1 < 0:
        x,y = GPS[i]
    else:
        x,y = GPS[i-1]
    x1,y1=GPS[i]

    r = requests.get(f"http://router.project-osmr.org/route/v1/car/{x},{y};{x1},{y1}?overwiev=false""")


    routes =json.loads(r.content)
    route_1 = routes.get("routes")[0]
    dist.append(round(route_1['distance']/100))
print(dist)


