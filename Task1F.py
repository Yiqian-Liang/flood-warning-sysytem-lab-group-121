from floodsystem.stationdata import build_station_list
Stations = build_station_list()
from floodsystem.station import inconsistent_typical_range_stations
print(inconsistent_typical_range_stations(Stations))