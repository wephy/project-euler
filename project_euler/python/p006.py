# Sum square difference

import numpy as np

sum1 = []
for n in range(1, 100 + 1):
    sum1.append(n ** 2)
sum1 = np.sum(sum1)

sum2 = 0
for n in range(1, 100 + 1):
    sum2 += n
sum2 **= 2

sum2 - sum1
