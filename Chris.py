from .utils import sorted_by_key  # noqa
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from haversine import haversine, Unit

#1B

def stations_by_distance(stations, p):
    stations_by_distance=[]
    for station in stations:
        distance=haversine(station.coordinate, p)
        stations_by_distance.append((station, station.town, distance))
    return stations_by_distance

stations_by_distance=sorted_by_key(stations_by_distance, 2)

#1C

def stations_within_radius(stations, centre, r):
    stations_within_radius=[]
    for station in stations:
        distance=haversine(station.coordinate, centre)
            if distance>=r:
                pass
            else:
                stations_within_radius.append(station)
    return stations_within_radius