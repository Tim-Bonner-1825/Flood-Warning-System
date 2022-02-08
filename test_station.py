# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

# Task 1F:


def test_inconsistent_typical_range_consistent():
    """Check that the outputs of rivers_by_station_number are of the correct type"""
    # create a list with one consistent station and one inconsistent station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s_con = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    trange = None
    s_incon = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    stations = [s_con, s_incon]
    assert len(stations.inconsistent_typical_range_stations(stations)) == 1
