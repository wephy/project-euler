# Square root convergents

import fractions


def sqrt2(n):
    denom = 2
    for _ in range(n - 1):
        denom = 2 + fractions.Fraction(1, denom)
    return 1 + fractions.Fraction(1, denom)


answer = 0
for n in range(1_001):
    fraction = sqrt2(n)
    numerator = fraction.numerator
    denominator = fraction.denominator
    if len(str(numerator)) > len(str(denominator)):
        answer += 1

print(answer)
