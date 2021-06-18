# Square root digital expansion

from decimal import *

getcontext().prec = 102

answer = 0
for i in [i for i in range(1, 100 + 1) if (i ** 0.5 % 1)]:
    answer += sum(map(int, filter(str.isdigit, str(Decimal(i).sqrt())[:101])))

print(answer)
