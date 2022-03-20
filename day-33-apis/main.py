


import requests
import datetime


#Latitude and Longitudes
# https://www.latlong.net/

now = int(datetime.datetime.now().strftime("%H:%M:%S").split(":")[0])

SEATTLE =  {"lat": 47.606209, "lng": -122.332069, 'formatted':0}
PITTSBURGH = {"lat": 40.442169, "lng": -79.994957, 'formatted':0}


#CHOOSE A CITY VARIABLE FROM ABOVE
CITY = SEATTLE



response = requests.get(url='http://api.open-notify.org/iss-now.json')
response.raise_for_status()
data = response.json()

iss_longitude = float(data['iss_position']['longitude'])
iss_latitude = float(data['iss_position']['latitude'])




response = requests.get("https://api.sunrise-sunset.org/json", params=CITY)

response.raise_for_status()

data=response.json()



sunrise=(int(data['results']['sunrise'].split("T")[1].split(":")[0]) + 24 - 8) % 24
sunset=(int(data['results']['sunset'].split("T")[1].split(":")[0]) + 24 - 8) % 24



if (now >= sunrise) and (now <= sunset):
    print('its light out')
elif (abs(iss_latitude - CITY['lat']) <= 5) and (abs(iss_longitude - CITY['lng']) <= 5):
    print("Look up!")
else:
    print("not above")