# Lexicographic permutations

from math import factorial

PERMUATION_NUM = 1_000_000
OBJECTS = [*range(10)]


def solve():
    p = PERMUATION_NUM - 1
    permutation = ""
    while OBJECTS:
        d, p = divmod(p, factorial(len(OBJECTS) - 1))
        permutation += str(OBJECTS.pop(d))
    return permutation


if __name__ == "__main__":
    print(solve())
