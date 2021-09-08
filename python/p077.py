# Prime summations

from sympy import sieve
from bisect import bisect
from itertools import count
from math import log

TARGET = 5000


def solve():
    primes = list(sieve.primerange(100 * log(TARGET)))[::-1]

    def num_ways(n):
        ways = [1] + ([0] * n)
        for p in primes[bisect(primes, n):]:
            for i in range(p, n + 1):
                ways[i] += ways[i - p]
        return int(ways[-1])

    for n in count():
        if num_ways(n) >= TARGET:
            return n


if __name__ == "__main__":
    print(solve())
