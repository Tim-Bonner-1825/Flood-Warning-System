from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1E"""
    # Create list of stations and print number of stations per river
    stations = build_station_list()
    print("First 9 Rivers with the most stations: \n", rivers_by_station_number(stations, 9))


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()
