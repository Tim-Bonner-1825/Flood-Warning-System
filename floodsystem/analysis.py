
import numpy as np
import matplotlib as mpl
from datetime import datetime, timedelta
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
import matplotlib.pyplot as plt

def polyfit(dates, levels, p):
    
    days = mpl.dates.date2num(dates)
    d0 = np.min(days)
    x = days - d0
    y = levels

    # Find coefficients of best-fit polynomial f(x) of degree 4
    p_coeff = np.polyfit(x, y, p)
    # Convert coefficient into a polynomial that can be evaluated,
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)

    return d0, poly
