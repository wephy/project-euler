# Goldbach's other conjecture

from time import time
from sympy import isprime

start = time()

squares = set()
primes = set([2])


def find_c(i=1):
    if (i ** 0.5) % 1 == 0:
        squares.add(i)
    if i > 10_000:
        return
    find_c(i+1)


find_c()
print(squares)


print(time() - start)
