import requests
from twilio.rest import Client
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

#environment variables
load_dotenv()
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
#Twilio
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
RECIPIENT = os.getenv("RECIPIENT")

#get today and yesterday's dates
time_now = datetime.now()
today_date = str(time_now.date())
yesterday_date = str(time_now.date() - timedelta(1))
day_before_yesterday_date = str(time_now.date() - timedelta(2))


#STOCK API
parameters_stocks = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
    "outputsize": "compact",
    "extended_hours": "false",
    "interval": "60min"
}
response = requests.get(STOCK_ENDPOINT, params=parameters_stocks)
response.raise_for_status()
stock_data= response.json()["Time Series (Daily)"]

yesterday_price = float(stock_data[yesterday_date]["4. close"])
day_before_yesterday_price = float(stock_data[day_before_yesterday_date]["4. close"])
percentage_change = (yesterday_price - day_before_yesterday_price) / yesterday_price *100

print(yesterday_price, day_before_yesterday_price, percentage_change)

if percentage_change >= 0:
    change_direction = "up"
else:
    change_direction = ("down"
                        "")

if abs(percentage_change) > 0.05:   #check if there is a change greater than 5%
    #NEWS API-GET NEWS
    news_parameters = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": "Tesla",
        "language": "en",
        "sortBy": "popularity",
        "from": f"{yesterday_date}"

    }
    response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    response.raise_for_status()
    news_data = response.json()
    articles = news_data["articles"]
    #List with top 3 articles
    article_list = articles[:3]
    article_list = [f"Headline: {article['title']}. \n Brief: {article['description']}." for article in article_list]

    #send whatsapp message with top 3 news
    client = Client(account_sid, auth_token)
    for article in article_list:
        message = client.messages.create(
            from_=TWILIO_NUMBER,
            body=f"{STOCK} {change_direction} by 5% \n {article}",
            to=RECIPIENT
        )
        print(message.status)



