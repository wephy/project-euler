# Totient permutation

import numpy as np
from sympy import sieve
from itertools import combinations
from math import log

LIMIT = 10**7


def solve():
    window = 100 * log(LIMIT)  # From brief testing, this naive formula holds
    primes = sieve.primerange(LIMIT**0.5 - window, LIMIT**0.5 + window)

    return np.prod(
        min([(a, b) for a, b in combinations(primes, 2) if a * b < LIMIT
             and sorted(str(a * b)) == sorted(str((a - 1) * (b - 1)))],
            key=lambda x: np.prod(x) / np.prod(np.array(x) - 1)))


if __name__ == "__main__":
    print(solve())
