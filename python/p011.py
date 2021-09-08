# Largest product in a grid

import os
import numpy as np

ADJACENTS = 4


def solve():
    matrix = np.loadtxt(os.path.join("..", "data", "p011.txt"),
                        delimiter=" ",
                        dtype=np.uint8)

    return max(
        product(matrix, y, x, dy, dx) for (y, x) in np.ndindex(20, 20)
        for dy, dx in [(1, 1), (1, -1)])


def product(matrix, y, x, dy, dx):
    if dy > 0:
        y0, y1 = 0, matrix.shape[0] - ADJACENTS
    else:
        y0, y1 = ADJACENTS, matrix.shape[0]

    if dx > 0:
        x0, x1 = 0, matrix.shape[1] - ADJACENTS
    else:
        x0, x1 = ADJACENTS, matrix.shape[1]

    if y0 <= y <= y1 and x0 <= x <= x1:
        product = 1
        for i in range(ADJACENTS):
            product *= matrix[y + (i * dy), x + (i * dx)]
        return product
    return 0


if __name__ == "__main__":
    print(solve())
