# 1000-digit Fibonacci number

fibs = [1, 1]
while len(str(fibs[-1])) < 1000:
    fibs.append(fibs[-1] + fibs[-2])

print(len(fibs))
