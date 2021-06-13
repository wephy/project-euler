# Counting fractions

from sympy import sieve

print(sum(sieve.totientrange(2, 1_000_001)))