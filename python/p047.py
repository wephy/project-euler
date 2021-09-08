# Distinct primes factors

from sympy import primefactors
from itertools import count


def solve():
    distincts = {}
    for i in count(3):
        distincts[i] = len(primefactors(i))
        if set(map(distincts.get, range(i - 3, i + 1))) == {4}:
            return i - 4


if __name__ == "__main__":
    print(solve())
