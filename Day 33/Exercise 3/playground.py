import requests

response = requests.get(
    "https://api.sunrise-sunset.org/json",
    {"lat": 36.7201600, "lng": -4.4203400, "formatted": 0},
)
print(response.json())