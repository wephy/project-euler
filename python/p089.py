# Roman numerals

import os
import numpy as np

matrix = np.loadtxt(os.path.join("..", "data", "p089.txt"), dtype=str)

numerals = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90,
            "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}


def reduce(number):
    result = numerals[number[-1]]
    for i in range(len(number) - 1):
        result += (numerals[number[i]] * (-1) ** (
                   numerals[number[i]] < numerals[number[i+1]]))

    minimal = ""
    while result > 0:
        for r, i in numerals.items():
            while result >= i:
                minimal += r
                result -= i
    return minimal


answer = 0
for roman_numeral in matrix:
    answer += len(roman_numeral) - len(reduce(roman_numeral))

print(answer)
