from .utils import sorted_by_key
from floodsystem.station import MonitoringStation


def stations_level_over_threshold(stations, tol):
    stations_level_over_threshold=[]
    for station in stations:
        if station.relative_water_level() = None
            pass
        else:
            if station.relative_water_level() > tol:
                stations_level_over_threshold.insert(0, (station.name, station.relative_water_level()))
            else:
                pass
        stations_level_over_threshold=sorted_by_key(stations_level_over_threshold, 1)
        stations_level_over_threshold.reverse()
    return stations_level_over_threshold
