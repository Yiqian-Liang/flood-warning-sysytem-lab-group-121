from floodsystem.utils import sorted_by_key  # noqa
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
Stations = build_station_list()
def stations_level_over_threshold(stations, tol):
    list=[]
    for station in stations:
        if station.relative_water_level()!=None:
            if station.relative_water_level()>float(tol):
                list.append((station.name,station.relative_water_level()))
                list=sorted(list, key=lambda x: x[-1])
    return list