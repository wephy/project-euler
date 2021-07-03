# Smallest multiple

import numpy as np
from math import log, floor

primes = [2, 3, 5, 7, 11, 13, 17, 19]

print(np.product([n ** floor(log(20, n)) for n in primes]))
