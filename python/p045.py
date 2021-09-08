# Triangular, pentagonal, and hexagonal

from itertools import count


def solve():
    for i in count(144):
        hexagon = (i * (2 * i - 1))
        if ((24 * hexagon + 1)**0.5 + 1) % 6 == 0:
            return hexagon


if __name__ == "__main__":
    print(solve())
