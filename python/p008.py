# Largest product in a series

import os
import numpy as np
from itertools import chain


def solve():
    data = np.array(
        [
            *chain.from_iterable(
                np.loadtxt(os.path.join("..", "data", "p008.txt"), dtype=str))
        ],
        dtype=np.uint8,
    )

    return max(
        np.prod(data[i:(i + 13)], dtype=np.uint64) for i in range(1000 - 13))


if __name__ == "__main__":
    print(solve())
