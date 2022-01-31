from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius


def run():
    stations=build_station_list()
    original_list=stations_within_radius(stations, (52.2053, 0.1218), 10)
    sorted_list=original_list.sort()
    print("The stations within 10 km:{}".format(sorted_list))


if __name__ == "__main__":
    print("*** Task 1: CUED Part IC Flood Warning System ***")
    run()
