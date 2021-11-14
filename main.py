import tkinter as tk

#we create a window
portfolio = tk.Tk()
portfolio.geometry('600x400')

#Portfolio title
lbl_Portfolio = tk.Label(portfolio, text = "Portfolio")
lbl_Portfolio.grid(row = 0, column = 0, sticky = 'w', pady = 2)

#we arrange the dashboard

#first we create the dashboard section
lbl_Dashboard = tk.Label(portfolio, text = "Dashboard")
lbl_total_value = tk.Label(portfolio, text = "Total Value (EUR)")
lbl_value_change = tk.Label(portfolio, text = "Value Change")
lbl_total_gain_loss = tk.Label(portfolio, text = "Total Gain/Loss")
lbl_total_value_in_euros = tk.Label(portfolio, text = "Needs work")
lbl_value_change_inper = tk.Label(portfolio, text = "Needs work")
lbl_gainloss_inper = tk.Label(portfolio, text = "Needs work")
btn_refresh = tk.Button(portfolio, text = 'Refresh data', bd = '5',command = portfolio.destroy)

#we grid the dashboard
lbl_Dashboard.grid(row = 1, column = 0, sticky = 'w', pady = 2)
lbl_total_value.grid(row = 2, column = 0, sticky = 'w', pady = 2)
lbl_value_change.grid(row = 2, column = 1, sticky = 'w', pady = 2)
lbl_total_gain_loss.grid(row = 2, column = 2, sticky = 'w', pady = 2)
lbl_total_value_in_euros.grid(row = 3, column = 0, sticky = 'w', pady = 2)
lbl_value_change_inper.grid(row = 3, column = 1, sticky = 'w', pady = 2)
lbl_gainloss_inper.grid(row = 3, column = 2, sticky = 'w', pady = 2)
btn_refresh.grid(row=1,column=1,sticky = 'w',pady=2)

#Second we create the Portfolios labels, then we add the computations
lbl_Portfolios_title = tk.Label(portfolio, text = "Portfolios")
lbl_Portfolio = tk.Label(portfolio, text = "Portfolio")
lbl_Last = tk.Label(portfolio, text = "Last")
lbl_Change = tk.Label(portfolio, text = "Change")
lbl_Unrealised = tk.Label(portfolio, text = "Unrealised Gain/Loss")
lbl_Total_Return = tk.Label(portfolio, text = "Total Return")
lbl_name_portfolio = tk.Label(portfolio, text = "Needs work")
lbl_Last_inEUR = tk.Label(portfolio, text = "Needs work")
lbl_Change_inper = tk.Label(portfolio, text = "Needs work")
lbl_Unrealized_inEUR = tk.Label(portfolio, text = "Needs work")
lbl_Total_ReturninEUR = tk.Label(portfolio, text = "Needs work")

#we grid the Portfolios
lbl_Portfolios_title.grid(row = 4, column = 0, sticky = 'w', pady = 2)
lbl_Portfolio.grid(row = 5, column = 0, sticky = 'w', pady = 2)
lbl_Last.grid(row = 5, column = 1, sticky = 'w', pady = 2)
lbl_Change.grid(row = 5, column = 2, sticky = 'w', pady = 2)
lbl_Unrealised.grid(row = 5, column = 3, sticky = 'w', pady = 2)
lbl_Total_Return.grid(row = 5, column = 4, sticky = 'w', pady = 2)
lbl_name_portfolio.grid(row = 6, column = 0, sticky = 'w', pady = 2)
lbl_Last_inEUR.grid(row = 6, column = 1, sticky = 'w', pady = 2)
lbl_Change_inper.grid(row = 6, column = 2, sticky = 'w', pady = 2)
lbl_Unrealized_inEUR.grid(row = 6, column = 3, sticky = 'w', pady = 2)
lbl_Total_ReturninEUR.grid(row = 6, column = 4, sticky = 'w', pady = 2)

#we populate the Portfolio movers section
lbl_Port_movers_title = tk.Label(portfolio, text = "Portfolio Movers")
btn1 = tk.Button(portfolio, text = 'I want to see my gainers', bd = '5',command = portfolio.destroy)
btn2 = tk.Button(portfolio, text = 'I want to see my losers', bd = '5',command = portfolio.destroy)

#We grid the Portfolio movers part
lbl_Port_movers_title.grid(row = 7, column = 0, sticky = 'w', pady = 2)
btn1.grid(row=8,column=0)
btn2.grid(row=8,column=1)

#the main functions we'll need
'''Dashboard:
A task for Leonardo, you need to create a function that calls the yfinance API and
updates the values of the app when the button "refresh data" is clicked'''

#We add the app window in the main loop, if we are running the main module
if __name__ == "__main__":
    portfolio.mainloop()