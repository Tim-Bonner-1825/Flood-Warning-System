
from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1B"""
    # Build List of Stations
    stations = build_station_list()

    # Sort important Station values by distance
    stortedStations = stations_by_distance(stations, (52.2053, 0.1218))
    newStats = []
    for s in stortedStations:
        newStats.append((s[0].name, s[0].town, s[1]))

    # Print output
    print("10 closest stations:")
    for x in range(11):
        print(newStats[x])

    print("\n 10 furthest stations:")
    for x in range(-11, -1):
        print(newStats[x])


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
