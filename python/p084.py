# Monopoly odds

import numpy as np
from numba import njit
from collections import Counter


@njit
def new(square, n, dist, randoms):
    new = (square + dist[randoms[n]]) % 40
    if new == 30:
        return 10
    rand = randoms[n]
    if new in [2, 17, 33]:
        if rand == 0:
            return 0
        elif rand == 1:
            return 10
    elif new in [7, 22, 36]:
        if rand == 0:
            return 0
        elif rand == 1:
            return 10
        elif rand == 2:
            return 11
        elif rand == 3:
            return 24
        elif rand == 4:
            return 39
        elif rand == 5:
            return 5
        elif rand == 6 or rand == 7:
            return ((new + 5) // 10 * 10 + 5) % 40
        elif rand == 8:
            if new == 7:
                return 12
            elif new == 22:
                return 28
            elif new == 36:
                return 36
        elif rand == 9:
            return (new - 3) % 40
    return new


@njit
def kernel(positions, dist, randoms, iterations):
    for i in range(iterations):
        positions[i] = new(positions[i-1], i, dist, randoms)


iterations = 1_000_000
dist = np.array([i+j+2 for i, j in np.ndindex(4, 4)])
randoms = np.random.randint(0, 16, iterations, dtype=np.uint8)
positions = np.zeros(iterations, np.uint8)

kernel(positions, dist, randoms, iterations)

print("".join(str(x[0]).zfill(2) for x in Counter(positions).most_common(3)))
