def kaijo(n):
    if n == 0:
        return 1
    else:
        return n * kaijo(n-1)

if __name__ == '__main__':
    for n in range(12):
        print('{:2d}! = {:10d}'.format(n, kaijo(n)))
