# Large sum

with open("../data/p013.txt") as f:
    numbers = f.read().split('\n')

answer = 0
for number in numbers:
    answer += int(number)
answer = str(answer)

print(answer[:10])
