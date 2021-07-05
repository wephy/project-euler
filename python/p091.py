# Right triangles with integer coordinates

import numpy as np

count = 0
for (x, y) in list(np.ndindex(50+1, 50+1))[1:]:
    slope = [x, y] / np.gcd(x, y)
    coord = [y, -x] + slope
    while coord[0] <= 50 and coord[1] <= 0:
        coord += slope
        count += 1

print((count * 2) + 50**2)
