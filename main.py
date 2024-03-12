import requests
from datetime import datetime
MY_LAT = 34.052235
MY_LONG = -118.243683

# Used to grab the location of the ISS
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# print(data)
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()['results']
sunrise = data['sunrise'].split("T")[1].split(":")[0]
sunset = data['sunset'].split("T")[1].split(":")[0]
print(sunset)
print(sunrise)

time_now = datetime.now()
print(time_now.hour)


