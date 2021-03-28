# Amicable numbers

from sympy import divisors

answer = 0

for i in range(10_000):
    divisor_sum = sum(divisors(i)[:-1])
    if divisor_sum != i:
        if sum(divisors(divisor_sum)[:-1]) == i:
            answer += i

print(answer)
