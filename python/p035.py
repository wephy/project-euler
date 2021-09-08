# Circular primes

from sympy import sieve

LIMIT = 1_000_000


def solve():
    candidates = set(map(str, filter(
        lambda x: not any(int(digit) % 2 == 0 for digit in str(x)),
        sieve.primerange(LIMIT))
        ))

    return 1 + sum(
        all(n[i:] + n[:i] in candidates for i in range(len(n)))
        for n in candidates)


if __name__ == "__main__":
    print(solve())
