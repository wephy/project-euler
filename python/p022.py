# Names scores

import os
import numpy as np
from string import ascii_uppercase


def solve():
    data = np.char.strip(
        np.loadtxt(os.path.join("..", "data", "p022.txt"),
                   delimiter=",",
                   dtype=str), '"')

    answer = 0
    for index, name in enumerate(sorted(data)):
        answer += (index + 1) * sum(
            (ascii_uppercase.index(char) + 1) for char in name)
    return answer


if __name__ == "__main__":
    print(solve())
