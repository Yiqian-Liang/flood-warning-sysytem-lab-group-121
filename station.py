# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):
        """Create a monitoring station."""

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
    def typical_range_consistent(self):
        if self.typical_range is None:
            return False
        elif isinstance(self.typical_range, tuple):
            if float(self.typical_range[0]) > float(self.typical_range[-1]):
                return False
        return True
    
    def relative_water_level(self):
        if self.typical_range_consistent==True:
            difference=float(self.typical_range[-1])-float(self.typical_range[0])
            level_above_lowest=float(self.latest_level)-float(self.typical_range[0])
            Fraction=level_above_lowest/difference
            return Fraction
        else:
            return None



        
def inconsistent_typical_range_stations(stations):
    list=[]
    for station in stations:
        if not station.typical_range_consistent():
            list.append(station.name)
    sorted_list=sorted(list)

    return sorted_list

def stations_level_over_threshold(stations, tol):
    list=[]
    for station in stations:
        if station.relative_water_level()!=None:
            if station.relative_water_level()>float(tol):
                list.append((station.name,station.relative_water_level()))
                list=sorted(list, key=lambda x: x[-1])
    return list
