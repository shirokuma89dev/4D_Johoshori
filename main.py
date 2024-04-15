import numpy as np
import matplotlib.pyplot as plt

RANGE = 5
STEP = 0.1

x = np.arange(-RANGE, RANGE + STEP, STEP)
y = [i**2 for i in x]

plt.plot(x, y)
plt.show()
