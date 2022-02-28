from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    stations=build_station_list()
    update_water_levels(stations)
    tol=0.8

    stations_over=stations_level_over_threshold(stations, tol)
    for station in stations_over:
        station_obj = station[0]
        print ("{}: {}".format(station_obj.name, station[1]))

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IC Flood Warning System ***")
    run()