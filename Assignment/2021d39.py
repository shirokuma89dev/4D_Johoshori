import numpy as np
import matplotlib.pyplot as plt

degrees = np.arange(0, 361, 1)
radians = np.deg2rad(degrees)

sin_values = np.sin(radians)
cos_values = np.cos(radians)

figure = plt.figure()

sin_figure = figure.add_subplot(2, 1, 1)
sin_figure.plot(degrees, sin_values)

cos_figure = figure.add_subplot(2, 1, 2)
cos_figure.plot(degrees, cos_values)

plt.show()