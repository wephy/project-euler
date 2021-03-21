# Power digit sum

digits = str(2 ** 1000)

x = 0
for digit in digits:
    x += int(digit)

print(x)
