import requests

req = requests.get("https://sample.api.com")

res = req.json()

print(res["json"])