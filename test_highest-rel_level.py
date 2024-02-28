from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from haversine import haversine, Unit
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.flood import stations_level_over_threshold
from Task2E import plot_water_levels
import matplotlib.pyplot as plt

def test_stations_highest_rel_level():
    station1 = MonitoringStation(1,1,"Station 1", (0,0),(2,6), "River 1", "A" ) 
    station2 = MonitoringStation(2,2,"Station 2", (3,45),(5,43), "River 2", "B" ) 
    station3 = MonitoringStation(3,3,"Station 3", (6,43),(54,3), "River 2", "C" ) 
    station4 = MonitoringStation(4,4,"Station 4", (9,3),(37,2), "River 2", "D" )
    station5 = MonitoringStation(5,5,"Station 5", (4,3), (6,5), "River 1", "E")

    station1.latest_level = 2.1
    station2.latest_level = 12
    station3.latest_level = 6
    station4.latest_level = 8
    station5.latest_level = 100

    list_of_stations = [station1,station2,station3,station4,station5]
    assert test_stations_highest_rel_level(list_of_stations, 3) == [(station5, station2, station1)]

def test_plot_water_levels():
    station1 = MonitoringStation(1,1,"Station 1", (0,0),(2,6), "River 1", "A" ) 
    station2 = MonitoringStation(2,2,"Station 2", (3,45),(5,43), "River 2", "B" ) 
    station3 = MonitoringStation(3,3,"Station 3", (6,43),(54,3), "River 2", "C" ) 
    station4 = MonitoringStation(4,4,"Station 4", (9,3),(37,2), "River 2", "D" )
    station5 = MonitoringStation(5,5,"Station 5", (4,3), (6,5), "River 1", "E")

    list_of_stations = [station1,station2,station3,station4,station5]
    plot_water_levels(list_of_stations)

    assert plt.gca().has_title()
    assert plt.gca().has_xlabel()
    assert plt.gca().has_ylabel()