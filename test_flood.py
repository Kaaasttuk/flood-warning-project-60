from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation

stations = build_station_list()

def test_stations_level_over_threshold():
    a = stations_level_over_threshold(stations,1000)
    assert type(a) == list
    assert len(a) == 0

def test_stations_highest_rel_level():
    a = stations_highest_rel_level(stations,10)
    assert type(a) == list
    assert len(a) == 11