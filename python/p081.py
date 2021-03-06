# Path sum: two ways

import os
import numpy as np
import heapq


def solve():
    matrix = np.loadtxt(
        os.path.join("..", "data", "p083.txt"), delimiter=",", dtype=np.uint32
    )

    vertices = set(np.ndindex((matrix.shape[0], matrix.shape[1])))
    h = [(matrix[0, 0], (0, 0))]
    visited = {}
    while h:
        current, (y, x) = heapq.heappop(h)
        for y, x in [(y, x + 1), (y + 1, x)]:
            if (y, x) not in visited and (y, x) in vertices:
                heapq.heappush(h, (current + matrix[y, x], (y, x)))
                visited[(y, x)] = current + matrix[y, x]

    return visited[(matrix.shape[0] - 1, matrix.shape[1] - 1)]


if __name__ == "__main__":
    print(solve())
