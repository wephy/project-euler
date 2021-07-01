# Square digit chains

import numpy as np
from collections import Counter
from itertools import combinations_with_replacement

known = {0: False, 1: False, 89: True}


def termination(n):
    if n in known.keys():
        return known[n]
    known[n] = termination(sum(int(d)**2 for d in str(n)))
    return known[n]


for i in range(568):
    termination(i)

F = [1, 1, 2, 6, 24, 120, 720, 5_040, 40_320, 362_880]
answer = 0
for combo in combinations_with_replacement([i for i in range(10)], 7):
    if known[sum(d**2 for d in combo)]:
        answer += F[7] // np.product([F[v] for v in Counter(combo).values()])

print(answer)
