from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list
Stations=build_station_list()
R=stations_level_over_threshold(Stations, 0.8)
for i in range(len(R)):
    print(R[i][0],R[i][1])
