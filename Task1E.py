from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

# Create list of stations and print number of stations per river
stations = build_station_list()
print(rivers_by_station_number(stations, 9))
