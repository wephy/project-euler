# Large sum

import os

with open(os.path.join("..", "data", "p013.txt"), encoding="utf-8") as f:
    numbers = f.read().split('\n')

answer = 0
for number in numbers:
    answer += int(number)
answer = str(answer)

print(answer[:10])
