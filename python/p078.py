# Coin partitions

from numba import njit

TARGET = 1_000_000


@njit
def solve():
    p = {0: 1, 1: 1}
    n = 1

    while True:
        n += 1
        p[n] = 0
        i = 0

        while True:
            i += 1
            m1 = n - i * ((3 * i) - 1) // 2
            m2 = n - i * ((3 * i) + 1) // 2
            if m1 < 0 and m2 < 0:
                break
            s = 1
            if i % 2 == 0:
                s = -1
            if m1 >= 0:
                p[n] += s * p[m1]
            if m2 >= 0:
                p[n] += s * p[m2]

        p[n] = p[n] % TARGET
        if p[n] == 0:
            return n


if __name__ == "__main__":
    print(solve())
