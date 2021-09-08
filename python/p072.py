# Counting fractions

from sympy import sieve

LIMIT = 1_000_000


def solve():
    return sum(sieve.totientrange(2, 1_000_000 + 1))


if __name__ == "__main__":
    print(solve())
