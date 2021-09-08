# Combinatoric selections

from sympy import binomial

LIMIT = 100


def solve():
    return sum(
        int(binomial(n, r)) > 1_000_000 for n in range(1, LIMIT + 1)
        for r in range(1, n))


if __name__ == "__main__":
    print(solve())
