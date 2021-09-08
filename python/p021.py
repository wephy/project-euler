# Amicable numbers

import numpy as np
from numba import njit

LIMIT = 10_000


def solve():
    sieve = np.array(np.zeros(LIMIT), dtype=np.uint32)
    kernel(sieve)

    return sum(i for i in range(LIMIT)
               if ((d := sieve[i]) < LIMIT and d != i and sieve[d] == i))


@njit
def kernel(sieve):
    for i in range(1, LIMIT):
        for j in range(2 * i, LIMIT, i):
            sieve[j] += i


if __name__ == "__main__":
    print(solve())
