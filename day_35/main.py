import requests
import os
from dotenv import load_dotenv


class Main:
    load_dotenv(".env")

    MY_LAT = 37.566536
    MY_LNG = 126.977966
    my_api:str = os.environ.get("MY_API")
    url= "https://api.openweathermap.org/data/2.5/weather"
    params = {"lat": MY_LAT,
              "lon": MY_LNG,
              "appid": my_api
              }

    response = requests.get(url,params)
    response.raise_for_status()
    data = response.json()

    print(f"API: {my_api}")
    print(data)


if __name__ == "__main__":
    Main()