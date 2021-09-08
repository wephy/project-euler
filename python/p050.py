# Consecutive prime sum

import numpy as np
from sympy import sieve
from itertools import count

LIMIT = 1_000_000


def solve():
    primes_list = list(sieve.primerange(2, LIMIT))
    primes_set = set(primes_list)
    max_length = np.where(np.cumsum(primes_list) > LIMIT)[0][0]
    for window in count(max_length, -1):
        for i in range(len(primes_list) - window):
            p = sum(primes_list[i:i + window])
            if p >= LIMIT:
                break
            elif p in primes_set:
                return p


if __name__ == "__main__":
    print(solve())
