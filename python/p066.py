# Diophantine equation


import numpy as np
from fractions import Fraction
import time


def minimal_solution(n):
    print("\n\n", n)

    if np.sqrt(n) % 1 == 0:
        return 0

    a = np.ceil(np.sqrt(n))
    b = 1
    k = a ** 2 - n * b ** 2
    print(a, b, k)

    m0 = np.sqrt(n)
    while k != 1:
        ms = []
        for i in range(0, int(m0 + 2)):
            if (a + b * i) / k % 1 == 0:
                ms += [i]
        print(ms)
        m = min(ms, key=lambda x: abs(n - x ** 2))
        print("m: ", m)
        a, b, k = (m * a + n * b) // abs(k), (a + b * m) // abs(k), (m ** 2 - n) // k
        # bp = (a + b * m) / abs(k)
        # kp = (m ** 2 - n) / k

        print(a, b, k)
        # time.sleep(1)

    return int(a)

minimal_solution(181)
# print(2 ** 52)

# solutions = {}
# for i in range(2, 1000 + 1):
#     solutions[i] = minimal_solution(i)

# print(max(solutions, key=solutions.get))
# 183567298683461940
# 1534755952314119
# 4503599627370496