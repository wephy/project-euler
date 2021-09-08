# Path sum: three ways

import os
import numpy as np


def solve():
    matrix = np.loadtxt(
        os.path.join("..", "data", "p082.txt"), delimiter=",", dtype=np.uint32
    )

    size = matrix.shape[0]
    for x in range(1, size):
        column = matrix[:, x] + matrix[:, (x - 1)]
        for y1, y2 in zip(range(1, size), reversed(range(0, size - 1))):
            column[y1] = min(column[y1], matrix[y1, x] + column[y1 - 1])
            column[y2] = min(column[y2], matrix[y2, x] + column[y2 + 1])
        matrix[:, x] = column

    return min(matrix[:, -1])


if __name__ == "__main__":
    print(solve())
