# Sub-string divisibility

from itertools import permutations

primes = [2, 3, 5, 7, 11, 13, 17]

answer = 0
for p in map(lambda t: ''.join(map(str, t)),
             permutations([d for d in range(10)])):
    failed = False
    for i in range(7):
        if int(p[i+1:i+4]) % primes[i] != 0:
            failed = True
            break
    if not failed:
        answer += int(p)

print(answer)
