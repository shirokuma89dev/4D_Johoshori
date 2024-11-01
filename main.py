############ SORTING ALGORITHMS ############
def normal_quick(a):
    length = len(a)
    stack = [(0, length - 1)]
    while len(stack) > 0:
        left, right = stack.pop()
        if left >= right:
            continue
        i = left
        j = right
        s = a[left + (right - left) // 2]
        while i < j:
            while a[i] < s:
                i += 1
            while a[j] > s:
                j -= 1
            if i < j:
                if a[i] == a[j]:
                    j -= 1
                else:
                    a[i], a[j] = a[j], a[i]
        stack.append((j + 1, right))
        stack.append((left, i - 1))


def recursive_quick(arr, left, right):
    if left < right:
        pivot = arr[left]
        low = left
        high = right + 1

        while True:
            low += 1
            while low <= right and arr[low] < pivot:
                low += 1
            high -= 1
            while arr[high] > pivot:
                high -= 1
            if low >= high:
                break

            # Swap elements at low and high
            arr[low], arr[high] = arr[high], arr[low]

        # Place pivot in the correct position
        arr[left], arr[high] = arr[high], arr[left]

        # Recursively sort the left and right subarrays
        recursive_quick(arr, left, high - 1)
        recursive_quick(arr, high + 1, right)

############ MAIN ############

import random
import time

reqursive_time = []
normal_time = []

for trial in range(10):
    print(trial + 1, "回目")

    rand = []  # 空のリストを作成

    for i in range(1000000):  # 乱数の個数を指定
        rand.append(random.randint(1, 10000000))

    recursive_start = time.time()
    recursive_quick(rand, 0, len(rand) - 1)
    recursive_end = time.time()
    reqursive_time.append(recursive_end - recursive_start)
    print("再帰関数:", rand[:4], "時間:", reqursive_time[trial])

    normal_start = time.time()
    normal_quick(rand)
    normal_end = time.time()
    normal_time.append(normal_end - normal_start)
    print("通常関数:", rand[:4], "時間:", normal_time[trial])
    print("")

print("### result ###")
print("再帰関数（平均）:", sum(reqursive_time) / len(reqursive_time))
print("通常関数（平均）:", sum(normal_time) / len(normal_time))