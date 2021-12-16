import yfinance as yf

class Investment(object):
    def __init__(self,ticker,volume,Date_of_purchase):
        self.ticker = ticker
        self.volume = volume
        self.Date_of_purchase = Date_of_purchase

    def GetCurrentValue(self,ticker):
        ticker_yahoo = yf.Ticker(ticker)
        data = ticker_yahoo.history()
        return data.tail(1)['Close'].iloc[0]

    def Buy(self):
        print('Bought')

    def Sell(self):
        print('sold')

Inv1 = Investment('AMZN',3,'Dec 4 10:47:14 2021')

# we print the ticker
print(Inv1.ticker)
print(Inv1.volume)
print(Inv1.GetCurrentValue('FB')*Inv1.volume)

