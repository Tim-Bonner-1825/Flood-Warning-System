from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.station import MonitoringStation


def run():
    """Requirements for Task 1F"""
    # List of Stations
    stations = build_station_list()
    incon = inconsistent_typical_range_stations(stations)

    # Get names of inconsistent stations
    incon_Names = []
    for stat in incon:
        incon_Names.append(stat.name)

    # Sort and print
    incon_Names.sort()
    print(incon_Names)


if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
