from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold

def run():
    stations=build_station_list()
    tol=0.8

    stations_over=stations_level_over_threshold(stations, tol)
    for station in stations_over:
        print ("%d %d" % (station[0], station[1]))
