# Name: Cole Branston
# Date: 2022/07/30
# Purpose: Project which gets the live stock price

from yahoo_fin.stock_info import *
from yahoo_fin import news
import time

def ticker_price():

    ticker = input("\nEnter a ticker symbol: ").upper()
    print("\nLive Price: ", round(get_live_price(ticker),2))

def sp_500():
    for x in tickers_sp500():
        print(x, "=", round(get_live_price(x),2))

def ticker_news():

    ticker = input("\nEnter a ticker symbol: ").upper()

    print("\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Articles".rjust(98))
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        
    time.sleep(1)

    for x in news.get_yf_rss(ticker):

        time.sleep(0.2)

        print("\nArticle: "+str(x["title"])+"\n", "\nSummary: "+str(x["summary"]), "\n\nLink: "+str(x["links"][0]["href"]))
        print("\n----------------------------------------------------------------------------------------------------------------")

while True:

    try:
        print("\nStock Market Info")
        print("-----------------")

        print("\n1. Live Stock Price\n2. S&P 500 Stocks\n3. Stock News\n4. Quit")

        choice = int(input("\nPick an option by number: "))

        if choice == 1:
            ticker_price()

        elif choice == 2:
            sp_500()

        elif choice == 3:
            ticker_news()

        elif choice == 4:
            break

    except:
        print("\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Error".rjust(98))
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        continue