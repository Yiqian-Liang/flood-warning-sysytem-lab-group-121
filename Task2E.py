import matplotlib.pyplot as plt
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
import datetime
from floodsystem.flood import calculate_relative_level, stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
import numpy

def plot_water_levels(station, dates, levels):

    plt.plot(dates, levels)

    plt.axhline(y = station.typical_range[0])
    plt.axhline(y = station.typical_range[1])

    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    # Display plot
    plt.tight_layout()

    plt.show()


stations = build_station_list()
update_water_levels(stations)
print(stations_highest_rel_level(stations, 5))
 

names = list([x[0] for x in stations_highest_rel_level(stations, 5)])

for station in stations:
    if station.name in names:
        print(station)
        d, l = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=10))
        dates = numpy.array(d)
        levels = numpy.array(l)
        plot_water_levels(station, dates, levels)