from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.station import MonitoringStation

Stations = MonitoringStation()

list1 = rivers_with_station(Stations)
number = len(list1)
selected_list = list1[0,10]
selected_list.sort()
print(selected_list)

dict1 = stations_by_river(Stations)
print(dict1['River Aire'], dict1['River Cam'], dict1['River Thames'])
