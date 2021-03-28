# Factorial digit sum

from math import factorial

answer = 0
for digit in str(factorial(100)):
    answer += int(digit)

print(answer)
