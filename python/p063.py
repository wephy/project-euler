# Powerful digit counts

import numpy as np

answer = 0
for a in range(1, 10):
    for b in range(1, int(1 / (1 - np.log10(9))) + 1):
        if len(str(a ** b)) == b:
            answer += 1

print(answer)
