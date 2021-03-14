# Digit fifth powers

numbers = []

for number in range(2, 999999):
    digits_5 = []
    for digit in str(number):
        digits_5.append(int(digit) ** 5)
    if sum(digits_5) == number:
        numbers.append(number)

print(sum(numbers))
