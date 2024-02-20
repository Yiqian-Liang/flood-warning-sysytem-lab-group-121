from floodsystem.utils import sorted_by_key  # noqa
from floodsystem.stationdata import build_station_list,update_water_levels
from floodsystem.station import MonitoringStation

def stations_level_over_threshold(stations, tol):
    update_water_levels(stations)
    list=[]
    for station in stations:
        if station.relative_water_level()!=None and station.relative_water_level()>float(tol) and station.latest_level!=None:
            list.append((station.name,station.relative_water_level()))
            list=sorted(list, key=lambda x: x[-1],reverse=True)
    return list
