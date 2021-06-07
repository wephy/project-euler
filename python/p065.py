# Convergents of e

from fractions import Fraction

denominators = []
for i in range(1, 34):
    denominators += [1, 2*i, 1]

answer = 0
for d in denominators[::-1]:
    answer = Fraction(1, d + answer)
answer += 2

print(sum(map(int, [*str(answer.numerator)])))
