import random
import numpy as np
import time

arr_num = 50000
ref_arr = [random.randint(i, arr_num) for i in range(arr_num)]

def shell_sort(gap, array):
    while gap > 0:
        for k in range(gap):
            for i in range(k + gap, len(array), gap):
                for j in range(i - gap, k - 1, -gap):
                    if array[j] > array[j + gap]:
                        array[j], array[j + gap] = array[j + gap], array[j]
                    else:
                        break

        gap //= 2

def measure_sort_time(N, num_trials = 20):
    print('N =', N)
    times = []
    for i in range(num_trials):
        arr = ref_arr.copy()

        start_time = time.time()
        print("Start time: ", start_time)
        
        shell_sort(int(len(arr) / N), arr)
        
        end_time = time.time()
        times.append(end_time - start_time)

    return np.mean(times)

n_values = np.arange(2, 5.1, 0.3)
sort_times = [measure_sort_time(n) for n in n_values]

## print the results as a table
print('N\tTime')
for n, time in zip(n_values, sort_times):
    print('{}\t{}'.format(n, time))

## plot the results
import matplotlib.pyplot as plt
plt.plot(n_values, sort_times)
plt.xlabel('N')
plt.ylabel('Time (s)')
plt.title('Shell Sort Time')
plt.show()

