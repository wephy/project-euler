# 1000-digit Fibonacci number

fibNums = [1, 1]
while len(str(fibNums[-1])) < 1000:
    fibNums.append(fibNums[-1] + fibNums[-2])
print(len(fibNums))
