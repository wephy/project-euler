# Counting fractions in a range

import numpy as np
from numba import vectorize


@vectorize
def count(denominator):
    numerators = np.arange(denominator // 3 + 1, denominator // 2 + 1)
    return np.count_nonzero(np.gcd(numerators, denominator) == 1)


print(sum(count(np.arange(4, 12_000 + 1))))
