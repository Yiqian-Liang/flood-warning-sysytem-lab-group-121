from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list,update_water_levels
import datetime
import matplotlib.dates as mdates
Stations=build_station_list()
update_water_levels(Stations)
# print("Running 2F")
list=[]
for Station in Stations:
    if Station.relative_water_level()!=None and Station.latest_level!=None:
        list.append(Station)#(Station.measure_id,Station.relative_water_level()))
list=sorted(list, key=lambda x: x.relative_water_level(),reverse=True)
top_five=list[:5]
Measure_ids=[]

# for i in range(len(top_five)):
#     Measure_ids.append(top_five[i][0])
# print("About to run for loop")    
for station in top_five:
    dt=2
    dates,levels=fetch_measure_levels(station.measure_id,dt=datetime.timedelta(days=dt))
    # d = mdates.date2num(dates)
    # print(d)
    # print(levels)
    plot_water_level_with_fit(station, dates, levels, 4)

    
    
    