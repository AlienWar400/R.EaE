import folium
from folium.plugins import MarkerCluster
import pandas as pd
import geocoder
import adb_android
import inspect
import os
import re
import sys
import tempfile
import unittest
import pythonforandroid
import os.path as op
import socket
import bluetooth
#from thread import *

data = pd.read_csv("Volcanoes_USA.txt")
lat = data['LAT']
lon = data['LON']
elevation = data['ELEV']
curGeo = [43.22724, 76.86087]
curGeo2 = [43.21195, 76.86803]
curLat = ['LAT']
curLon = ['LON']

def curCoordinate():
    global curGeo2
    print("Добрый день!")
    curLat = float(input())
    curLon = float(input())
    #print(curLat, curLon)
    curGeo2 = [curLat, curLon]

# def sayGeo(curGeo2 = []):
#     print("curGeo ", float(curGeo2)+"!")
#     findMe()
#
# curGeo = curCoordinate()

def color_change(elev):
    if(elev < 1000):
        return('green')
    elif(1000 <= elev < 3000):
        return('orange')
    else:
        return('red')

#curCoordinate()

if curGeo != curGeo2:
    curGeo = curGeo2
    map = folium.Map(location=curGeo,  # [43.22723, 76.86104],
                     zoom_start=15, zoom_control="false")#, tiles="CartoDB dark_matter")
    folium.Marker(location=curGeo, popup="Me", icon=folium.Icon(color='lightblue')).add_to(map)



marker_cluster = MarkerCluster().add_to(map)

for lat, lon, elevation in zip(lat, lon, elevation):
    folium.CircleMarker(location=[lat, lon],
                        radius = 9, popup=str(elevation)+" m",
                        fill_color=color_change(elevation),
                        color="gray", fill_opacity = 0.9).add_to(marker_cluster)



g = geocoder.ip('me')
print(g.latlng)


#print(curGeo)

map.save("map1.html")



#2 Marks
#[43.2269, 76.86186], [43.2274, 76.86045]