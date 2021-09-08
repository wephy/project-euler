# Coded triangle numbers

import os
import numpy as np
from string import ascii_uppercase


def solve():
    data = np.char.strip(
        np.loadtxt(os.path.join("..", "data", "p042.txt"),
                   delimiter=",",
                   dtype=str), '"')

    @np.vectorize
    def word_sum(word):
        return sum(ascii_uppercase.index(char) + 1 for char in word)

    return np.count_nonzero((8 * word_sum(data) + 1)**0.5 % 1 == 0)


if __name__ == "__main__":
    print(solve())
