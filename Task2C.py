from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level

def run():
    stations=build_station_list()
    N=10

    N_stations=stations_highest_rel_level(stations, N)
    for station in N_stations:
        print ("{} : {}".format(station[0], station[1]))

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IC Flood Warning System ***")
    run()