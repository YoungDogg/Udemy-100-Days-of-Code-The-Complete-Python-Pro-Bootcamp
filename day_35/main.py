import requests
import os
from dotenv import load_dotenv


class Main:
    load_dotenv(".env")

    MY_LAT = -12.463440
    MY_LNG = 130.845642
    my_api:str = os.environ.get("MY_API")
    url= "https://api.openweathermap.org/data/2.5/forecast"
    params = {"lat": MY_LAT,
              "lon": MY_LNG,
              "appid": my_api,
              "cnt": 4
              }

    response = requests.get(url,params)
    response.raise_for_status()
    data = response.json()

    for each_day in data["list"]:
        weather_code = each_day["weather"][0]["id"]
        # print(f"weather code: {weather_code}")
        if weather_code < 700:
            print("Bring an Umbrella")
            break

    # print(data["list"])

if __name__ == "__main__":
    Main()