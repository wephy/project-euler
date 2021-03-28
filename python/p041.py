# Pandigital prime

import itertools


def is_prime(num):
    if num > 1:
        for fac in range(2, int(num**0.5 + 1)):
            if (num % fac) == 0:
                return False
        return True


answer = 0
for n in range(1, 10):
    permutation_array = []
    for i in range(1, n + 1):
        permutation_array.append(i)
    permutations = list(itertools.permutations(permutation_array))
    for permutation in permutations:
        permutation_string = ""
        for number in permutation:
            permutation_string += str(number)
        permutation_number = int(permutation_string)
        if (is_prime(permutation_number)):
            if (permutation_number > answer):
                answer = permutation_number

print(answer)
