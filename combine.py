#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

# Creates three "windows" that the user can navigate through using Back and Next - buttons.

import tkinter
import tkinter.ttk

# we
def start_tab_widgets():
    # Create the label for the frame
    first_window_label = tkinter.ttk.Label(first_frame, text='You\'re a lucky guy/gal!')
    first_window_label.grid(column=0, row=0, pady=10, padx=10, sticky=(tkinter.W))

    # start_tab functionalities
    lbl_lucky = tkinter.ttk.Label(first_frame,
                                  text='Today we offer you the opportunity to invest in the stock market')
    lbl_lucky.grid(column=0, row=1,pady=10, padx=10, sticky=(tkinter.W))
    E_tickers = tkinter.ttk.Entry(first_frame)
    E_tickers.grid(column=0,row=3,pady=10, padx=10, sticky=(tkinter.W))
    ticker_value=E_tickers.get()
    lbl_insert_stickers = tkinter.ttk.Label(first_frame,text='Insert tickers in this column')
    lbl_insert_stickers.grid(column=0,row=2,pady=10, padx=10, sticky=(tkinter.W))
    lbl_how_many_shares = tkinter.ttk.Label(first_frame,text='How many shares do you want?')
    lbl_how_many_shares.grid(column=1,row=2,pady=10, padx=10, sticky=(tkinter.W))
    E_nb_of_shares = tkinter.ttk.Entry(first_frame)
    E_nb_of_shares.grid(column=1,row=3,pady=10, padx=10, sticky=(tkinter.W))

    def print_userinput():
        #this function aggregates both the ticker and the number of shares, as of now it's printed, but wont be in the final result
        tickert=tkinter.Label(first_frame,text=(E_tickers.get()+'-'+E_nb_of_shares.get()))
        tickert.grid(column=1,row=9,pady=10, padx=10, sticky=(tkinter.W))

    Btn_ticker_value=tkinter.ttk.Button(first_frame,text='Print',command=print_userinput)
    Btn_ticker_value.grid(column=0,row=9,pady=10, padx=10, sticky=(tkinter.W))

    # Create the buttons to move frames and exit
    first_window_quit_button = tkinter.Button(first_frame, text = "Quit", command = quit_program)
    first_window_quit_button.grid(column=0, row=10, pady=10, sticky=(tkinter.W))
    first_window_next_button = tkinter.Button(first_frame, text = "Next", command = call_second_frame_on_top)
    first_window_next_button.grid(column=1, row=10, pady=10, sticky=(tkinter.W))

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

###############################
# Main program starts here :) #
###############################

# Create the root GUI window.
root_window = tkinter.Tk()
root_window.title('Stock portfolio')

# Define window size
window_width = 200
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