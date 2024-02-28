from floodsystem.stationdata import build_station_list, update_water_levels

stations = build_station_list()
update_water_levels(stations)

def calculate_relative_level(stations):
    relative_level_list = []
    for station in stations:
        if station.typical_range and station.latest_level is not None:
            relative_level = (station.latest_level - station.typical_range[0]) / (station.typical_range[1] - station.typical_range[0])
            relative_level_list.append((station.name, relative_level))

    return relative_level_list


def stations_highest_rel_level(stations, N):
    sorted_list = sorted(calculate_relative_level(stations), key = lambda x:x[1], reverse = True)
    top_N_stations = sorted_list[:N]
    return top_N_stations

for a,b in stations_highest_rel_level(stations, 10):
    print(a,b)