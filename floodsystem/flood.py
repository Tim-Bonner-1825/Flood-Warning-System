from .station import MonitoringStation
from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    stat_level = []
    for stat in stations:
        if stat.relative_water_level() != None:
            if stat.relative_water_level() > tol:
                stat_level.append((stat, stat.relative_water_level()))
    stat_level.sort(key=lambda x: x[1], reverse=True)
    return stat_level


def stations_highest_rel_level(stations, N):
    '''takes arguments MonitoringStation objects, number of objects and outputs a list of the N highest stations sorted descending by relative water level
    args:
        stations = list of MonitoringStation objects, N = highest N stations you would like returned
    return:
        list of MonitoringStation objects, sorted descending for water level up until the Nth in the list
    '''
    relative_level_list = [(each, each.relative_water_level()) for each in stations if not each.relative_water_level() == None]
    return [each[0] for each in sorted_by_key(relative_level_list, 1, reverse=True)[:N]]
