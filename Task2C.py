from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level

def run():
    stations=build_station_list()
    N=10

    N_stations=stations_highest_rel_level(stations, N)
    for station in N_stations:
        print ("%d %d" % (station[0], station[1]))