# Diophantine equation

import numpy as np
from fractions import Fraction


def minimal_solution(s):
    if np.sqrt(s) % 1 == 0:
        return 0

    a0 = int(np.floor(np.sqrt(s)))
    a = a0
    m = 0
    d = 1

    answer = Fraction(0, 1)
    denominators = []
    while answer.numerator ** 2 - s * answer.denominator ** 2 != 1:
        m = (d * a) - m
        d = (s - (m ** 2)) / d
        a = int(np.floor((a0 + m) / d))
        denominators += [a]

        answer = 0
        for den in denominators[::-1]:
            answer = Fraction(1, den + answer)
        answer += a0

    return answer.numerator


solutions = {}
for i in range(2, 1000 + 1):
    solutions[i] = minimal_solution(i)

print(max(solutions, key=solutions.get))
