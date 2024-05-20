import numpy as np
import matplotlib.pyplot as plt


def taylor_sin(phase, n):
    result = phase
    term = phase
    EPS = 1.0e-8

    for i in range(0, n, 2):
        old_result = result
        term *= -phase * phase / (i + 2) / (i + 3)
        result += term

        if np.abs(old_result - result) < (EPS * np.abs(old_result)):
            return result

    if np.abs(result) < EPS:
        return result
    else:
        return np.nan

print('x'.center(10), 'Taylor sin(x)'.rjust(25), 'numpy sin(x)'.rjust(25))
print("-" * 62)

for x in range(0, 181, 10):
    x_rad = np.radians(x)
    taylor = taylor_sin(x_rad, 200)
    numpy_sin = np.sin(x_rad)

    print(str(x).center(10), str(taylor).rjust(25), str(numpy_sin).rjust(25))

## Result ##
#     x                  Taylor sin(x)              numpy sin(x)
# --------------------------------------------------------------
#     0                            0.0                       0.0
#     10           0.17364817766651633       0.17364817766693033
#     20           0.34202014332590347        0.3420201433256687
#     30            0.4999999999999643       0.49999999999999994
#     40            0.6427876096850399        0.6427876096865393
#     50            0.7660444430917407         0.766044443118978
#     60            0.8660254037859597        0.8660254037844386
#     70            0.9396926208012458        0.9396926207859083
#     80            0.9848077530113933         0.984807753012208
#     90            0.9999999999939768                       1.0
#    100            0.9848077529761511         0.984807753012208
#    110            0.9396926207878726        0.9396926207859084
#    120            0.8660254037946835        0.8660254037844387
#    130            0.7660444431657727         0.766044443118978
#    140            0.6427876096838189        0.6427876096865395
#    150            0.4999999999884349       0.49999999999999994
#    160            0.3420201432809031        0.3420201433256689
#    170           0.17364817766971424       0.17364817766693028
#    180         2.479060653624965e-16    1.2246467991473532e-16