# Amicable chains

import numpy as np
from numba import njit

LIMIT = 1_000_000


def solve():
    sieve = np.array(np.zeros(LIMIT), dtype=np.uint32)

    @njit
    def kernel(sieve):
        for i in range(1, LIMIT):
            for j in range(2 * i, LIMIT, i):
                sieve[j] += i

    @njit
    def solution(sieve):
        longest, answer = 0, 0
        for n in range(1, LIMIT + 1):
            chain = [n]
            while chain[-1] <= LIMIT:
                s = sieve[chain[-1]]
                if s in chain:
                    if s == chain[0] and len(chain) > longest:
                        longest, answer = len(chain), n
                    break
                chain.append(s)
        return answer

    kernel(sieve)

    return solution(sieve)


if __name__ == "__main__":
    print(solve())
