STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_URL = "https://www.alphavantage.co/query"
NEWS_URL = "https://newsapi.org/v2/top-headlines"

import requests
from env import STOCK_API, NEWS_API


def get_stock_price():
    global STOCK, STOCK_API, STOCK_URL

    parameters = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": STOCK,
        "apikey": STOCK_API,
    }
    stock_request = requests.get(url=STOCK_URL, params=parameters)
    stock_request.raise_for_status()

    stock_price_data = stock_request.json()
    price_data = list(stock_price_data["Time Series (Daily)"].items())
    yesterday_price = float(price_data[0][1]["4. close"])
    prev_yesterday_price = float(price_data[1][1]["4. close"])

    price_change = yesterday_price - prev_yesterday_price
    percent = round((price_change / prev_yesterday_price) * 100)
    return percent


def get_stock_news():
    global COMPANY_NAME, NEWS_API, NEWS_URL

    parameters = {"q": COMPANY_NAME, "apiKey": NEWS_API}

    news_request = requests.get(url=NEWS_URL, params=parameters)
    news_request.raise_for_status()

    news_response = news_request.json()

    articles_dict = []
    if len(news_response["articles"]) > 2:
        for article in news_response["articles"][0:2]:
            articles_dict.append(
                {"headline": article["title"], "brief": article["description"]}
            )
    else:
        for article in news_response["articles"]:
            articles_dict.append(
                {"headline": article["title"], "brief": article["description"]}
            )
    return articles_dict


price_change = get_stock_price()

if price_change > 0:
    news_articles = get_stock_news()
    for article in news_articles:
        print(
            f"\n{COMPANY_NAME} 🔺{price_change}%\nHeadline: {article['headline']}\nBrief: {article['brief']}\n"
        )

if price_change < -5:
    news_articles = get_stock_news()
    for article in news_articles:
        print(
            f"\n{COMPANY_NAME} 🔻{price_change}%\nHeadline: {article['headline']}\nBrief: {article['brief']}\n"
        )