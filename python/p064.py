# Odd period square roots

import numpy as np
from numba import vectorize

LIMIT = 10_000


def solve():
    @vectorize
    def period(s):
        if np.sqrt(s) % 1 == 0:
            return 0
        a0 = np.floor(np.sqrt(s))
        a = a0
        m = 0
        d = 1

        x = 0
        while a != 2 * a0:
            m = (d * a) - m
            d = (s - (m**2)) / d
            a = np.floor((a0 + m) / d)
            x += 1
        return x

    return np.count_nonzero(period(np.arange(1, LIMIT + 1)) % 2 == 1)


if __name__ == "__main__":
    print(solve())
