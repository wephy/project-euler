# Digit factorial chains

from itertools import combinations_with_replacement
from sympy.utilities.iterables import multiset_permutations
from math import factorial


def solve():
    factorials = [factorial(i) for i in range(10)]
    digits = [*range(10)]

    def chain(n, combination=True):
        count = 0
        found = set()
        if not combination:
            n = sum(factorials[int(i)] for i in n)
            count += 1
        while n not in found:
            found.add(n)
            n = sum(factorials[int(i)] for i in str(n))
            count += 1
        return count

    answer = 0
    for i in range(1, 7):
        for combo in combinations_with_replacement(digits, i):
            if chain(combo, False) == 60:
                for perm in multiset_permutations(combo):
                    if perm[0] == 0:
                        continue
                    if chain(int("".join(map(str, perm)))) == 60:
                        answer += 1

    return answer


if __name__ == "__main__":
    print(solve())
