import os
import html
import smtplib
import requests
import itertools
import datetime as dt
from stock_response import response
from dotenv import load_dotenv
load_dotenv("../.env")

print(os.getenv("ALPHAVANTAGE_KEY"))

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# https://www.alphavantage.co/query?}

# stock_params = {
#     "function":"TIME_SERIES_DAILY",
#     "symbol":"TSLA",
#     "interval":"60min",
#     "outputsize":"compact",
#     "apikey":os.getenv("ALPHAVANTAGE_KEY")
# }
#
# response = requests.get("https://www.alphavantage.co/query", params=stock_params)
# response.raise_for_status()
# stock_data = response.json()
today = dt.datetime.now()
yesterday = dt.timedelta(days = 1)
two_days_ago = dt.timedelta(days = 2)
two_days_ago_date = today - two_days_ago
yesterday_date = today - yesterday

time_series = response['Time Series (Daily)']
last_two_days = list(itertools.islice(time_series.items(), 0, 2))
closing_price_yesterday = float(last_two_days[0][1]['4. close'])
closing_price_two_days_ago = float(last_two_days[1][1]['4. close'])

price_diff = closing_price_yesterday - closing_price_two_days_ago
percent_change = abs(price_diff / closing_price_yesterday) * 100
if percent_change > 2:
    # GET NEWS
    news_params = {
        "qInTitle":"tesla",
        "from": two_days_ago_date.strftime("%Y-%m-%d"),
        "sortBy": "publishedAt",
        "language": "en",
        "pageSize": 3,
        "apikey":os.getenv("NEWS_API_KEY")
    }

    news_response = requests.get("https://newsapi.org/v2/everything", params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()
    for article in news_data['articles']:
        print(article['description'])




## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.



# GET https://newsapi.org/v2/everything?q=tesla&from=2024-12-27&sortBy=publishedAt&apiKey={os.getenv("NEWS_API_KEY")}


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

emailContent = "\n".join([f"Headline: {article['title']}\nDescription: {article['description']}\n\n" for article in news_data['articles']])

print(emailContent)

with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.starttls()
    connection.login(user=os.getenv("MY_EMAIL"), password=os.getenv("EMAIL_KEY"))
    connection.sendmail(
        from_addr=os.getenv("MY_EMAIL"),
        to_addrs="budget4you.cc@gmail.com",
        msg=f"Subject:Stock - TESLA NEWS\n\n{emailContent.replace('…', '')}"
    )


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

