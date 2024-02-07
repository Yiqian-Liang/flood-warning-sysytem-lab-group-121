from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from haversine import haversine, Unit
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

test_stations=[]
for i in range (10):#0-9
    s = MonitoringStation(
                    station_id='http://environment.data.gov.uk/flood-monitoring/id/stations/52119',
                    measure_id='@id',
                    label=f'Station{i}',
                    coord=(float(i-5), float(0)),
                    typical_range=(i+1,-i+5),
                    river='river',
                    town=f'town{i}')
    test_stations.append(s)
    
def test_1B():
    assert stations_by_distance(test_stations, (0,0))==[5,4,3,2,1,0,2,3,4]
    
def test_1C():
    assert stations_within_radius(test_stations,(0,0),2)==['Station4','Station5']

s = MonitoringStation(
                station_id='http://environment.data.gov.uk/flood-monitoring/id/stations/52119',
                measure_id='@id',
                label=f'Station10',
                coord=(float(0), float(0)),
                typical_range=None,
                river='river',
                town=f'town10')
test_stations.append(s)   

def test_1F():
    assert inconsistent_typical_range_stations(test_stations)==['Station4','Station5','Station6','Station7','Station8','Station9','Station10']

def test_rivers_with_station():
    test_stations=[]
    for i in range (5):
        s = MonitoringStation(
                    station_id='http://environment.data.gov.uk/flood-monitoring/id/stations/52119',
                    measure_id='@id',
                    label=f'Station{i}',
                    coord=(float(i-5), float(0)),
                    typical_range=(i+1,-i+5),
                    river=f'river{i}',
                    town=f'town{i}')
    test_stations.append(s)

    assert rivers_with_station(test_stations) == set("River 0", "River 1", "River 2", "River 3" "River 4")


def test_stations_by_river():
    station1 = MonitoringStation(1,1,"Station 1", (0,0),(2,6), "River 1", "A" ) 
    station2 = MonitoringStation(2,2,"Station 2", (3,45),(5,43), "River 2", "B" ) 
    station3 = MonitoringStation(3,3,"Station 3", (6,43),(54,3), "River 3", "C" ) 
    station4 = MonitoringStation(4,4,"Station 4", (9,3),(37,2), "River 2", "D" )
    station5 = MonitoringStation(5,5,"Station 5", (4,3), (6,5), "River 1", "E")

    list_of_stations = [station1,station2,station3,station4,station5]
    result = stations_by_river(list_of_stations) 
    stations_sorted = {"River 1":[station1, station5], "River 2": [station2, station4], "River 3": [station3]}

    for river,stations in result.items():
        assert river in stations_sorted
        assert set(stations) == set(stations_sorted[river])

def test_rivers_by_station_number():
    station1 = MonitoringStation(1,1,"Station 1", (0,0),(2,6), "River 1", "A" ) 
    station2 = MonitoringStation(2,2,"Station 2", (3,45),(5,43), "River 2", "B" ) 
    station3 = MonitoringStation(3,3,"Station 3", (6,43),(54,3), "River 2", "C" ) 
    station4 = MonitoringStation(4,4,"Station 4", (9,3),(37,2), "River 2", "D" )
    station5 = MonitoringStation(5,5,"Station 5", (4,3), (6,5), "River 1", "E")

    list_of_stations = [station1,station2,station3,station4,station5]
    assert test_rivers_by_station_number(list_of_stations,2) == [("River 2",3),("River 1",2)]