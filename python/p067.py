# Maximum path sum II

import os
import numpy as np

with open(os.path.join("..", "data", "p067.txt"), encoding="utf-8") as f:
    data = [list(map(int, row.split())) for row in f.read().splitlines()]

answer = data[-1]
for row in data[-2::-1]:
    answer = np.add([*map(max, zip(answer, answer[1:]))], row)

print(answer[0])
