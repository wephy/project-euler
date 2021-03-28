# Digit fifth powers

answer = 0
for number in range(2, 1_000_000):
    if number == sum(int(digit) ** 5 for digit in str(number)):
        answer += number

print(answer)
