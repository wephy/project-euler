# Sub-string divisibility

from itertools import permutations

primes = [2, 3, 5, 7, 11, 13, 17]
answer = 0

digits = []
for i in range(0, 10):
    digits.append(i)

for permutation in list(permutations(digits)):
    pandigital = ""
    for digit in permutation:
        pandigital += str(digit)
    if pandigital[0] == "0":
        continue

    passed = True
    for d in range(1, 8):
        sub_string = str(pandigital[d] + 
                         pandigital[d + 1] + 
                         pandigital[d + 2])
        if int(sub_string) % primes[d-1] != 0:
            passed = False
            break
    if passed:
        answer += int(pandigital)

print(answer)
