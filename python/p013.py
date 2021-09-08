# Large sum

import os
import numpy as np


def solve():
    data = np.loadtxt(os.path.join("..", "data", "p013.txt"), dtype=object)

    return str(sum(int(n) for n in data))[:10]


if __name__ == "__main__":
    print(solve())
