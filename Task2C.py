from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_highest_rel_level


def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    highestLevels = stations_highest_rel_level(stations, 10)
    for st in highestLevels:
        print(st.name, st.relative_water_level())


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
