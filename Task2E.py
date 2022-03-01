import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():   
    stations = build_station_list()
    update_water_levels(stations)
    station_to_plot = stations_highest_rel_level(stations, 5)

    dt = 10

    for station in station_to_plot:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_levels(station, dates, levels)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IC Flood Warning System ***")
    print("stations with over 100 relative level are excluded as outliers.")
    run()


