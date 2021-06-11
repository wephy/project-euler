# Totient maximum

from sympy import nextprime

answer = x = 1
while answer * x < 1_000_000:
    answer *= x
    x = nextprime(x)

print(answer)
