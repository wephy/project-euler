# Cuboid route

import numpy as np
from numba import njit


@njit
def solve(limit):
    squares = [i**2 for i in range(1, 6*int(limit**0.5)+1)]
    squares_set = set(squares)
    solutions, m = 0, 0
    while solutions < limit:
        for path in squares[m:(2.5)*m]:
            left = path - squares[m]
            if left in squares_set:
                target = squares.index(left) + 1
                solutions += max(min(target-1, m+1) - np.ceil(target/2) + 1, 0)
        m += 1
    return (m, solutions)


print(solve(1000000))
