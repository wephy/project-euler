# Pandigital prime

import itertools
from sympy import isprime

answer = 0
for n in range(1, 10):
    p_array = []
    for i in range(1, n + 1):
        p_array.append(i)
    perms = list(itertools.permutations(p_array))
    for p in perms:
        p_string = ""
        for number in p:
            p_string += str(number)
        p_number = int(p_string)
        if (isprime(p_number)):
            if (p_number > answer):
                answer = p_number

print(answer)
