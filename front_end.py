import tkinter
import tkinter.ttk
import datetime
import yfinance as yf


# create classes
class Investment(object):
    def __init__(self,ticker,volume,Date_of_purchase,avg_price):
        self.ticker = ticker
        self.volume = volume
        self.Date_of_purchase = Date_of_purchase
        self.avg_price = avg_price

# we populate the start tab
def start_tab_widgets():
    # Create the label for the frame
    first_window_label = tkinter.ttk.Label(first_frame, text='Welcome to your stock portfolio!')
    first_window_label.grid(column=0, row=0, pady=10, padx=10, sticky=(tkinter.W))

    # start_tab functionalities
    lbl_lucky = tkinter.ttk.Label(first_frame,
                                  text='Place your orders below, your portfolio will be generated after you fill in your orders, and click Generate my portfolio')
    lbl_lucky.grid(column=0, row=1, padx=10, sticky=(tkinter.W))
    lbl_insert_stickers = tkinter.ttk.Label(first_frame,text='Insert tickers in this column')
    lbl_insert_stickers.grid(column=0,row=2,pady=10, padx=10, sticky=(tkinter.W))
    lbl_how_many_shares = tkinter.ttk.Label(first_frame,text='How many shares do you want?')
    lbl_how_many_shares.grid(column=1,row=2,pady=10, padx=10, sticky=(tkinter.W))
    lbl_market_value = tkinter.ttk.Label(first_frame,text='Current market value...')
    lbl_market_value.grid(column=3,row=2,pady=10, padx=10, sticky=(tkinter.W))

    E1_tickers = tkinter.ttk.Entry(first_frame)
    E1_tickers.grid(column=0,row=10,pady=10, padx=10, sticky=(tkinter.W))
    E2_tickers = tkinter.ttk.Entry(first_frame)
    E2_tickers.grid(column=0, row=11, pady=10, padx=10, sticky=(tkinter.W))
    E3_tickers = tkinter.ttk.Entry(first_frame)
    E3_tickers.grid(column=0, row=12, pady=10, padx=10, sticky=(tkinter.W))
    E4_tickers = tkinter.ttk.Entry(first_frame)
    E4_tickers.grid(column=0, row=13, pady=10, padx=10, sticky=(tkinter.W))
    E5_tickers = tkinter.ttk.Entry(first_frame)
    E5_tickers.grid(column=0, row=14, pady=10, padx=10, sticky=(tkinter.W))

    E1_nb_of_shares = tkinter.ttk.Entry(first_frame)
    E1_nb_of_shares.grid(column=1,row=10,pady=10, padx=10, sticky=(tkinter.W))
    E2_nb_of_shares = tkinter.ttk.Entry(first_frame)
    E2_nb_of_shares.grid(column=1, row=11, pady=10, padx=10, sticky=(tkinter.W))
    E3_nb_of_shares = tkinter.ttk.Entry(first_frame)
    E3_nb_of_shares.grid(column=1, row=12, pady=10, padx=10, sticky=(tkinter.W))
    E4_nb_of_shares = tkinter.ttk.Entry(first_frame)
    E4_nb_of_shares.grid(column=1, row=13, pady=10, padx=10, sticky=(tkinter.W))
    E5_nb_of_shares = tkinter.ttk.Entry(first_frame)
    E5_nb_of_shares.grid(column=1, row=14, pady=10, padx=10, sticky=(tkinter.W))

    #this records a time stamp when we print the user output
    x = datetime.datetime.now()
    stamp = x.strftime("%c")

    def get_current_price(symbol):
        ticker = yf.Ticker(symbol)
        todays_data = ticker.history(period='1d')
        return todays_data['Close'][0]

    def print_userinput():
        #this function aggregates both the ticker and the number of shares, as of now it's printed, but wont be in the final result
        investment1=E1_tickers.get()+','+E1_nb_of_shares.get()+','+stamp
        investment2=E2_tickers.get()+','+E2_nb_of_shares.get()+','+stamp
        investment3=E3_tickers.get()+','+E3_nb_of_shares.get()+','+stamp
        investment4=E4_tickers.get()+','+E4_nb_of_shares.get()+','+stamp
        investment5=E5_tickers.get()+','+E5_nb_of_shares.get()+','+stamp
        userinput=investment1+investment2+investment3+investment4+investment5
        lbl_userinput = tkinter.ttk.Label(first_frame,text=userinput)
        lbl_userinput.grid(column=1,row=98,pady=10, padx=10, sticky=(tkinter.W))


    #we create a button to output user input
    Btn_ticker_value=tkinter.ttk.Button(first_frame,text='Generate my portfolio',command=print_userinput)
    Btn_ticker_value.grid(column=0,row=90,pady=10, padx=10, sticky=(tkinter.W))

    # Create the buttons to move frames and exit
    first_window_quit_button = tkinter.Button(first_frame, text = "Quit", command = quit_program)
    first_window_quit_button.grid(column=0, row=100, padx=10,pady=10, sticky=(tkinter.W))
    first_window_next_button = tkinter.Button(first_frame, text = "Next", command = call_second_frame_on_top)
    first_window_next_button.grid(column=1, row=100, padx=10,pady=10, sticky=(tkinter.W))

'''
    #we initiate the five investments
    Investment1=Investment(E1_tickers.get(),E1_nb_of_shares.get(),stamp,get_current_price(E1_tickers))
    Investment2=Investment(E2_tickers.get(),E2_nb_of_shares.get(),stamp,get_current_price(E2_tickers))
    Investment3=Investment(E3_tickers.get(),E3_nb_of_shares.get(),stamp,get_current_price(E3_tickers))
    Investment4=Investment(E4_tickers.get(),E4_nb_of_shares.get(),stamp,get_current_price(E4_tickers))
    Investment5=Investment(E5_tickers.get(),E5_nb_of_shares.get(),stamp,get_current_price(E5_tickers))
'''
def portfolio_widgets():
    # Create the label for the frame
    second_window_label = tkinter.ttk.Label(second_frame, text='Portfolio')
    second_window_label.grid(column=0, row=0, pady=10, padx=10, sticky=(tkinter.W))

    # Create the button for the frame
    second_window_back_button = tkinter.Button(second_frame, text = "Back", command = call_first_frame_on_top)
    second_window_back_button.grid(column=0, row=10, pady=10, sticky=(tkinter.W))
    second_window_next_button = tkinter.Button(second_frame, text = "Next", command = call_third_frame_on_top)
    second_window_next_button.grid(column=1, row=10, pady=10, sticky=(tkinter.W))

    #insert porfolio functionalities here
    #first we populate with the portfolio
    lbl_Portfolios_title = tkinter.Label(second_frame, text="Portfolios", bg='orange')
    lbl_Portfolios_title.grid(row=4, column=0, sticky='w', pady=2)
    lbl_Portfolio = tkinter.Label(second_frame, text="Portfolio", bg='orange')
    lbl_Portfolio.grid(row=5, column=0, sticky='w', pady=2)
    lbl_Last = tkinter.Label(second_frame, text="Last", bg='orange')
    lbl_Last.grid(row=5, column=1, sticky='w', pady=2)
    lbl_Change = tkinter.Label(second_frame, text="Change", bg='orange')
    lbl_Change.grid(row=5, column=2, sticky='w', pady=2)
    lbl_Unrealised = tkinter.Label(second_frame, text="Unrealised Gain/Loss", bg='orange')
    lbl_Unrealised.grid(row=5, column=3, sticky='w', pady=2)
    lbl_Total_Return = tkinter.Label(second_frame, text="Total Return", bg='orange')
    lbl_Total_Return.grid(row=5, column=4, sticky='w', pady=2)
    lbl_name_portfolio = tkinter.Label(second_frame, text="Needs work", bg='orange')
    lbl_name_portfolio.grid(row=6, column=0, sticky='w', pady=2)
    lbl_Last_inEUR = tkinter.Label(second_frame, text="Needs work", bg='orange')
    lbl_Last_inEUR.grid(row=6, column=1, sticky='w', pady=2)
    lbl_Change_inper = tkinter.Label(second_frame, text="Needs work", bg='orange')
    lbl_Change_inper.grid(row=6, column=2, sticky='w', pady=2)
    lbl_Unrealized_inEUR = tkinter.Label(second_frame, text="Needs work", bg='orange')
    lbl_Unrealized_inEUR.grid(row=6, column=3, sticky='w', pady=2)
    lbl_Total_ReturninEUR = tkinter.Label(second_frame, text="Needs work", bg='orange')
    lbl_Total_ReturninEUR.grid(row=6, column=4, sticky='w', pady=2)

    # we populate the Portfolio movers section of the second frame
    lbl_Port_movers_title = tkinter.Label(second_frame, text="Portfolio Movers", bg='green')
    btn1 = tkinter.Button(second_frame, text='I want to see my gainers', bd='5', command=())
    btn2 = tkinter.Button(second_frame, text='I want to see my losers', bd='5', command=())

    # We grid the Portfolio movers part
    lbl_Port_movers_title.grid(row=7, column=0, sticky='w', pady=2)
    btn1.grid(row=8, column=0)
    btn2.grid(row=8, column=1)

def reco_widgets():
    # Create the label for the frame
    third_window_label = tkinter.ttk.Label(third_frame, text='Recommendation tab')
    third_window_label.grid(column=0, row=0, pady=10, padx=10, sticky=(tkinter.N))

    # Create the button for the frame
    third_window_back_button = tkinter.Button(third_frame, text = "Back", command = call_second_frame_on_top)
    third_window_back_button.grid(column=0, row=1, pady=10, sticky=(tkinter.N))
    third_window_quit_button = tkinter.Button(third_frame, text = "Quit", command = quit_program)
    third_window_quit_button.grid(column=1, row=1, pady=10, sticky=(tkinter.N))

def call_first_frame_on_top():
    # This function can be called only from the second window.
    # Hide the second window and show the first window.
    second_frame.grid_forget()
    first_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

def call_second_frame_on_top():
    # This function can be called from the first and third windows.
    # Hide the first and third windows and show the second window.
    first_frame.grid_forget()
    third_frame.grid_forget()
    second_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

def call_third_frame_on_top():
    # This function can only be called from the second window.
    # Hide the second window and show the third window.
    second_frame.grid_forget()
    third_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

def quit_program():
    root_window.destroy()

# we run the main program now

# Create the root GUI window.
root_window = tkinter.Tk()
root_window.title('Stock portfolio')

# Define window size
window_width = 300
window_heigth = 100

# Create frames inside the root window to hold other GUI elements. All frames must be created in the main program, otherwise they are not accessible in functions.
first_frame=tkinter.ttk.Frame(root_window, width=window_width, height=window_heigth)
first_frame['borderwidth'] = 2
first_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.W, tkinter.E))

second_frame=tkinter.ttk.Frame(root_window, width=window_width, height=window_heigth)
second_frame['borderwidth'] = 2
second_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.W, tkinter.E))

third_frame=tkinter.ttk.Frame(root_window, width=window_width, height=window_heigth)
third_frame['borderwidth'] = 2
third_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.W, tkinter.E))

# Create all widgets to all frames
reco_widgets()
portfolio_widgets()
start_tab_widgets()

# Hide all frames in reverse order, but leave first frame visible (unhidden).
third_frame.grid_forget()
second_frame.grid_forget()

# Start tkinter event - loop
root_window.mainloop()