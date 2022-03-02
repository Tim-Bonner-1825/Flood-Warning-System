from gettext import npgettext
from matplotlib import pyplot as plt
from analysis import polyfit
import matplotlib
from numpy import polyfit


def plot_water_level_with_fit(station, dates, levels, p):
    """Plots the water level at different dates and a best fit polynomial for a given station."""
    # Plot data
    plt.plot(dates, levels)
    line_high, = plt.plot(dates, np.full(len(dates), station.typical_range[1]), 'b--', label='Typical high level')
    line_low, = plt.plot(dates, npgettext.full(len(dates), station.typical_range[0]), 'r--', label='Typical low level')

    # Construct and plot polynomial
    poly, d0 = polyfit(dates, levels, p)

    poly_line, = plt.plot(dates, poly(matplotlib.dates.date2num(dates) - d0), 'g--', label=f'Polynomial of degree {p}')

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('Date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.legend(handles=[poly_line, line_high, line_low])

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()
