from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold

def run():
    stations=build_station_list()
    tol=0.8

    stations_over=stations_level_over_threshold(stations, tol)
    for station in stations_over:
        print ("{}: {}".format(station[0], station[1]))

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IC Flood Warning System ***")
    run()