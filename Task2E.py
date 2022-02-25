import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)
    
    plot_stations = []
    for station in stations:
        if station.latest_level == None:
            pass
        else:
            plot_stations.append([station, station.latest_level])
    
    plot_stations = sorted(plot_stations, key = lambda x:x[1])
    print(plot_stations)

    station_to_plot = []

    for list in plot_stations[-5:]:
        station_to_plot.append(list[0])

    dt = 10

    for station in station_to_plot:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))

        plot_water_levels(station, dates, levels)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IC Flood Warning System ***")
    run()


