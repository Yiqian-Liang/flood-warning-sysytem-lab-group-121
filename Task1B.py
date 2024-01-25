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

distance_from_Cam=stations_by_distance(Stations, (52.2053, 0.1218))
print(distance_from_Cam[:10])
print(distance_from_Cam[-10:])


