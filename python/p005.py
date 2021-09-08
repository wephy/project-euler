# Smallest multiple

from sympy import sieve
from math import log, floor, prod

LIMIT = 20


def solve():
    return prod(n**floor(log(LIMIT, n)) for n in sieve.primerange(LIMIT))


if __name__ == '__main__':
    print(solve())
