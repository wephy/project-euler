# Names scores

from string import ascii_uppercase

with open("p022.txt", "r") as data:
    names = eval("[" + data.readline() + "]")

answer = 0
for index, name in enumerate(sorted(names)):
    value = 0
    for char in name:
        value += ascii_uppercase.index(char) + 1
    answer += (index + 1) * value

print(answer)
