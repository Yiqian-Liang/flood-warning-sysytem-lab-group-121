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

print(stations_within_radius(Stations,(52.2053, 0.1218),10))