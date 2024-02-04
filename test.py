from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from haversine import haversine, Unit
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.station import inconsistent_typical_range_stations
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