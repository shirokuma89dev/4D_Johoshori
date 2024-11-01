def push(n):
    stack.append(n)

def pop():
    try:
        return 0, stack.pop()
    except IndexError:
        return -1, None

if __name__ == "__main__":
    stack = []
    while (c := input("i;push o;pop; e;end ?")) != "e":
        if c == "i":
            data = input("data?")
            ret = push(data)
        elif c == "o":
            ret, n = pop()
            if ret == -1:
                print("スタックが空です")
            else:
                print("pop -->  {:s}".format(n))
        elif c == "e":
            break
