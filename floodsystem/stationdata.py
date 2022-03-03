#Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides interface for extracting statiob data from
JSON objects fetched from the Internet and

"""

import datetime

import matplotlib

from floodsystem.analysis import polyfit
from floodsystem.utils import sorted_by_key
from . import datafetcher
from .station import MonitoringStation


def build_station_list(use_cache=True):
    """Build and return a list of all river level monitoring stations
    based on data fetched from the Environment agency. Each station is
    represented as a MonitoringStation object.

    The available data for some station is incomplete or not
    available.

    """

    # Fetch station data
    data = datafetcher.fetch_station_data(use_cache)

    # Build list of MonitoringStation objects
    stations = []
    for e in data["items"]:
        # Extract town string (not always available)
        town = None
        if 'town' in e:
            town = e['town']

        # Extract river name (not always available)
        river = None
        if 'riverName' in e:
            river = e['riverName']

        # Attempt to extract typical range (low, high)
        try:
            typical_range = (float(e['stageScale']['typicalRangeLow']),
                             float(e['stageScale']['typicalRangeHigh']))
        except Exception:
            typical_range = None

        try:
            # Create mesure station object if all required data is
            # available, and add to list
            s = MonitoringStation(
                station_id=e['@id'],
                measure_id=e['measures'][-1]['@id'],
                label=e['label'],
                coord=(float(e['lat']), float(e['long'])),
                typical_range=typical_range,
                river=river,
                town=town)
            stations.append(s)
        except Exception:
            # Not all required data on the station was available, so
            # skip over
            pass

    return stations


def update_water_levels(stations):
    """Attach level data contained in measure_data to stations"""

    # Fetch level data
    measure_data = datafetcher.fetch_latest_water_level_data()

    # Build map from measure id to latest reading (value)
    measure_id_to_value = dict()
    for measure in measure_data['items']:
        if 'latestReading' in measure:
            latest_reading = measure['latestReading']
            measure_id = latest_reading['measure']
            measure_id_to_value[measure_id] = latest_reading['value']

    # Attach latest reading to station objects
    for station in stations:

        # Reset latestlevel
        station.latest_level = None

        # Atach new level data (if available)
        if station.measure_id in measure_id_to_value:
            if isinstance(measure_id_to_value[station.measure_id], float):
                station.latest_level = measure_id_to_value[station.measure_id]



def flood_risk_assessment(stations):
    """Classifies the stations according to risk of flooding. Returns list of tuples (name, risk level, score)"""
    stations_and_risk = []
    for station in stations:
        # Get polynomial fit
        dates, levels = datafetcher.fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=2))
        if dates != [] and levels != []:
            poly, d0 = polyfit(dates, levels, 4)

            # Check if level is rising or falling (comparing now and now + 12h)
            x = matplotlib.dates.date2num(dates[-1])
            r = poly(x - d0 + 0.5) > 1.1 * poly(x - d0)
            f = poly(x - d0 + 0.5) < 0.9 * poly(x - d0)

            # Use rising/falling as a scaling factor on relative
            if r:
                scaling_factor = 1.2
            elif f:
                scaling_factor = 0.8
            else:
                scaling_factor = 1

            try:
                score = station.relative_water_level() * scaling_factor

                # Classify risk
                if score > 0.85:
                    risk = 'Severe'
                elif score > 0.75:
                    risk = 'High'
                elif score > 0.5:
                    risk = 'Moderate'
                else:
                    risk = 'Low'

                # Append data from this station to the list
                stations_and_risk.append((station.name, score, risk))
            except TypeError:
                pass

    return sorted_by_key(stations_and_risk, 1, reverse=True)
