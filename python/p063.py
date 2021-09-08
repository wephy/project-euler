# Powerful digit counts

from math import log10


def solve():
    return sum(
        len(str(a**b)) == b for a in range(1, 10)
        for b in range(1, int(1 / log10(10 / 9)) + 1))


if __name__ == "__main__":
    print(solve())
