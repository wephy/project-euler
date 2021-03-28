# Pandigital products

from sympy import divisors


def pandigital_product(n):
    pairs = []
    divisors_list = divisors(n)[1:-1]
    for i in range((len(divisors_list) + 1) // 2):
        pairs.append([divisors_list[i], divisors_list[-i-1]])
    for pair in pairs:
        digits = "".join(map(str, [n, pair[0], pair[1]]))
        if ''.join(sorted(digits)) == "123456789":
            return True


answer = 0
for i in range(1_000, 10_000):
    if pandigital_product(i):
        answer += i

print(answer)
