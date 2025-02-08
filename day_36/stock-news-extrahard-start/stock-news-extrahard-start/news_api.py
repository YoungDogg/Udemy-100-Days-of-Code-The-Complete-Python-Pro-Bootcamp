import requests


class NewsAPI:
    """
    get news from newsapi.org
    """
    def __init__(self,my_api):
        self.api = my_api

    def get_data(self):
        url = "https://newsapi.org/v2/top-headlines"
        params = {
            "q": "tesla",
            "apiKey": self.api
        }

        response = requests.get(url, params=params)
        data = response.json()
        return [(row.get("title", "no title"), row.get("description", "no description "))
                for row in data.get("articles", [])]


if __name__ == "__main__":
    import os
    from dotenv import load_dotenv


    load_dotenv(".env")
    my_api:str = os.environ.get("NEWSAPI")
    news = NewsAPI(my_api).get_data()
    print(news)