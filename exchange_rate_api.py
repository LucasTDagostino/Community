
import json
import requests

url = 'https://api.bluelytics.com.ar/v2/latest'
r = requests.get(url)
r = requests.get(url)
data=json.loads(r.text)
tipo_de_cambio = data['blue']['value_sell']

