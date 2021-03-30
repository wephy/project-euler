# Sum square difference

import numpy as np

sum1 = sum2 = 0
for n in range(1, 100 + 1):
    sum1 += n ** 2
    sum2 += n
sum2 = sum2 ** 2

print(sum2 - sum1)
