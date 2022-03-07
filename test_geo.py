from tokenize import String
from typing import List, Set, Tuple
from floodsystem.geo import *
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
import random

# TASK 1B:


def test_stations_by_distance():
    """Check that the outputs of stations_by_distance are of the correct type and value"""

    stations = build_station_list()
    p = (52.2053, 0.1218)
    X = stations_by_distance(stations, p)

    # The output must be list
    if type(X) is not list:
        raise TypeError("Output is not a list")

    # Every entry must be tuple
    for entry in X:
        if type(entry) != tuple:
            raise TypeError("At least one entry in the list is not a tuple")

    # Ordered by distance
    for n in range(0, len(X) - 1):
        assert X[n + 1][1] >= X[n][1]

# TASK 1C:


def test_stations_within_radius():
    """Check that the outputs of stations_within_radius are of the correct type"""
    stations = build_station_list()
    p = (52.2053, 0.1218)

    # No stations within a radius of 0
    assert stations_within_radius(stations, p, 0) == []

    # Choose a random radius
    R = random.randint(5, 10000)

    # Output list
    X = stations_within_radius(stations, p, R)

    # Type of the output
    assert type(X) == list

# TASK 1D:


def test_rivers_with_station():
    """Check that the outputs of rivers_with_station are of the correct type"""
    stations = build_station_list()
    # Obtain output
    X = rivers_with_station(stations)

    # Output is of correct type
    assert type(X) == list

    # Type of every entry in the set is correct
    for n in range(0, len(X) - 1):
        assert type(X[n]) == str

    # No duplicate entries
    for entry in X:
        if X.count(entry) > 1:           # Frequency Counter
            raise ValueError("There are duplicate entries in the output")


def test_stations_by_river():
    """Check that the outputs of stations_by_river are of the correct type and value"""
    stations = build_station_list()

    # Obtain output
    X = stations_by_river(stations)

    # Output type
    assert type(X) == dict
    # River Cam is in Cambridge
    assert "Cambridge" in X["River Cam"]

# TASK 1E:


def test_rivers_by_station_number():
    """Check that the outputs of rivers_by_station_number are of the correct type"""
    stations = build_station_list()
    # Obtain output
    N = random.randint(1, 1000)
    X = rivers_by_station_number(stations, N)

    # Type of the output
    assert type(X) == list

    # Alphabetical order
    for n in range(0, len(X) - 1):
        assert X[n + 1][1] <= X[n][1]
    # List is of length N or less
    assert len(X) <= N


def test_rivers_by_station_number():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "station"
    coord = (1, 1)
    trange = None
    river1 = "River 1"
    river2 = "River 2"
    river3 = "River 3"
    river4 = "River 4"
    town = "Town"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river1, town)
    s2 = MonitoringStation(s_id, m_id, label, coord, trange, river2, town)
    s3 = MonitoringStation(s_id, m_id, label, coord, trange, river1, town)
    s4 = MonitoringStation(s_id, m_id, label, coord, trange, river3, town)
    s5 = MonitoringStation(s_id, m_id, label, coord, trange, river2, town)
    s6 = MonitoringStation(s_id, m_id, label, coord, trange, river1, town)
    s7 = MonitoringStation(s_id, m_id, label, coord, trange, river3, town)
    s8 = MonitoringStation(s_id, m_id, label, coord, trange, river4, town)
    stations = [s1, s2, s3, s4, s5, s6, s7, s8]

    assert len(rivers_by_station_number(stations, 1)) == 1

    river_list = rivers_by_station_number(stations, 2)

    # Multiple entries with same number in Nth position
    #assert len(river_list) == 3

    #assert "River 4" not in [item[0] for item in river_list]

    #for river in ["River 1", "River 2", "River 3"]:
       # assert river in [item[0] for item in river_list]