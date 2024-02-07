from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number

# def rivers_with_station(stations):
#     list_of_monitored_rivers=[]
#     for station in stations:
#         list_of_monitored_rivers.append(station.river)
#     set_of_monitored_rivers=set(list_of_monitored_rivers)
#     return set_of_monitored_rivers

# def stations_by_river(stations):
#     dic = dict()
#     for river in rivers_with_station(stations):
#         dic[river] = []
    
#     for station in stations:
#         dic[station.river].append(station)
#     return dic

# def rivers_by_station_number(stations, N+1):
#     dic_river = {key: len(value) for key, value in stations_by_river(stations).items()}
#     my_list = [(k, v) for k, v in dic_river.items()]
#     sorted_list = sorted(my_list, key=lambda t:t[1])
#     sorted_list.reverse()
#     selected_list_initial = sorted_list[:N]

#     for i in range(N+1, len(sorted_list)):
#         if sorted_list[i][1] == sorted_list[N][1]:
#             selected_list_initial.append(sorted_list[i])
#         else:
#             break
#     return selected_list_initial

data = build_station_list()

print(rivers_by_station_number(data, 14))

