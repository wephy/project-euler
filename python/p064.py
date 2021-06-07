# Odd period square roots

import numpy as np
from numba import vectorize


@vectorize
def period(S):
    if np.sqrt(S) % 1 == 0:
        return 0

    a0 = np.floor(np.sqrt(S))
    a = a0
    m = 0
    d = 1

    x = 0
    while a != 2 * a0:
        m = (d * a) - m
        d = (S - (m ** 2)) / d
        a = np.floor((a0 + m) / d)
        x += 1

    return x


numbers = np.arange(1, 10_000 + 1)
periods = period(numbers)
print(len(periods[periods % 2 == 1]))
