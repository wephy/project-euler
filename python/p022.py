# Names scores

import os
import numpy as np
from string import ascii_uppercase

data = np.char.strip(np.loadtxt(os.path.join("..", "data", "p022.txt"),
                                delimiter=",", dtype=str), '"')

answer = 0
for index, name in enumerate(sorted(data)):
    value = 0
    for char in name:
        value += ascii_uppercase.index(char) + 1
    answer += (index + 1) * value

print(answer)
