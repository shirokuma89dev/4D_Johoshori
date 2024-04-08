def calculate_even_sum(n):
    sum = 0
    for i in range(2, n + 1, 2):
        sum += i
    print(sum)

calculate_even_sum(10)