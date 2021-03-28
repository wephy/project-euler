# Digit factorials

from math import factorial

factorials = {}
for i in map(str, range(10)):
    factorials[i] = factorial(int(i))

answer = 0
for n in map(str, range(3, 2_540_160)):
    int_n = int(n)
    digits_sum = 0
    if '9' not in n and int_n > 362_880:
        continue
    for digit in n:
        digits_sum += factorials[digit]
    if digits_sum == int_n:
        answer += int_n

print(answer)
