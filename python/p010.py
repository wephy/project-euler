# Summation of primes

from numba import njit

LIMIT = 2_000_000


@njit
def solve():
    answer = 0
    composites = set()
    for i in range(2, LIMIT):
        if i not in composites:
            answer += i
            for p in range(i * 2, LIMIT, i):
                composites.add(p)
    return answer


if __name__ == "__main__":
    print(solve())
