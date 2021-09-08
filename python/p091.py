# Right triangles with integer coordinates

import numpy as np

LIMIT = 50


def solve():
    count = 0
    for (x, y) in list(np.ndindex(LIMIT + 1, LIMIT + 1))[1:]:
        slope = (x, y) / np.gcd(x, y)
        coord = (y, -x) + slope
        while coord[0] <= LIMIT and coord[1] <= 0:
            coord += slope
            count += 1

    return (count * 2) + LIMIT**2


if __name__ == "__main__":
    print(solve())
