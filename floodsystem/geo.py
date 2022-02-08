# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
from os import stat
from haversine import haversine, Unit
from .utils import sorted_by_key
"""This module contains a collection of functions related to
geographical data.

"""


def stations_by_distance(stations, p):
    dist_stat = []
    # Calculate distance from point
    for stat in stations:
        dist_stat.append((stat, haversine(stat.coord, p),))

    # Sort result and return
    result = sorted_by_key(dist_stat, 1)
    return result


def stations_within_radius(stations, centre, r):
    stat_dist = stations_by_distance(stations, centre)
    stats_in_rad = []

    # Check whether distance is less than the radius
    for elem in stat_dist:
        if elem[1] < r:
            stats_in_rad.append(elem[0])

    # Return result
    return stats_in_rad


def rivers_with_station(stations):
    # Collect all river names from stations
    rivers_sts = set([])
    for stat in stations:
        rivers_sts.add(stat.river)
    return sorted(rivers_sts)


def stations_by_river(stations):
    # List of rivers is constructed
    river_stations = {}
    rivers = rivers_with_station(stations)

    # Add stations based off of river
    for r in rivers:
        stat_on_river = []
        for st in stations:
            if st.river == r:
                stat_on_river.append(st)
        river_stations[r] = list(stat_on_river)
    return river_stations


def rivers_by_station_number(stations, N):
    # Create useful lists
    rivers = rivers_with_station(stations)
    stat_riv = stations_by_river(stations)
    riv_num = []

    # Turn list of stations into length of that list and sort
    for riv in rivers:
        riv_num.append((riv, len(stat_riv[riv])))
    riv_num.sort(key=lambda x: x[1], reverse=True)

    # Edge case: N > amount of rivers
    if N > len(riv_num):
        N = len(riv_num)

    return riv_num[:N]
