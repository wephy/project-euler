# Spiral primes

from sympy import isprime
from itertools import count


def solve():
    primes = 0
    x = 1
    for i in count(1):
        for _ in range(4):
            x += (2 * i)
            if isprime(x):
                primes += 1
        if primes / ((4 * i) + 1) < 0.1:
            return (2 * i) + 1


if __name__ == "__main__":
    print(solve())
