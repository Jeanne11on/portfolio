from matplotlib import pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

def pie_chart():
    data = pd.read_csv("stocks.csv")
    i = 0
    labels = []
    values = []
    for data.ticker[i] in data.ticker:
        labels.append(data.ticker[i])
        values.append(data.volume[i])
        i =+1
    # now to get the total number of failed in each section
    actualFigure = plt.figure(figsize = (5,5))
    actualFigure.suptitle("Stocks Pie Chart", fontsize = 22)
    #explode=(0, 0.05, 0, 0)
    # as explode needs to contain numerical values for each "slice" of the pie chart (i.e. every group needs to have an associated explode value)
    explode = list()
    for k in labels:
        explode.append(0.1)
    pie = plt.pie(values, labels=labels, explode=explode, shadow=True, autopct='%1.1f%%')
    plt.legend(pie[0], labels, loc="upper right")
    canvas = FigureCanvasTkAgg(actualFigure)
    canvas.get_tk_widget().grid(second_frame,column=1, row=10, padx=20, pady=5, sticky=(tkinter.N))


def show_total_shares():
 data = pd.read_csv("stocks.csv", names = ('ticker', 'volume','Date of Purchase', 'Average price'))
 volume=0
 i=0
 for data.ticker[i] in data.ticker:
     volume=volume+(data.volume[i])
     i+=1
 lbl_Portfolio = tkinter.Label(second_frame, text=ntick-1, bg='grey')
 lbl_Portfolio.grid(row=1, column=1, sticky='w', pady=2)