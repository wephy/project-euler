# Powerful digit sum

answer = 0
for a in range(1, 100):
    for b in range(1, 100):
        n = sum(list(map(int, [digit for digit in str(a ** b)])))
        if n > answer:
            answer = n

print(answer)        