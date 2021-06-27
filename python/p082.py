# Path sum: three ways

import os
import numpy as np

size = 80
matrix = np.loadtxt(os.path.join("..", "data", "p082.txt"),
                    usecols=range(size), delimiter=",", dtype=int)

for x in range(1, size):
    column = matrix[:, x] + matrix[:, x-1]
    for y in range(1, size):
        column[y] = min(column[y], column[y-1] + matrix[y, x])
    for y in range(size - 2, -1, -1):
        column[y] = min(column[y], matrix[y, x] + column[y+1])
    matrix[:, x] = column

print(min(matrix[:, -1]))
