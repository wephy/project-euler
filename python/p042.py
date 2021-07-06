# Coded triangle numbers

import os
import numpy as np
from string import ascii_uppercase

data = np.char.strip(np.loadtxt(os.path.join("..", "data", "p042.txt"),
                                delimiter=",", dtype=str), '"')

answer = 0
for word in data:
    word_sum = sum(ascii_uppercase.index(char) + 1 for char in word)
    if (8 * word_sum + 1) ** 0.5 % 1 == 0:
        answer += 1

print(answer)
