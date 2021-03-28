# Quadratic primes

from sympy import isprime


def quadratic_primes(a, b):
    n = 0
    while True:
        if not isprime(n ** 2 + a * n + b):
            return n
        else:
            n += 1


answer = {'n': 0, 'v': 0}
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        p = quadratic_primes(a, b)
        if p > answer['v']:
            answer['v'] = p
            answer['n'] = a * b

print(answer['n'])
