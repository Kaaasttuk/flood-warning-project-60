# list the towns where you assess the risk of flooding to be greatest.
from floodsystem.station import MonitoringStation
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
import datetime
import numpy as np

# make list of towns
def towns_with_station(stations):
    towns = []
    for station in stations:
        if station.town in towns:
            pass
        else:
            towns.append(station.town)
    
    stations_in_town = {}

    for town in towns:
        list = []
        for station in stations:
            if station.town == town:
                list.append(station)
            else:
                pass

        stations_in_town[town] = list

    return towns, stations_in_town

# assess risk based on (1) severe: a station with relative water level already above 2
# (2) high: one of the stations predicted 1 in 6 hours
# (3) moderate: all of the stations predicted 0.4 - 1 in 6 hours
# (4) low: every town below that

def assess_risk(towns, stations_in_town):
    severe = []
    high = []
    moderate = []
    low = []
    for town in towns:
        count = 0
        for station in stations_in_town[town]:
            if station.relative_water_level() == None:
                pass
            elif station.relative_water_level() > 2:
                count += 1
            else:
                pass
        if not town == None and count > 0 :
            severe.append(town)
            towns.remove(town)
        else:
            pass

    dt = 1
    for town in towns:

        for station in stations_in_town[town]:
            prediction_list =[]
            dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
            if len(levels) == 0:
                break
            else:

                past = -1 * round(len(levels)/4)
                present = levels[-1]
                one_ago = levels[past]
                if type(present) == list:
                    present = present[0]
                else:
                    pass
                if type(one_ago) == list:
                    one_ago = one_ago[0]
                else:
                    pass

                delta = present - one_ago
                if station.relative_water_level() == None:
                    pass
                else:
                    predicted_level = station.relative_water_level() + delta
                    prediction_list.append(predicted_level)

        prediction_list.sort(reverse=True)

        if len(prediction_list) == 0:
            pass
        elif prediction_list[0] > 1:
            high.append(town)
                
        elif prediction_list[0] > 0.4 and prediction_list[0] < 1:
            moderate.append(town)
        else:
            low.append(town)
    
    return severe, high, moderate, low
    

    

def run():
    stations = build_station_list()
    update_water_levels(stations)
    towns, stations_in_town = towns_with_station(stations)
    severe, high, moderate, low = assess_risk(towns, stations_in_town)

    print("The risk of flooding is greatest in following towns:{}".format(severe))
    print("The number of stations in each categories is, high:{}, moderate:{}, low:{}".format(len(high), len(moderate), len(low)))

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IC Flood Warning System ***")
    run()