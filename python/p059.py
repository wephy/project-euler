# XOR decryption

import os
from collections import Counter

with open(os.path.join("..", "data", "p059.txt"), encoding="utf-8") as f:
    text = f.readline().split(",")

answer = 0
for i in range(3):
    key = Counter([int(char) ^ 32 for char in text[i::3]]).most_common()[0][0]
    answer += sum([int(char) ^ key for char in text[i::3]])

print(answer)
