# Counting fractions in a range

import numpy as np
from numba import vectorize

LIMIT = 12_000


def solve():
    @vectorize
    def count(denominator):
        numerators = np.arange((denominator // 3) + 1, (denominator // 2) + 1)
        return np.count_nonzero(np.gcd(numerators, denominator) == 1)

    return sum(count(np.arange(4, LIMIT + 1)))


if __name__ == "__main__":
    print(solve())
