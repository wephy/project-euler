# Prime summations

from sympy import sieve

primes = list(sieve.primerange(1, 1_000_000))[::-1]


def solve(target, integers):
    count = (target % integers[0] == 0)
    while len(integers) > 1 and target > 0:
        count += solve(target, integers[1:])
        target -= integers[0]
    return count


answer = 10
while solve(answer, [p for p in primes if p < answer]) < 5000:
    answer += 1

print(answer)
