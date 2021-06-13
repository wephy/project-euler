# Totient permutation

import numpy as np
from sympy import sieve
from itertools import combinations

N = 10 ** 7

primes = sieve.primerange(N ** 0.5 - 1000, N ** 0.5 + 1000)

nums = [(a, b) for a, b in combinations(primes, 2) if a * b < N
        and sorted(str(a * b)) == sorted(str((a - 1) * (b - 1)))]

print(np.prod(min(nums, key=lambda x: np.prod(x) / np.prod(np.array(x) - 1))))
