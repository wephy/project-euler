# Consecutive prime sum

from sympy import sieve

primes = list(sieve.primerange(2, 1_000_000))
primes_set = set(primes)
counter = prime_sum = 0
while prime_sum < 1_000_000:
    prime_sum += primes[counter]
    counter += 1


def solution(window=counter):
    while True:
        for i in range(len(primes) - window):
            p = sum(primes[i:i+window])
            if p >= 1_000_000:
                break
            if p in primes_set:
                return p
        window -= 1


print(solution())
