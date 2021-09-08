# Square root convergents

from math import log10


def solve():
    def frac_gen():
        n = 3
        d = 2
        for _ in range(1000):
            yield n, d
            n, d = (2 * d) + n, n + d

    return sum(int(log10(x)) > int(log10(y)) for x, y in frac_gen())


if __name__ == "__main__":
    print(solve())
