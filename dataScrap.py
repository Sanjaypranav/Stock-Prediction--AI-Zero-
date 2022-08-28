import pandas as pd
import yfinance as yf
import yahoofinancials
from yahoofinancials import YahooFinancials


stockName = input("Enter stock name: ")
startTime = input("Enter time period: (year): ")
endTime = input("Enter time period: (month): ")
slidingWindow = input("Enter Sliding Window: (min): ")

# date format = 2022-08-25
# interval = 5m
# stockName = ticker symbol


data = yf.download(stockName, start = startTime, end = endTime, interval = slidingWindow)

type(data)
data.to_csv("IBM.csv")