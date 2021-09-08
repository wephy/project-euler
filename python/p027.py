# Quadratic primes

from math import prod
from sympy import sieve, isprime
from itertools import count

LIMIT = 1000


def solve():
    primes = set(sieve.primerange(LIMIT))
    tests = set()
    for b in primes.copy():
        for a in range(-b, LIMIT, 2):
            tests.add((a, b))

    composites = set()
    return prod(
        max(tests, key=lambda x: consecutive_primes(*x, primes, composites)))


def consecutive_primes(a, b, primes, composites):
    for i in count():
        x = (i * i) + (i * a) + b
        if x in composites or x not in primes and not isprime(x):
            composites.add(x)
            return i
        else:
            primes.add(x)


if __name__ == "__main__":
    print(solve())
