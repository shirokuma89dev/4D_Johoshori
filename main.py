import numpy as np

origin = 0.5
dest = 2.0
step = 0.5

for rad in np.arange(origin, dest + step, step):
    print(rad, "[rad]:", np.sin(rad))
