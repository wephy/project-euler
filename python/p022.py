# Names scores

import os
from string import ascii_uppercase

with open(os.path.join("..", "data", "p022.txt"), encoding="utf-8") as f:
    names = eval("[" + f.readline() + "]")

answer = 0
for index, name in enumerate(sorted(names)):
    value = 0
    for char in name:
        value += ascii_uppercase.index(char) + 1
    answer += (index + 1) * value

print(answer)
