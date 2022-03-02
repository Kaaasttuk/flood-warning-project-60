from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from Task2G import towns_with_station, assess_risk

stations = build_station_list()

def test_stations_level_over_threshold():

    s_id = "random station id"
    m_id = "random measure id"
    label = "Cambridge Station"
    coord = (1.0, 1.0)
    trange = (-2.0, 3.0)
    river = "Cambridge River"
    town = "Cambridge Town"
    

    Cambridge_Station = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    Cambridge_Station.latest_level = 0.1
    station = [Cambridge_Station]
    list = stations_level_over_threshold (station, 0)
    assert len(list) == 1

def test_stations_highest_rel_level():
    s_id = "random station id"
    m_id = "random measure id"
    label = "Cambridge Station"
    coord = (1.0, 1.0)
    trange = (-2.0, 3.0)
    river = "Cambridge River"
    town = "Cambridge Town"
    

    Cambridge_Station = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    Cambridge_Station.latest_level = 0.1
    station = [Cambridge_Station]
    st_list = stations_highest_rel_level(station, 1)
    assert type(st_list) == list
    assert len(st_list) == 1
    

