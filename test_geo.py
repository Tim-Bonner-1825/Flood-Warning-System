from tokenize import String
from typing import List, Set, Tuple
from floodsystem.geo import *
from floodsystem.stationdata import build_station_list
import random

# TASK 1B:


def test_stations_by_distance():
    """Check that the outputs of stations_by_distance are of the correct type and value"""

    stations = build_station_list()
    p = (52.2053, 0.1218)
    X = stations_by_distance(stations, p)

    # The output must be list
    if type(X) != List:
        raise TypeError("Output is not a list")

    # Every entry must be tuple
    for entry in X:
        if type(entry) != Tuple:
            raise TypeError("At least one entry in the list is not a tuple")
            break

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

    # Alphabetical order
    for n in range(0, len(X) - 1):
        assert X[n + 1] >= X[n]

# TASK 1D:


def test_rivers_with_station():
    """Check that the outputs of rivers_with_station are of the correct type"""
    stations = build_station_list()
    # Obtain output
    X = rivers_with_station(stations)

    # Output is of correct type
    assert type(X) == Set

    # Type of every entry in the set is correct
    for n in range(0, len(X) - 1):
        assert type(X[n]) == String

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
        assert X[n + 1][1] >= X[n][1]
    # List is of length N or greater
    assert len(X) >= N
