import requests
import env

base_url = "https://api.openweathermap.org/data/2.5/onecall"

data_params = {
    "appid": env.OWM_KEY,
    "lat": 80.2785,
    "lon": 13.0878,
    "exclude": "daily,current,minutely",
}

response = requests.get(url=base_url, params=data_params)
response.raise_for_status()

weather_data = response.json()
hourly_data = weather_data["hourly"]

for hour in hourly_data[:12]:
    hourly_weather_id = hour["weather"][0]["id"]
    if hourly_weather_id < 700:
        print("Will Rain")
        break
    else:
        print("no Rain")