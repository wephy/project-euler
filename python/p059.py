# XOR decryption

import os
import numpy as np
from collections import Counter


def solve():
    data = np.loadtxt(os.path.join("..", "data", "p059.txt"),
                      delimiter=",",
                      dtype=np.uint8)

    return sum(
        int(char) ^ Counter(int(char) ^ 32
                            for char in data[i::3]).most_common()[0][0]
        for i in range(3) for char in data[i::3])


if __name__ == "__main__":
    print(solve())
