import requests
import time
from decimal import Decimal, ROUND_DOWN


class StockPrice:
    def __init__(self, company, api):
        self.api_key = api
        self.company = company
        self.yesterday: str = ""
        self.two_days_ago: str = ""
        self.yesterday_open_price: str = ""
        self.two_days_ago_close_price: str = ""
        self.daily_data: dict = {}
        self.daily_percentage_change: Decimal = Decimal()

    def run_the_class(self):
        self.get_data()
        self.change_time_format()
        return self.get_daily_percentage_change()
        # self.print_get_news()

    def get_data(self):
        url = "https://www.alphavantage.co/query"
        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": self.company,
            "apikey": self.api_key
        }

        response = requests.get(url, params)
        response.raise_for_status()
        data = response.json()
        self.daily_data = data["Time Series (Daily)"]

    def change_time_format(self):
        # get the current day and yesterday. But current day isn't available. Get the data 2 days ago
        yesterday_timestamp = time.time() - 86400
        two_days_ago_timestamp = time.time() - (86400 * 2)
        self.yesterday = time.strftime("%Y-%m-%d", time.localtime(yesterday_timestamp))
        self.two_days_ago = time.strftime("%Y-%m-%d", time.localtime(two_days_ago_timestamp))

        # get yesterday and two days ago data from the API
        for day in self.daily_data:
            if day == self.yesterday:
                self.yesterday_open_price = float(self.daily_data[day]["1. open"])
            if day == self.two_days_ago:
                self.two_days_ago_close_price = float(self.daily_data[day]["4. close"])

    # if the price went 5% up or down, get news
    def get_daily_percentage_change(self):
        daily_percentage_change = Decimal(
            (self.yesterday_open_price - self.two_days_ago_close_price) / self.two_days_ago_close_price
            * 100)
        truncated = daily_percentage_change.quantize(Decimal('0.1'), rounding=ROUND_DOWN)

        self.daily_percentage_change = truncated

        print(f"daily_percentage_change: {truncated}%")
        return self.daily_percentage_change

    def print_get_news(self):
        if abs(self.daily_percentage_change) > 5:
            print("get news")
        else:
            print("it stayed its position")


if __name__ == "__main__":
    import os
    from dotenv import load_dotenv

    load_dotenv(".env")
    API_KEY = os.environ.get("STOCKAPI")

    s = StockPrice(api=API_KEY, company="TSLA")
    s.run_the_class()
