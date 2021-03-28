# Non-abundant sums

from sympy import divisors

abundants = set()
for i in range(1, 28_123):
    if sum(divisors(i)[:-1]) > i:
        abundants.add(i)

answer = 0
for i in range(1, 28_123):
    for abundant in abundants:
        diff = i - abundant
        if diff in abundants:
            break
    if diff not in abundants:
        answer += i

print(answer)
