from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.station import MonitoringStation

# List of Stations
stations = build_station_list()
incon = inconsistent_typical_range_stations(stations)

# Get names of inconsistent stations
incon_Names = []
for stat in incon:
    incon_Names.append(stat.name)

# Sort and print
incon_Names.sort()
print(incon_Names)
