import numpy as np
import random

# input the number of elements
n = input("Enter the number of elements: ")

if (not n.isdigit()):
    print("Invalid input")
    exit()

n = int(n)

# generate random array
arr = [random.randint(0, n - 1) for i in range(n)]

# sort the array
for i in range(n - 1):
    min_val = arr[i]
    min_index = i   
    for j in range(i + 1, n):
        if arr[j] < min_val:
            min_val = arr[j]
            min_index = j

    arr[min_index], arr[i] = arr[i], arr[min_index]

# ascending or descending
order = input("Enter 'asc' for ascending or 'desc' for descending: ")

if not (order == "asc" or order == "desc"):
    print("Invalid input")
    exit()

# reverse the array if descending:
if order == "desc":
    arr = arr[::-1]

print("Sorted array: ", arr)
print("✅😀 Done! Happy Coding!")
