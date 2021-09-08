# Totient maximum

from sympy import nextprime

LIMIT = 1_000_000


def solve():
    def prime_gen():
        i = 1
        while True:
            yield (i := nextprime(i))

    x = 1
    for p in prime_gen():
        if (y := x * p) > LIMIT:
            return x
        x = y


if __name__ == "__main__":
    print(solve())
