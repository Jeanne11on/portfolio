import tkinter
from tkinter import ttk
import datetime as dt
import yfinance as yf
import os
import csv

root_window = tkinter.Tk()
root_window.title('Python portfolio')
root_window.geometry('700x600')

# We initialize the Treeview to hold our portfolio
my_tree = ttk.Treeview(root_window, show='headings')

# We create an csv flat file to store our values in
def create_database():
    global header
    header=['Ticker', 'Volume', 'Purchased at', 'Current value']
    with open('stocks.csv','w',encoding='UTF8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)

# we create a function to get the current share price of a ticker
def Shareprice(ticker):
    ticker_yahoo = yf.Ticker(ticker)
    data = ticker_yahoo.history()
    return data.tail(1)['Close'].iloc[0]

def stamp():
    x = dt.datetime.now()
    return x.strftime("%c")

def CurrentPrice():
    a=Shareprice(Entry_ticker.get())
    b=int(Entry_volume.get())
    return round(a*b,2)

# add an investment to the portfolio
def add_to_portfolio():
    global count
    my_tree.insert(parent='', index='end', iid=count, text='',
                   values=(Entry_ticker.get(), Entry_volume.get(), stamp(), CurrentPrice()))
    count += 1

    # immediately after adding an investment in our treeview, we add our new investment to a our database
    csvdata=[Entry_ticker.get(), Entry_volume.get(), stamp(), CurrentPrice()]
    with open('stocks.csv', 'w', encoding='UTF8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)

    with open('stocks.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(csvdata)

    # We clear the entry widgets automatically when the button is pressed
    Entry_ticker.delete(0, tkinter.END)
    Entry_volume.delete(0, tkinter.END)

# remove one stock
def rmv_from_portfolio():
    x = my_tree.selection()[0]
    my_tree.delete(x)

# clear the portfolio (remove all stocks)
def rmv_all():
    for record in my_tree.get_children():
        my_tree.delete(record)

# Defining columns
my_tree['columns']=('Ticker','Volume','Purchased at','Current value')

# Column_formatting
my_tree.column('#0', anchor=tkinter.W, width=70, stretch=False)
my_tree.column('Ticker', anchor=tkinter.CENTER, width=50)
my_tree.column('Volume', anchor=tkinter.CENTER, width=50)
my_tree.column('Purchased at', anchor=tkinter.CENTER, width=175)
my_tree.column('Current value', anchor=tkinter.CENTER, width=150)

# Heading_formatting
my_tree.heading('#0', text='ID', anchor=tkinter.W)
my_tree.heading('Ticker', text='Ticker', anchor=tkinter.W)
my_tree.heading('Volume', text='Volume', anchor=tkinter.W)
my_tree.heading('Purchased at', text='Purchased at', anchor=tkinter.W)
my_tree.heading('Current value', text='Current value', anchor=tkinter.W)

# We find out if the user already has investments in his portfolio
path_name = 'stocks.csv'

if os.path.exists(path_name):
    # then we read the data from the csv file, and make sure it appears in our treeview
    Old_data = []
else:
    # then we create the database (CSV file)
    create_database()
    Old_data = []

# We insert data in our portfolio
global count
count = 0
for record in Old_data:
    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3]))
    count += 1

# we pack our Tree view onto our frame
my_tree.pack(pady=20, padx=0,fill='y')

# Create frame for new frame
frame_user_input = tkinter.Frame(root_window)
frame_user_input.pack(pady=20)

# widgets_user_input:Labels and entry
Lbl_ticker = tkinter.Label(frame_user_input, text='Ticker')
Lbl_ticker.grid(row=0, column=0)

Lbl_volume = tkinter.Label(frame_user_input, text='Volume')
Lbl_volume.grid(row=0, column=1)

Entry_ticker = tkinter.Entry(frame_user_input, text='Add ticker here...')
Entry_ticker.grid(row=1, column=0)

Entry_volume = tkinter.Entry(frame_user_input, text='Add nb of shares here...')
Entry_volume.grid(row=1, column=1)

# Buttons to add and remove records
Btn_add_record = tkinter.Button(root_window, text='Add to portfolio', command=add_to_portfolio)
Btn_add_record.pack(pady=20)

Btn_rmv_record = tkinter.Button(root_window, text='Remove one selected stock', command=rmv_from_portfolio)
Btn_rmv_record.pack(pady=20)

Btn_rmv_all = tkinter.Button(root_window, text='Clear my portfolio', command=rmv_all)
Btn_rmv_all.pack(pady=20)

# we add this program to the main loop
root_window.mainloop()

