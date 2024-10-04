def put_line(n):
    if n > 0:
        print('*', end='')
        put_line(n - 1)
    else:
        print()


def put_triangle(n):
    if n > 0:
        put_triangle(n - 1)
        put_line(n)


if __name__ == '__main__':
    print("put_triangle(5)")
    put_triangle(5)

    print("put_triangle(7)")
    put_triangle(7)
