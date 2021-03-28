# Power digit sum

digits = str(2 ** 1000)

answer = 0
for digit in digits:
    answer += int(digit)

print(answer)
