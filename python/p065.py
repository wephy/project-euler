# Convergents of e

from fractions import Fraction

CONVERGENT = 100


def solve():
    denominators = []
    for i in range(1, CONVERGENT // 3 + 1):
        denominators += [1, 2 * i, 1]

    answer = 0
    for d in denominators[::-1]:
        answer = Fraction(1, d + answer)
    return sum(map(int, str((answer + 2).numerator)))


if __name__ == "__main__":
    print(solve())
