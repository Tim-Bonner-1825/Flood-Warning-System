import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from .datafetcher import fetch_measure_levels


def plot_water_levels(station, dates, levels):
    # Plot
    plt.plot(dates, levels)
    plt.plot([station.typical_range[1] for x in levels], levels)
    plt.plot([station.typical_range[0] for x in levels], levels)
    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title("{}".format(station.name))

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()
