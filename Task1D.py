from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1D"""
    # Build list of stations and rivers
    stations = build_station_list()
    rivers = rivers_with_station(stations)
    print(len(rivers), "stations.", "First 10 -", rivers[:10], "\n")

    # Sort stations names by three different rivers and print
    stats_by_river = stations_by_river(stations)
    stats1 = stats_by_river['River Aire']
    for i in range(len(stats1)):
        stats1[i] = stats1[i].name
    print("Stations on the River Aire: \n", sorted(stats1), "\n")

    stats2 = stats_by_river['River Cam']
    for i in range(len(stats2)):
        stats2[i] = stats2[i].name
    print("Stations on the River Cam: \n", sorted(stats2), "\n")

    stats3 = stats_by_river['River Thames']
    for i in range(len(stats3)):
        stats3[i] = stats3[i].name
    print("Stations on the River Thames: \n", sorted(stats3), "\n")


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
