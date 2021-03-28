# Even Fibonacci numbers

answer = 0
a, b = 1, 2
while a < 4_000_000:
    if a % 2 == 0:
        answer += a
    a, b = b, a + b

print(answer)
