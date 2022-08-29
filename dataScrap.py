import pandas as pd
import yfinance as yf
import yahoofinancials
from yahoofinancials import YahooFinancials
import datetime

def add_a_day(startTime):
    date = startTime.split('-')[2]
    date = int(date) + 1
    startTime = startTime.replace(startTime.split('-')[2], str(date))
    return  startTime

stockName = input("Enter stock name: ")

startTime , endTime = add_a_day(input("Enter start time period: (year-month-date)(# date format = 2022-08-25): ")) , add_a_day(input("Enter end time period: (year-month-date)(# date format = 2022-08-25): "))
slidingWindow = input("Enter Sliding Window: (min): ") + 'm'

# date format = 2022-08-25
# interval = 5m
# stockName = ticker symbol


data = yf.download(stockName, start = startTime, end = endTime, interval = slidingWindow)

type(data)
data.to_csv(f"{stockName}.csv")