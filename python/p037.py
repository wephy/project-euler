# Truncatable primes

from sympy import sieve
from itertools import count, combinations_with_replacement, permutations, chain


def solve():
    solutions = set()
    for i in count():
        primes = set(sieve.primerange(10**(i + 2)))
        for left, right in arrangements([2, 3, 5, 7], 2):
            for center in arrangements([1, 3, 7, 9], i):
                n = "".join(map(str, [left, *center, right]))
                if int(n) in primes:
                    if all(
                            int(x) in primes for i in range(len(n))
                            for x in [n[i:], n[:len(n) - i]]):
                        solutions.add(int(n))
                        if len(solutions) == 11:
                            return sum(solutions)


def arrangements(digits, size):
    return set(chain.from_iterable(
            map(permutations, combinations_with_replacement(digits, size))))


if __name__ == "__main__":
    print(solve())
