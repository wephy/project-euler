# Prime power triples

from sympy import sieve
from bisect import bisect_left

limit = 50_000_000
primes = list(sieve.primerange(1, limit**0.5))
powers = [[p**i for p in primes[:bisect_left(primes, limit**(1 / i))]]
          for i in range(2, 5)]

found = set()
for a in powers[0]:
    for b in powers[1][:bisect_left(powers[1], limit - a)]:
        remainder = limit - a - b
        for c in powers[2][:bisect_left(powers[2], remainder)]:
            found.add(remainder - c)

print(len(found))
