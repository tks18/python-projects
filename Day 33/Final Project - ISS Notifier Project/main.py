import requests
from datetime import datetime

MY_LAT = -37.4174  # 13.058075  # Your latitude
MY_LONG = -47.6710  # 80.265693  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
print(data)

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.
lat_ok = iss_latitude > MY_LAT - 5 and iss_latitude < MY_LAT + 5
long_ok = iss_longitude > MY_LONG - 5 and iss_longitude < MY_LONG + 5

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

if time_now.hour > sunset and time_now.hour < sunrise:
    if lat_ok and long_ok:
        print("Thambi Mela Paaru ")
