from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

# Build Station List
stations = build_station_list()

# Take names of stations within 10km
stats_within_10 = stations_within_radius(stations, (52.2053, 0.1218), 10)
names = []
for s in stats_within_10:
    names.append(s.name)

# print result
print(sorted(names))
