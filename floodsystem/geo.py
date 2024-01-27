# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
#Task1B
from floodsystem.stationdata import build_station_list
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



