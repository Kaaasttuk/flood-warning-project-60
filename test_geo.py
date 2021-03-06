from floodsystem.geo import rivers_with_station, stations_by_river, rivers_by_station_number, stations_within_radius, stations_within_radius
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from haversine import haversine, Unit

stations = build_station_list()

def test_rivers_with_station():
    a = rivers_with_station(stations)
    assert type(a) == list
    assert len(a) > 0


def test_stations_by_river():
    a = stations_by_river(stations)
    assert type(a) == dict

def test_rivers_by_station_number():
    a = rivers_by_station_number(stations, 10)
    assert type(a) == list

def test_stations_within_radius():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    station = [s]
    n = stations_within_radius(station, (-2.0, 4.0), 10)
    assert len(n) == 1







