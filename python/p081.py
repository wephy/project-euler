# Path sum: two ways

import os
import numpy as np

size = 80

matrix = np.loadtxt(os.path.join("..", "data", "p081.txt"),
                    usecols=range(size), delimiter=",", dtype=int)

for (y, x), v in np.ndenumerate(matrix.copy()):
    if x > 0 and y > 0:
        matrix[y, x] = v + min(matrix[y-1, x], matrix[y, x-1])
    elif y == 0 and x > 0:
        matrix[y, x] = v + matrix[y, x-1]
    elif x == 0 and y > 0:
        matrix[y, x] = v + matrix[y-1, x]

print(matrix[size-1, size-1])
