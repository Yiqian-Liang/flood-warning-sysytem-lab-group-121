import numpy as np
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
def polyfit(dates, levels, p):
    x = mdates.date2num(dates)
    Poly = np.poly1d([0])  # Initialize Poly as a zero-degree polynomial
    d0=0
    if len(x)!=0:
        d0=x[0]
        p_coeff = np.polyfit(x-x[0], levels, p)
        Poly=np.poly1d(p_coeff)

    return Poly, d0
