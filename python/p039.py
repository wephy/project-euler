# Integer right triangles

from sympy import divisors

perimeters = []
for r in range(2, 1000 // 3, 2):
    div_list = divisors(r ** 2 // 2)
    for i in range((len(div_list) + 1) // 2):
        p = 3 * r + 2 * (div_list[i] + div_list[-i-1])
        if p <= 1000:
            perimeters.append(p)

print(max(perimeters, key=perimeters.count))
