import os
from dotenv import load_dotenv
from stock_price_api import StockPrice
from decimal import Decimal
from news_api import NewsAPI

load_dotenv(".env")

STOCK_API_KEY = os.environ.get("STOCKAPI")
NEWS_API_KEY = os.environ.get("NEWSAPI")
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""TSLA: 🔺2% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey have 
gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings 
show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash. 
or "TSLA: 🔻5% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey 
have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F 
filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus 
market crash."""
class Main:
    """ Main here """
    percentage_change:Decimal = StockPrice(api=STOCK_API_KEY, company=STOCK).run_the_class()
    news:list = NewsAPI(NEWS_API_KEY).get_data()

    # if abs(percentage_change) > 5:
    if abs(percentage_change) < 5:
        print(news)
    else:
        print("it stayed its position")

if __name__ == "__main__":
    Main()
