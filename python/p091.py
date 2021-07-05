# Right triangles with integer coordinates

import numpy as np

limit = 50

answer = 0
for coord in np.ndindex(limit+1, limit+1):
    perp = (coord / np.gcd(*coord))
    perp = [perp[1], -perp[0]]
    new = np.array([coord[0] + perp[0], coord[1] + perp[1]])
    while new[0] <= 50 and new[1] >= 0:
        answer += 1
        new[0] += perp[0]
        new[1] += perp[1]

answer = answer * 2 + limit**2

print(answer)