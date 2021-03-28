# 10001st prime

from sympy import isprime

primes = []

n = 2
while len(primes) <= 10_000:
    if isprime(n):
        primes.append(n)
    n += 1

print(primes[10_000])
