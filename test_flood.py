from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation

stations = build_station_list()

def test_stations_level_over_threshold():

    s_id = "random station id"
    m_id = "random measure id"
    label = "Cambridge Station"
    coord = (1.0, 1.0)
    trange = (-2.0, 3.0)
    river = "Cambridge River"
    town = "Cambridge Town"
    latest_level = 0.1

    Cambridge_Station = MonitoringStation(s_id, m_id, label, coord, trange, river, town, latest_level)
    station = [Cambridge_Station]
    list = stations_level_over_threshold (station, 0)
    assert len(list) == 1

def test_stations_highest_rel_level():
    a = stations_highest_rel_level(stations,0)
    assert type(a) == list
    assert len(a) == 0