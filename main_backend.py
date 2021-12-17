import yfinance as yf
import pandas as pd
import numpy as np
import csv
import os
import mplfinance as mpf

#the function show whether the csv file given as argument is empty or not (true = empty, false = not empty)
def is_empty_csv(file):
    with open(file) as csvfile:
        reader = csv.reader(csvfile)
        for i, _ in enumerate(reader):
            if i:  # found the second row
                return False
    return True

#the function creates the stocks database (csv file named "stocks.csv") which catalogs all the stocks owned by the user 
#if the file exists the function stops    
def create_database():
   Path = os.path.isfile('stocks.csv')
   if Path==False:
    with open('stocks.csv', 'x',  newline='') as file:
     writer = csv.writer(file)
     writer.writerow(["ticker", "volume","Date of Purchase","Average price"])
   else:
      return

#this function allows the user to add new stocks to the database and add or remove a certain 
#amount of volume of a stock
#the csv library does not have a specific function which does so, so we used a function of the panda library in order to
#read the csv file and rewrite it with the new modifications using csv library. Without using this method the most common
#way to resolve this issue is creating another excel file where temporarly copying the old file but we find this
#solutions too complicated.
def update_data(ticker, volume, purchase_date, avgprice):
   data = pd.read_csv("stocks.csv", names = ('ticker', 'volume','Date of Purchase', 'Average price'))
   nrows = 0
   for index, row in data.iterrows():
       nrows+=1
   with open('stocks.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    i = 0
    for index, row in data.iterrows():
     if row.ticker != ticker:
       writer.writerow(row)
       i+=1
     elif row.ticker == ticker:
       newvolume = int(volume) + int(row.volume)
       writer.writerow([ticker, newvolume, purchase_date, avgprice])
    if i == nrows:
        writer.writerow([ticker, volume, purchase_date, avgprice])

#this function allows to delete stocks from the portfolio 
def delete_data(ticker):
 data = pd.read_csv("stocks.csv", names = ('ticker', 'volume'))
 with open('stocks.csv', 'w', newline='') as file:
   writer = csv.writer(file)
   for index, row in data.iterrows():
    if row.ticker != ticker:
       writer.writerow(row)
    else:
       return  

#this function gives the current price of the stocks included in the stocks database
def currentstocksdata():
   data = pd.read_csv("stocks.csv")
   j = 0
   for data.ticker[j] in data.ticker:
      j+=1
   i = 0
   todaydata = pd.DataFrame(index=np.arange(j), columns=np.arange(3))
   todaydata.columns = ['tick', 'volume', 'currentprice']
   for data.ticker[i] in data.tick:
      stock = yf.ticker(data.ticker[i])
      currentdata = stock.history(period = "1d")
      todaydata.ticker[i] = data.ticker[i]
      todaydata.volume[i] = data.volume[i]
      todaydata.currentprice[i] = currentdata['Close'][0]
      i+=1
   return todaydata

#this function retrieve historical price values in a gived period
def analyse_stock(stock, period):
   stockdata = yf.ticker(stock)
   #period could be 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y or ytd (all history)
   hist = stockdata.history(period=period)
   ##### for Leo: see if we can integrate with flask interface ######
   mpf.plot(hist, type = 'line', title = (stock + " " + period + " graph")) #this line plot a simple graph to show stokc trends
   return hist

#this function gives general information about the stock inserted: a description of the company, its market cap
#and the number of employees
def info_stock(stock):
    stockdata = yf.ticker(stock)
    stockinfo = stockdata.info
    marketcap = stockinfo['marketCap']
    employees = stockinfo['fullTimeEmployees']
    sector = stockinfo['sector']
    business_summary = stockinfo['longBusinessSummary']
    finaldata = pd.DataFrame(index=np.arange(4), columns=np.arange(1))
    finaldata.index = ['market_cap', 'employees', 'sector', 'business_summary']
    finaldata.columns = ['informations']
    finaldata.informations['market_cap'] = marketcap
    finaldata.informations['employees'] = employees
    finaldata.informations['sector'] = sector
    finaldata.informations['business_summary'] = business_summary
    return finaldata
   
def get_current_price(symbol):
        ticker = yf.Ticker(symbol)
        todays_data = ticker.history(period='1d')
        return todays_data['Close'][0]

#this function suggests the user to buy or to sell a stock retreiving informations trhough recommendation method
#of yfinance library. This method gives a list of advices from important financial institutions. the function takes into account
#only the Sell or Buy advices, counts them and verifies if there are more Buy advices than Sell and viceversa.
#If the result is uncertain it gives back the string "recommendations are not clear go into a deeper analysis to decide what to do"
def recommendations_stock(stock):
    stockdata = yf.Ticker(stock)
    stockrec = stockdata.recommendations
    data = pd.DataFrame(stockrec)
    data.columns = ['firm', 'tograde', 'fromgrade', 'action']
    i = 0 
    buy = 0
    sell = 0
    for data.firm[i] in data.firm:
       if data.tograde[i]  == "Buy":
          buy +=1
       if data.tograde[i] == "Sell":
          sell +=1
       i+=1
    if buy > sell + 4:
       return "buy the stock"
    elif sell > buy + 3: 
       return "sell the stock"
    else:
       return "recommendations are not clear go into a deeper analysis to decide what to do"
