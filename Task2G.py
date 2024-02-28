from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list,update_water_levels
import datetime
import numpy

stations = build_station_list()
for station in stations:
    d, l = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=1))

    #gradient of function in the end
    name_list_1 = []
    name_list_5 = []
    level_1 = numpy.array(l)[-1]
    level_2 = numpy.array(l)[-2]
    sign = level_1 - level_2
    if sign >= 0:
        name_list_1.append(station.name)
    else:
        name_list_5.append(station.name)

        #average for past 2 days
    sum = 0
    for i in l:
        sum += i
        average = sum/len(l)
        name_list_2 = []
        name_list_3 = []
        name_list_4 = []
    if average > station.typical_range[1]:
        name_list_2.append(station.name)
    if average > station.typical_range[0] and average < station.typical_range[1]:
        name_list_3.append(station.name)
    else:
        name_list_4.append(station.name)


    print('Severe list:')
    for i in name_list_1 and name_list_2:
        print(i)
    print('High list:')
    for i in name_list_1 and name_list_3:
        print(i)
    print('Moderate list:')
    for i in name_list_1 and name_list_4:
        print(i)
    print('low list:')
    for i in name_list_5 and name_list_4:
        print(i)