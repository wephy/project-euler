# Large sum

f = open(r"large sum.txt", "r")

numbers = f.read().split('\n')

sum = 0
for number in numbers:
    sum += int(number)

sum = str(sum)
print(sum[:10])
