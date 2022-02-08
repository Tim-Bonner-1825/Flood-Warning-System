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
    for stat in stations:
        dist_stat.append((stat, haversine(stat.coord, p),))
    result = sorted_by_key(dist_stat, 1)
    return result


def stations_within_radius(stations, centre, r):
    stat_dist = stations_by_distance(stations, centre)
    stats_in_rad = []
    for elem in stat_dist:
        if elem[1] < r:
            stats_in_rad.append(elem[0])
    return stats_in_rad


def rivers_with_station(stations):
    rivers_sts = set([])
    for stat in stations:
        rivers_sts.add(stat.river)
    return sorted(rivers_sts)


def stations_by_river(stations):
    river_stations = {}
    rivers = rivers_with_station(stations)
    for r in rivers:
        stat_on_river = []
        for st in stations:
            if st.river == r:
                stat_on_river.append(st)
        river_stations[r] = list(stat_on_river)
    return river_stations


def rivers_by_station_number(stations, N):
    rivers = rivers_with_station(stations)
    stat_riv = stations_by_river(stations)
    riv_num = []
    for riv in rivers:
        riv_num.append((riv, len(stat_riv[riv])))
    riv_num.sort(key=lambda x: x[1], reverse=True)
    return riv_num[:N]
