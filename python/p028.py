# Number spiral diagonals

answer = 1
step = 0
current = 1
for i in range((1001 - 1) // 2):
    step += 2
    for _ in range(4):
        current += step
        answer += current

print(answer)
