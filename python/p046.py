# Goldbach's other conjecture

from sympy import isprime
from itertools import count


def solve():
    primes = set([2])
    for i in count(3, 2):
        if isprime(i):
            primes.add(i)
        else:
            if not any(map(lambda x: ((i - x) / 2)**0.5 % 1 == 0, primes)):
                return i


if __name__ == "__main__":
    print(solve())
