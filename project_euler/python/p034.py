# Digit factorials

import math

answer = 0
for num in range(3, 99999): #should increase range, but need to optimise 
    num_string = str(num)
    digits_fac_sum = 0

    for digit in num_string:
        digits_fac_sum += math.factorial(int(digit))

    if digits_fac_sum == num:
        answer += num

print(answer)