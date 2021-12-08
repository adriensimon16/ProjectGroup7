
# importer les packages
from download import download
import pandas as pd
import folium
from openrouteservice import convert
import openrouteservice
import json
from Opti_traj import *
from ipywidgets import interact

# importer la base de données Base.csv
url = 'https://raw.githubusercontent.com/SENEAssane/ProjectGroup7/main/Package/Data/Base.csv'
path = os.path.join(os.getcwd(),'Base.csv')
download(url, path, replace=True)
geo = pd.read_csv('./Base.csv')
geo = geo.rename(columns={' NOMGARE ':'NOM GARE'})

# importer la base de données Data_distance.csv
ur1 = 'https://raw.githubusercontent.com/SENEAssane/ProjectGroup7/main/Package/Data/Datadistance.csv'
path = os.path.join(os.getcwd(),'Datadistance.csv')
download(ur1, path, replace=True)
Dist = pd.read_csv('./Datadistance.csv')

# importer la base de données Data_distance.csv
ur1 = 'https://raw.githubusercontent.com/SENEAssane/ProjectGroup7/main/Package/Data/dataprixnettoye.csv'
path = os.path.join(os.getcwd(),'dataprixnettoye.csv')
download(ur1, path, replace=True)
prix = pd.read_csv('./dataprixnettoye.csv')

# Fonction
def Distab(a,b):
 '''Cette fonction permet de calculer la distance entre deux sorties données,
     à partir du tableau des distances'''
 return (Dist.iloc[a][b+1])

def prixab(a,b):
   '''Cette fonction permet de calculer le prix entre deux sorties données,
    à partir du tableau des prix'''
   return (prix.iloc[a][b+1])


# Crée une liste qui contient le nom de toutes les villes
villes = sorted(geo.NOMGARE.unique())

def itineraire(DEPART, ARRIVEE):
    i = geo.loc[geo['NOMGARE'] == DEPART].index[0]
    j = geo.loc[geo['NOMGARE'] == ARRIVEE].index[0]
    pr = prixab(i,j)
    Ds = Distab(i,j)
    
    # Résolution du problème de la distance différente entre
    # l'aller et le retour avec une boucle
    if i < j:

        x = [geo['X'][i], 
             geo['Y'][i]]
        
        y = [geo['X'][j], 
             geo['Y'][j]]
        moy = pr/Ds
        coor = [x, y]

        client = openrouteservice.Client(key='5b3ce3597851110001cf6248a649f5b5021e4f02b016b51649758663')  # Specify your personal API key

        m = folium.Map(
                        location=[43.1837661, 3.0042121],
                        zoom_start=10,
                        control_scale=True)

        for i in range(0, len(coor)-1):
            coord = coor[i], coor[i+1]
            res = client.directions(coord)

            with(open('test.json', '+w')) as f:
                f.write(json.dumps(res, indent=4, sort_keys=True))

                geometry = client.directions(coord)['routes'][0]['geometry']
                decoded = convert.decode_polyline(geometry)
                distance_txt = "<h4> <b>Distance :&nbsp" + "<strong>"+str(round(res['routes'][0]['summary']['distance']/1000,1))+" Km </strong>" +"</h4></b>"
                prix_txt = "<h4> <b>Prix :&nbsp" + "<strong>"+str(pr)+" € </strong>" +"</h4></b>"
                prix_moy_txt = "<h4> <b>Prix Moyenne par KM :&nbsp" + "<strong>"+str(round(moy,3))+" € </strong>" +"</h4></b>"
                folium.GeoJson(decoded).add_child(folium.Popup(distance_txt+prix_txt+prix_moy_txt,max_width = 300)).add_to(m)

                folium.Marker(
                            coord[0][::-1],
                            popup = "<strong>location One</strong>",
                            tooltip = DEPART
                             ).add_to(m)

                folium.Marker(
                            coord[1][::-1],
                            popup = "<strong>location One</strong>",
                            tooltip = ARRIVEE
                             ).add_to(m)
        return m

    elif i > j:

        y = [geo['X'][i],
             geo['Y'][i]]
        
        x = [geo['X'][j],
             geo['Y'][j]]
        moy = pr/Ds
        coor = [x, y]

        client = openrouteservice.Client(key='5b3ce3597851110001cf62486f5564a064e34f3895221e5a0d9a2405')
        m = folium.Map(
                        location=[43.1837661, 3.0042121],
                        zoom_start=10,
                        control_scale=True)

        for i in range(0, len(coor)-1):
            coord = coor[i], coor[i+1]
            res = client.directions(coord)

            with(open('test.json', '+w')) as f:
                f.write(json.dumps(res, indent=4, sort_keys=True))

                geometry = client.directions(coord)['routes'][0]['geometry']
                decoded = convert.decode_polyline(geometry)
                distance_txt = "<h4> <b>Distance :&nbsp" + "<strong>"+str(round(res['routes'][0]['summary']['distance']/1000,1))+" Km </strong>" +"</h4></b>"
                prix_txt = "<h4> <b>Prix :&nbsp" + "<strong>"+str(pr)+" € </strong>" +"</h4></b>"
                prix_moy_txt = "<h4> <b>Prix Moyenne par KM :&nbsp" + "<strong>"+str(round(moy,3))+" € </strong>" +"</h4></b>"
                folium.GeoJson(decoded).add_child(folium.Popup(distance_txt+prix_txt+prix_moy_txt,max_width = 300)).add_to(m)

                folium.Marker(
                            coord[0][::-1],
                            popup = "<strong>location One</strong>",
                            tooltip = ARRIVEE 
                             ).add_to(m)

                folium.Marker(
                            coord[1][::-1],
                            popup = "<strong>location One</strong>",
                            tooltip = DEPART
                             ).add_to(m)
                     
        return m
    
    else :
        print("Veuilliez entrer deux sorties différentes")  

# Affichage de la carte avec la fonction interact
interact(itineraire, DEPART = villes, ARRIVEE = villes)
