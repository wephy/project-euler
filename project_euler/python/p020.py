# Factorial digit sum

from math import factorial

x = 0
for digit in str(factorial(100)):
    x += int(digit)

print(x)
