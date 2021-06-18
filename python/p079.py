# Passcode derivation

import os
from itertools import chain

with open(os.path.join("..", "data", "p079.txt"), encoding="utf-8") as f:
    data = f.read().splitlines()

d = {i: set() for i in set(chain.from_iterable(data))}

for attempt in data:
    d[attempt[0]].update([attempt[1], attempt[2]])
    d[attempt[1]].update([attempt[2]])

print("".join(sorted(d.keys(), key=lambda x: len(d[x]), reverse=True)))
