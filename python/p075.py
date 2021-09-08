# Singular integer right triangles

import numpy as np

LIMIT = 1_500_000


def solve():
    lengths = {}
    for m in range(1, 866):
        for n in range((m % 2) + 1, m, 2):
            if np.gcd(m, n) == 1:
                x = 2 * m * (m + n)
                for i in range(1, (LIMIT // x) + 1):
                    length = x * i
                    if length not in lengths:
                        lengths[length] = True
                    elif lengths[length]:
                        lengths[length] = False

    return sum(lengths.values())


if __name__ == "__main__":
    print(solve())
