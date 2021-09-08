# Lattice paths

from math import factorial

SIZE = 20


def solve():
    return factorial(2 * SIZE) // (factorial(SIZE)**2)


if __name__ == "__main__":
    print(solve())
