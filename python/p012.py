# Highly divisible triangular number

from sympy import divisors

n = 1
while True:
    if len(divisors(n * (n + 1) // 2)) > 500:
        break
    n += 1

print(n * (n + 1) // 2)
