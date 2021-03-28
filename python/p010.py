# Summation of primes

answer = 0
composites = set()
for i in range(2, 2_000_000):
    if i not in composites:
        answer += i
        for p in range(i * 2, 2_000_000, i):
            composites.add(p)

print(answer)
