import numpy as np

def quartic(x):
    return x, x ** 4

dest = 1.0
step = 0.1
arr = np.arange(0, dest, step)

for i in arr:
    print(quartic(i))