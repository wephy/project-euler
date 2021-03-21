# Pandigital multiples

def concatenated_product(n):
    product = ""
    i = 1
    while True:
        concatenated = str(n * i)
        if len(product) + len(concatenated) > 9:
            break
        product += str(concatenated)
        i += 1

    return int(product)


highest_product = 0
for n in range(1, 1000000//2):
    n_product = concatenated_product(n)
    n_product_string = str(n_product)

    pandigital = True
    for d in range(1, 10):
        if ((n_product_string.count(str(d))) > 1 or
           (n_product_string.count(str(d))) < 1):
            pandigital = False
    if pandigital is False:
        continue

    if n_product > highest_product:
        highest_product = n_product

print(highest_product)
