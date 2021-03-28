# Lexicographic permutations

from math import factorial


def permuation(p, objects):
    permutation_digits = []
    while objects:
        d, p = divmod(p, factorial(len(objects) - 1))
        permutation_digits.append(objects[d])
        objects.pop(d)
    return "".join(map(str, permutation_digits))


PERMUATION_NUM = 999_999  # From 0
OBJECTS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(permuation(PERMUATION_NUM, OBJECTS))
