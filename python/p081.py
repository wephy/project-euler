# Path sum: two ways

import os
import numpy as np

size = 80

matrix = np.loadtxt(os.path.join("..", "data", "p081.txt"),
    usecols=range(size), delimiter=",", dtype=int)

for i in range((size * 2) - 3, -1, -1):
    for y in range(0, size):
        for x in range(0, size):
            if x + y == i:
                current = matrix[x, y]
                if x == size - 1:
                    matrix[x, y] = current + matrix[x, y+1]
                elif y == size - 1:
                    matrix[x, y] = current + matrix[x+1, y]
                else:
                    matrix[x, y] = current + min([matrix[x, y+1], matrix[x+1, y]])

print(matrix[0, 0])
