# Pandigital multiples

answer = 0
for i in range(10_000):
    product = ""
    multiplier = 1
    while len(product) < 9:
        product += str(multiplier * i)
        multiplier += 1
    if ''.join(sorted(product)) == '123456789':
        if int(product) > answer:
            answer = int(product)

print(answer)
