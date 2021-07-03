# Even Fibonacci numbers

a, b = 1, 2
answer = 0
while a < 4_000_000:
    if a % 2 == 0:
        answer += a
    a, b = b, a + b

print(answer)
