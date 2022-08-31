from ast import arg
from email.policy import default
import pandas as pd
import yfinance as yf
import yahoofinancials
from yahoofinancials import YahooFinancials
import datetime
import argparse

def add_a_day(startTime):
    date = startTime.split('-')[2]
    date = int(date) + 1
    startTime = startTime.replace(startTime.split('-')[2], str(date))
    return  startTime


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='For Scrapping stock data')
    parser.add_argument('--StartTime',help='Enter start time period: (year-month-date)(# date format = 2022-08-25):',required=True)
    parser.add_argument('--EndTime',help='Enter start time period: (year-month-date)(# date format = 2022-08-25):',required=True)
    parser.add_argument('--window',help ='Window Size',default = '5m')
    parser.add_argument('--Name',help='Enter Stock Name that you want to fetch (AAPL)',default='AAPL')
    args = parser.parse_args()
    startTime , endTime = args.StartTime , args.EndTime
    slidingWindow = args.window
    stockName = args.Name 
    # From user input 
    '''
    stockName = input("Enter stock name: ")
    startTime , endTime = add_a_day(input("Enter start time period: (year-month-date)(# date format = 2022-08-25): ")) , add_a_day(input("Enter end time period: (year-month-date)(# date format = 2022-08-25): "))
    slidingWindow = input("Enter Sliding Window: (min): ") + 'm'
    '''
    # date format = 2022-08-25
    # interval = 5m
    # stockName = ticker symbol


    data = yf.download(stockName, start = startTime, end = endTime, interval = slidingWindow)

    type(data)
    data.to_csv("/run/media/pranav/3CDEB4E6DEB4999A/Projects/Stock-Prediction--AI-Zero-/Data/AAPL.csv")