import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.analysis import polyfit


#a function that displays a plot (using Matplotlib) of the water level data against time for a station, and include on the plot lines for the typical low and high levels. 
# The axes should be labelled and use the station name as the plot title.

def plot_water_levels(station, dates, levels):

    high_low = station.typical_range
    typical_range = list(high_low)

    # Plot
    plt.plot(dates, levels, label= "water levels")

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)
    plt.axhline(y = typical_range[0], color = 'b', linestyle = ':', label = "typical low")
    plt.axhline(y = typical_range[1], color = "r", linestyle = ":", label = "typical high")

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    
    plt.legend()

    plt.show()


def plot_water_level_with_fit(station, dates, levels, p):
    plot_water_levels(station, dates, levels)
    polyfit(dates, levels, p)

