# Lexicographic permutations

from math import factorial


def permuation(p, l):
    permutation_digits = []
    while l:
        d, p = divmod(p, factorial(len(l) - 1))
        permutation_digits.append(l[d])
        l.pop(d)
    return "".join(map(str, permutation_digits))


print(permuation(999_999, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
