from floodsystem.geo import rivers_with_station, stations_by_river, rivers_by_station_number, stations_within_radius, stations_within_radius
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation

stations = build_station_list()

def test_rivers_with_station():
    a = rivers_with_station(stations)
    assert type(a) == list
    assert len(a) > 0


def test_stations_by_river():
    a = stations_by_river(stations)
    assert type(a) == dict

def test_rivers_by_station_number():
    # maybe this has a problem?
    a = rivers_by_station_number(stations, 10)
    assert type(a) == list









