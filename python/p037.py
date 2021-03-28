# Truncatable primes

from sympy import isprime

truncatable_primes = set()
i = 11
while len(truncatable_primes) < 11:
    if isprime(i):
        left, right = str(i)[1:], str(i)[:-1]
        failed = False
        while left:
            if not isprime(int(left)) or not isprime(int(right)):
                failed = True
                break
            left, right = left[1:], right[:-1]
        if not failed:
            truncatable_primes.add(i)
    i += 2

print(sum(truncatable_primes))
