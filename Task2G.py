
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
import datetime
import numpy as np

"""Task 2G: issuing flood warnings for towns"""
'''Logic used for this code:
 - checks the data for recent days and tries to assign it an equation (to have a gradient function)
 - checks the gradient of the graph in recent days
 - assigns a risk level based on the rate of change of water level
 - gives weighted significance to dy/dx, time of change, current relative height
 '''

def risk_evaluation(station, gradientsig, timesig, heightsig):

    dt=2
    p=4
    risk_level = 0
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))

    try:
        data_good = True
        poly, d0 = polyfit(dates, levels, p)
        gradient = np.gradient(poly)
        risk_level += gradient[-1]*gradientsig
        if gradient[:1] > 0:
            gradientlist = list(np.gradient(gradient))
            gradientlist.reverse()
            try:
                start_time = gradientlist.index(0)
                risk_level += (len(gradientlist)-start_time)*timesig
            except:
                pass
        risk_level += station.relative_water_level() * heightsig    
    except:
       data_good = False
    return risk_level, data_good

def risk_level_assignment(stationlist):  # will be given a list of tuples, [station, risk_level]
    for station in stationlist:
        print(station[1])
        risk_level = "no data"
        if station[1] > 100:
            pass
            #Likely to be intentionally high value, given to stations not of concern or with broken data
        if station[1] < 100:
            risk_level = "Severe risk of flooding"
        if station[1] < 1.5:
            risk_level = "High risk of flooding"
        if station[1] < 1:
            risk_level = "Moderate risk of flooding"
        if station[1] < 0.5:
            risk_level = "Low risk of flooding"
        print(station[0], risk_level)
    return("risk assignment complete")


def run():
    stations = build_station_list()
    stations = stations[:20]
    update_water_levels(stations)
    atRisk = []

    for station in stations:
        risk_level, data_good = risk_evaluation(station, gradientsig=4, timesig=0.1, heightsig=7)  # relative height is most important, then rate of change, then the time it has been rising for
        relevant_data = (station.name, risk_level)
        if data_good == True:
            atRisk.append(relevant_data)
        else:
            atRisk.append((station.name, 150))
    atRisk.sort(key = lambda x: x[1], reverse=True)
    risk_level_assignment(atRisk)



if __name__ == '__main__':
    print("***Task 2G: CUED Part 1A Flood Warning System***")
    run()