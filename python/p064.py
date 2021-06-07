# Odd period square roots

import numpy as np
from numba import vectorize


@vectorize
def period(S):
    if np.sqrt(S) % 1 == 0:
        return 0

    a0 = np.floor(np.sqrt(S))
    an = a0
    mn = 0
    dn = 1

    x = 0
    while an != 2 * a0:
        mn = (dn * an) - mn
        dn = (S - (mn ** 2)) / dn
        an = np.floor((a0 + mn) / dn)
        x += 1

    return x


numbers = np.arange(1, 10_000 + 1)
periods = period(numbers)
print(len(periods[periods % 2 == 1]))
