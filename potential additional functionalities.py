import yfinance as yf

class Investment(object):
    def __init__(self,ticker,volume,Date_of_purchase):
        self.ticker = ticker
        self.volume = volume
        self.Date_of_purchase = Date_of_purchase

    def GetCurrentValue(self,ticker):
        ticker_yahoo = yf.Ticker(ticker)
        data = ticker_yahoo.history()
        print(data.tail(1)['Close'].iloc[0])

    def Buy(self):
        print('Bought')

    def Sell(self):
        print('sold')

        dfportfolio = pd.DataFrame([investment1,investment2,investment3,investment4,investment5],columns=["ticker", "volume","Date of Purchase","Average price"])

Inv1 = Investment('FB',10,'Dec 4 10:47:14 2021')

# we print the ticker
print(Inv1.ticker)
print(Inv1.volume)
print(Inv1.GetCurrentValue('AMZN')*Inv1.volume)



nb_entries = []
count = 0

'''
def Add_new_fields():
    max_entries = 20  # we want no more than 20 entries possible
    count = 0
    global count

    if count <= max_entries:
        nb_entries.append(tkinter.ttk.Entry(root_window))
        nb_entries[-1].grid(row=count, column=0, padx=10)
        count += 1

   #We create the button to add new entry fields
    Btn_addstock = tkinter.ttk.Button(first_frame,text='Add a new stock',command=Add_new_fields())
    Btn_addstock.grid(row=50,column=0,padx=10)
'''

'''
    #we create a button to delete a new stock
    Btn_deletestock = tkinter.ttk.Button(first_frame,text='Delete the last stock',command={})
    Btn_deletestock.grid(column=1, row=50, pady=10, padx=10, sticky=(tkinter.W))
'''