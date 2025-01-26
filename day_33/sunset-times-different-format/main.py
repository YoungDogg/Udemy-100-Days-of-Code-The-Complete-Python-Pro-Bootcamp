import requests


url = " https://api.sunrise-sunset.org/json"
MY_LAT = -70.967984
MY_LNG = -71.826545
params = {"lat": MY_LAT,
          "lng": MY_LNG,
          "formatted": 0
          }

response = requests.get(url=url, params=params)
response.raise_for_status()

data = response.json()["results"]
sunrise = data["sunset"]
print(sunrise)