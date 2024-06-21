import random
import numpy as np
import time

arr_num = 100000
ref_arr = []

for i in range(20):
    ref_arr.append([random.randint(i, arr_num) for i in range(arr_num)])

def shell_sort(N, array):
    gap = int(len(array) / N)

    while gap > 0:
        for group in range(gap):
            for i in range(group + gap, len(array), gap):
                for j in range(i - gap, group - 1, -gap):
                    if array[j] > array[j + gap]:
                        array[j], array[j + gap] = array[j + gap], array[j]
                    else:
                        break

        gap = int(gap / N)
    
    # 最後に一回以上、gapが1の挿入ソートを行わないとソートを保証できない
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break

    # print("Sorted array: ", array)

def measure_sort_time(N, num_trials = 20):
    print('N =', N)
    times = []
    for i in range(num_trials):
        arr = ref_arr[i].copy()

        start_time = time.time()
        print("Start time: ", start_time)
        
        shell_sort(N, arr)
        
        end_time = time.time()
        times.append(end_time - start_time)
    print(arr)

    return np.mean(times)

n_values = np.linspace(2, 5, int((5 - 2) / 0.3 + 1))
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

