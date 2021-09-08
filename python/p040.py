# Champernowne's constant

from math import prod, log10


def solve():
    digits = "".join(
        str(x) for x in range(int(1_000_000 / (log10(1_000_000) - 1))))
    return prod(int(digits[i]) for i in [10**x for x in range(7)])


if __name__ == "__main__":
    print(solve())
