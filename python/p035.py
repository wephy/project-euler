# Circular primes

composites = set()
primes = set()
for i in range(2, 1_000_000):
    if i not in composites:
        primes.add(str(i))
        for p in range(i * 2, 1_000_000, i):
            composites.add(p)

answer = 0
for prime in primes:
    failed = False
    for _ in range(len(prime)):
        prime = prime[-1] + prime[:-1]
        if prime not in primes:
            failed = True
            break
    if not failed:
        answer += 1

print(answer)
