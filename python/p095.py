# Amicable chains

import numpy as np
from numba import njit

limit = 1_000_000
sieve = np.array(np.zeros(limit), dtype=np.uint32)


@njit
def kernel(sieve):
    for i in range(1, limit):
        for j in range(2*i, limit, i):
            sieve[j] += i


@njit
def solve(sieve):
    longest, answer = 0, 0
    for n in range(1, limit+1):
        chain = [n]
        while chain[-1] <= limit:
            s = sieve[chain[-1]]
            if s in chain:
                if s == chain[0] and len(chain) > longest:
                    longest, answer = len(chain), n
                break
            chain.append(s)
    return answer


kernel(sieve)
print(solve(sieve))
