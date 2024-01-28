from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation

#Task1D
from floodsystem.stationdata import build_station_list

data = build_station_list()

def rivers_with_station(stations):
    list_of_monitored_rivers=[]
    for station in stations:
        list_of_monitored_rivers.append(station.river)
    set_of_monitored_rivers=set(list_of_monitored_rivers)
    return set_of_monitored_rivers

def stations_by_river(stations):
    dic = dict()
    for river in rivers_with_station(stations):
        dic[river] = []
    
    for station in stations:
        dic[station.river].append(station)
    return dic



list1 = rivers_with_station(data)
number = len(list1)
list1=list(list1)
list1.sort()
selected_list = list1[0:10]
print(f"{number} stations. first 10 - {selected_list}")

# dict1 = stations_by_river(data)
# AireStation = []
# CamStation = []
# ThamesStation = []
# for station in dict1["River Aire"]:
#     AireStation.append(station.name)
# AireStation.sort()

# for station in dict1["River Cam"]:
#     CamStation.append(station.name)
# CamStation.sort()

# for station in dict1["River Thames"]:
#     ThamesStation.append(station.name)
# ThamesStation.sort()

# print(f"River Aire : {AireStation}")
# print(f"River Cam : {CamStation}")
# print(f"River Thames : {ThamesStation}")
