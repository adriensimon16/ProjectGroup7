#%% 
import requests
import json
import pandas as pd
from pyproj import Proj, transform 
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
inProj = Proj(init="epsg:2154")
outProj = Proj(init="epsg:4326")

#%%

GPS=[]     #couples (x,y)
for i in range (len(df_brut)):
    GPS.append( transform(inProj, outProj, X[i], Y[i]))

#%%
dist = []
#call the OSMR API
for i in range (len(GPS)):
    if i-1 < 0:
        x,y = GPS[i]
    else:
        x,y = GPS[i-1]
    x1,y1=GPS[i]

    r = requests.get(f"http://router.project-osmr.org/route/v1/car/{x},{y};{x1},{y1}?overwiev=false""")

#then you load the response using the json library
#by default you get only one alternative so you acces the 0-th element of the 'routes'
    routes =json.loads(r.content)
    route_1 = routes.get("routes")[0]
    dist.append(round(route_1['distance']/100))
print(dist)


