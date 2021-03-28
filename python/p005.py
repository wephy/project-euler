# Smallest multiple

from sympy import isprime
from math import log, floor

TEST = 20
answer = 1
for i in range(1, TEST + 1):
    if isprime(i):
        answer *= i ** floor(log(TEST, i))

print(answer)
