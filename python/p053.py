# Combinatoric selections

from math import factorial


def nCr(n, r):
    numerator = factorial(n)
    denominator = factorial(r) * factorial(n - r)
    return numerator / denominator


answer = 0
for n in range(101):
    for r in range(n):
        if nCr(n, r) > 1_000_000:
            answer += 1

print(answer)
