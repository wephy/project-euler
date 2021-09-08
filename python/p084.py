# Monopoly odds

import numpy as np
from numba import njit
from collections import Counter

SIDES = 4


def solve():
    iterations = 1_000_000
    distribution = np.array([i + j + 2 for i, j in np.ndindex(SIDES, SIDES)])
    positions = np.zeros(iterations, dtype=np.uint8)

    rng = np.random.default_rng()
    rints = rng.integers(0, 16, iterations, dtype=np.uint8)

    kernel(positions, distribution, rints, iterations)

    return "".join(
        str(x[0]).zfill(2) for x in Counter(positions).most_common(3))


@njit
def kernel(positions, distribution, rints, iterations):
    for i in range(iterations):
        positions[i] = throw(positions[i - 1], i, distribution, rints)


@njit
def throw(current_square, iteration, distribution, rints):
    n = rints[iteration]
    new = (current_square + distribution[n]) % 40

    if new == 30:
        return 10
    if new in [2, 17, 33]:
        if n == 0:
            return 0
        elif n == 1:
            return 10
    elif new in [7, 22, 36]:
        if n == 0:
            return 0
        elif n == 1:
            return 10
        elif n == 2:
            return 11
        elif n == 3:
            return 24
        elif n == 4:
            return 39
        elif n == 5:
            return 5
        elif n == 6 or n == 7:
            return ((new + 5) // 10 * 10 + 5) % 40
        elif n == 8:
            if new == 7:
                return 12
            elif new == 22:
                return 28
            elif new == 36:
                return 36
        elif n == 9:
            return (new - 3) % 40
    return new


if __name__ == "__main__":
    print(solve())
