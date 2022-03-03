
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels
import datetime

def run():
    """Demonstration task for 2F"""
    # builds and updates a list of stations
    stations = build_station_list()
    update_water_levels(stations)
    # orders the stations by relative water level
    stations = stations_highest_rel_level(stations, 5)

    dt = datetime.timedelta(days=2)
    # plots the water levels and typical range and polynomial
    for station in stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt)
        if len(dates) == 0:
            continue
        plot_water_level_with_fit(station, dates, levels, 4)


if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System***")
    run()