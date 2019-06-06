import requests
import json

#API //df4ec644a21a962a3c101cc85b7be81b//
# http://api.ipstack.com/67.209.129.219?access_key=df4ec644a21a962a3c101cc85b7be81b

# url = 'http://api.ipstack.com/67.209.129.219?access_key=df4ec644a21a962a3c101cc85b7be81b'
# params = {'sensor': 'false', 'address': 'Almaty, KZ'}
# r = requests.get(url, params=params)
# results = r.json()['results']
# location = results[0]['geometry']['location']
# location['lat'], location['lng']

import geocoder
g = geocoder.google('Almaty')
g.latlng
print(g)