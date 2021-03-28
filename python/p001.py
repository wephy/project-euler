# Multiples of 3 and 5

answer = 0
for m in range(1_000):
    if m % 5 == 0 or m % 3 == 0:
        answer += m

print(answer)
