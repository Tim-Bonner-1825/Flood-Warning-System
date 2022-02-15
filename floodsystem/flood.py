from .station import MonitoringStation


def stations_level_over_threshold(stations, tol):
    stat_level = []
    for stat in stations:
        if stat.relative_water_level() != None:
            if stat.relative_water_level() > tol:
                stat_level.append((stat, stat.relative_water_level()))
    stat_level.sort(key=lambda x: x[1], reverse=True)
    return stat_level
