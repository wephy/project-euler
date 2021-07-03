# Largest palindrome product

answer = 0
for x in range(999, 99, -1):
    for product in (x * y for y in range(x, 99, -1)):
        if product < answer:
            break
        if str(product) == str(product)[::-1]:
            answer = product

print(answer)
