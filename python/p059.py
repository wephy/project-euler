# XOR decryption

import os
import numpy as np
from collections import Counter

data = np.loadtxt(os.path.join("..", "data", "p059.txt"),
                  delimiter=",", dtype=np.uint8)

answer = 0
for i in range(3):
    key = Counter([int(char) ^ 32 for char in data[i::3]]).most_common()[0][0]
    answer += sum([int(char) ^ key for char in data[i::3]])

print(answer)
