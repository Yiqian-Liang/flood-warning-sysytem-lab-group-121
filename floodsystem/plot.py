import numpy as np
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from .analysis import polyfit
from .datafetcher import fetch_measure_levels
import datetime
def plot_water_level_with_fit(station, dates, levels, p):
    poly, d0 =polyfit(dates,levels, p)#This function returns(poly,d0)
    if len(dates)!=0:
        d = mdates.date2num(dates)
        x1 = np.linspace(min(d), max(d), 191)
        # print(x1)
        # print(poly.c)
        plt.plot(dates, levels,label='water levels')
        plt.plot(x1, poly(x1-d0),'--',label='polyfit for water levels')
        plt.xlabel("Date")
        plt.ylabel("Water Level (m)")
        plt.xticks(rotation=45)
        plt.title(station.name)
        plt.legend()

    # Display plot
        plt.show()
    