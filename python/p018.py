# Maximum path sum I

import os
import numpy as np


def solve():
    with open(os.path.join("..", "data", "p018.txt"), encoding="utf-8") as f:
        data = [list(map(int, row.split())) for row in f]

    answer = data[-1]
    for row in data[-2::-1]:
        answer = np.add([*map(max, zip(answer, answer[1:]))], row)
    return answer[0]


if __name__ == "__main__":
    print(solve())
