# Diophantine equation

import numpy as np
from fractions import Fraction

LIMIT = 1000


def solve():
    def minimal_solution(D):
        if np.sqrt(D) % 1 == 0:
            return 0

        a0 = int(np.floor(np.sqrt(D)))
        a = a0
        m = 0
        d = 1

        n = Fraction(0, 1)
        denominators = []
        while n.numerator**2 - (D * n.denominator**2) != 1:
            m = (d * a) - m
            d = (D - (m**2)) / d
            a = int(np.floor((a0 + m) / d))
            denominators += [a]

            n = 0
            for den in denominators[::-1]:
                n = Fraction(1, den + n)
            n += a0
        return n.numerator

    return max(range(LIMIT + 1), key=minimal_solution)


if __name__ == "__main__":
    print(solve())
