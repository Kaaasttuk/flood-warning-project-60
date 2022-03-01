from cProfile import label
from tkinter.ttk import LabeledScale
import numpy as np
import matplotlib
import matplotlib.pyplot as plt





def polyfit(dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    y = levels


    p_coeff = np.polyfit(x-x[0], y, p)
    poly = np.poly1d(p_coeff)

    plt.plot(x, y, ".", label="data points")

    x1 = np.linspace(x[0], x[-1], 30)
    plt.plot(x1, poly(x1 - x[0]), label = "fit")
    plt.show

