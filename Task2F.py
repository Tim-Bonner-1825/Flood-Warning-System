
from floodsystem.stationdata import update_water_levels
from floodsystem.stationdata import build_station_list
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib as mpl
import numpy as np
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit


def run():

    stations = build_station_list()
    update_water_levels(stations)

    flooded_list_x = stations_highest_rel_level(stations, 10)

    flooded_list = []

    for station in stations:
        for i in range(1,5):
            if (flooded_list_x[i][0]).name == station.name:
                flooded_list.append(station)


    for station in flooded_list:
        dates = fetch_measure_levels(station.measure_id)   
        levels = fetch_measure_levels(dt = timedelta(days = 5))
        plot_water_level_with_fit(station,dates,levels, 4)
        plt.show()


if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()

