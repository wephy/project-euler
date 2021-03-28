# Large sum

with open(r"p013.txt", "r") as f:
    numbers = f.read().split('\n')

answer = 0
for number in numbers:
    answer += int(number)
answer = str(answer)

print(answer[:10])
