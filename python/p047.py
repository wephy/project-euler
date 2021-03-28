# Distinct primes factors

from sympy import primefactors

n, i = 0, 0
while i < 4:
    if len(primefactors(n)) == 4:
        i += 1
    else:
        i = 0
    n += 1
print(n-3)
