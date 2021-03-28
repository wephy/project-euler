# Pentagon numbers

def pentagon(n):
    return ((3 * (n ** 2) - n) // 2)


def pentagon_check(n):
    return ((24 * n + 1) ** 0.5 + 1) % 6 == 0


def find_d(j=0):
    x = pentagon(j)
    for k in range(j-1, 0, -1):
        y = pentagon(k)
        if pentagon_check(x - y):
            if pentagon_check(x + y):
                print(x - y)
                return
    find_d(j+1)


find_d()
