# Square digit chains

import numpy as np
from collections import Counter
from itertools import combinations_with_replacement

cache = {0: False, 1: False, 89: True}


def termination(n):
    if n in cache.keys():
        return cache[n]
    return termination(sum(int(d)**2 for d in str(n)))


for i in range(568):
    cache[i] = termination(i)

F = [1, 1, 2, 6, 24, 120, 720, 5_040, 40_320, 362_880]
answer = 0
for combo in combinations_with_replacement([*range(10)], 7):
    if cache[sum(d**2 for d in combo)]:
        answer += F[7] // np.prod([F[v] for v in Counter(combo).values()])

print(answer)
