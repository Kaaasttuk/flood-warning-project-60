from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

#1B


def run():
    stations=build_station_list()
    p=(52.2053, 0.1218)

    original_list=stations_by_distance(stations, p)
    closest_list=original_list[0,9]
    print("The closest 10 stations:{}".format(closest_list))

    reverse_list=original_list.reverse()
    furthest_list=reverse_list[0,9]
    print("The furthest 10 stations:{}".format(furthest_list))


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()