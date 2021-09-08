# Passcode derivation

import os
import numpy as np
from itertools import chain


def solve():
    data = np.loadtxt(os.path.join("..", "data", "p079.txt"), dtype=str)

    d = {i: set() for i in set(chain.from_iterable(data))}
    for attempt in data:
        d[attempt[0]].update([attempt[1], attempt[2]])
        d[attempt[1]].update([attempt[2]])

    return "".join(sorted(d.keys(), key=lambda x: len(d[x]), reverse=True))


if __name__ == "__main__":
    print(solve())
