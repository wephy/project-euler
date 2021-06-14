# Digit factorial chains

from itertools import combinations_with_replacement
from sympy.utilities.iterables import multiset_permutations

FACTORIAL = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def chain(n, add_first=True):
    count = 0
    found = set()
    if not add_first:
        n = sum([FACTORIAL[int(i)] for i in str(n)])
        count += 1
    while n not in found:
        found.add(n)
        n = sum([FACTORIAL[int(i)] for i in str(n)])
        count += 1
    return count


answer = 0
for i in range(1, 7):
    for combo in combinations_with_replacement(digits, i):
        if chain("".join(map(str, combo)), False) == 60:
            for perm in multiset_permutations(combo):
                if perm[0] == 0:
                    continue
                if chain(int("".join(map(str, perm)))) == 60:
                    answer += 1

print(answer)
