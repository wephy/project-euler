# Highly divisible triangular number

from itertools import count
from sympy import divisors

TARGET = 500


def solve():
    for n in count():
        if len(divisors(n * (n + 1) // 2)) > TARGET:
            return n * (n + 1) // 2


if __name__ == "__main__":
    print(solve())
