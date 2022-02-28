from .utils import sorted_by_key
from floodsystem.station import MonitoringStation


def stations_level_over_threshold(stations, tol):
    stations_level_over_threshold=[]
    for station in stations:
        if station.relative_water_level() == None:
            pass
        else:
            if station.relative_water_level() > tol:
                stations_level_over_threshold.append((station, station.relative_water_level()))
            else:
                pass
    stations_level_over_threshold=sorted_by_key(stations_level_over_threshold, 1)
    stations_level_over_threshold.reverse()

    return stations_level_over_threshold


def stations_highest_rel_level(stations, N):
    stations_highest_rel_level=[]
    for station in stations:
        if station.relative_water_level() == None:
            pass
        else:
            stations_highest_rel_level.insert(0, (station, station.relative_water_level()))
    stations_highest_rel_level=sorted_by_key(stations_highest_rel_level, 1)
    stations_highest_rel_level.reverse()
    new_list=stations_highest_rel_level[0:N]
    list_stations = []
    for tuple in new_list:
        list_stations.append(tuple[0])


    return list_stations