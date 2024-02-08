# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.utils import sorted_by_key  # noqa
#Task1B
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from haversine import haversine, Unit
Stations = build_station_list()
def stations_by_distance(stations, p):
    list=[]
    for station in stations:
        distance=haversine(station.coord, p)
        touple=(station.name,station.town,distance)
        list.append(touple)
    sorted_list=sorted(list, key=lambda x: x[-1])
    return sorted_list

#Task1C
from floodsystem.stationdata import build_station_list
from haversine import haversine, Unit
Stations = build_station_list()
def stations_within_radius(stations, centre, r):
    list=[]
    for station in stations:
        distance=haversine(station.coord, centre)
        if distance<r:
            list.append(station.name)
    list=sorted(list, key=lambda x:x[0])

    return list

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

#Task1E
def rivers_by_station_number(stations, N):
    N-=1
    dic_river = {key: len(value) for key, value in stations_by_river(stations).items()}
    my_list = [(k, v) for k, v in dic_river.items()]
    sorted_list = sorted(my_list, key=lambda t:t[1])
    sorted_list.reverse()
    selected_list_initial = sorted_list[:(N)]

    for i in range(N, len(sorted_list)):
        if sorted_list[i][1] == sorted_list[N][1]:
            selected_list_initial.append(sorted_list[i])
        else:
            break
    return selected_list_initial

#Task 1F
Stations = build_station_list()
from floodsystem.station import inconsistent_typical_range_stations
print(inconsistent_typical_range_stations(Stations))


    



