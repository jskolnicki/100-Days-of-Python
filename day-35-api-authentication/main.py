import requests

api_key = '35e1c4eae55e876e0fdf629713b58c2d'

parameters =  {"lat": 47.380932, "lon": -122.234840, 'appid': '35e1c4eae55e876e0fdf629713b58c2d'}


response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params= parameters)
response.raise_for_status()
data=response.json()


no_rain = True
for i in data['hourly'][8:20]:
    if i['weather'][0]['id'] < 700:
        no_rain = False

if no_rain:
    (print("NO RAIN!! :)"))