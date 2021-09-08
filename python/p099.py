# Largest exponential

import os
import numpy as np


def solve():
    matrix = np.loadtxt(os.path.join("..", "data", "p099.txt"),
                        delimiter=",",
                        dtype=np.uint64)

    return np.argmax(matrix[:, 1] * np.log10(matrix[:, 0])) + 1


if __name__ == "__main__":
    print(solve())
