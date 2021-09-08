# Prime power triples

from sympy import sieve
from bisect import bisect_left

LIMIT = 50_000_000


def solve():
    primes = list(sieve.primerange(1, LIMIT**0.5))
    powers = [[p**i for p in primes[:bisect_left(primes, LIMIT**(1 / i))]]
              for i in range(2, 5)]

    found = set()
    for a in powers[0]:
        for b in powers[1][:bisect_left(powers[1], LIMIT - a)]:
            remainder = LIMIT - a - b
            for c in powers[2][:bisect_left(powers[2], remainder)]:
                found.add(remainder - c)

    return len(found)


if __name__ == "__main__":
    print(solve())
