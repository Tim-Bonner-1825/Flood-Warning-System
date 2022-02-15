from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold


def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    stats_high = stations_level_over_threshold(stations, 0.8)
    for st in stats_high:
        print(st[0].name, st[1])


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
