# Pandigital prime

from sympy import isprime
from itertools import permutations


def solve():
    def parse(t):
        return int("".join(map(str, t)))

    pandigital_primes = (parse(perm) for i in range(1, 10)
                         if sum(range(i + 1)) % 3 != 0
                         for perm in permutations(range(1, (i + 1)))
                         if isprime(parse(perm)))
    return max(pandigital_primes)


if __name__ == "__main__":
    print(solve())
