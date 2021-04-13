# Prime digit replacements

from sympy import sieve
from sympy.utilities.iterables import multiset_permutations

primes = set(sieve.primerange(0, 1_000_000))


def testable_numbers(digits, numbers, number="", min_digit=0):
    for i in range(min_digit, 10):
        new_number = number + str(i)
        if len(new_number) < digits:
            testable_numbers(
                digits,
                numbers,
                number=new_number,
                min_digit=int(new_number[0]))
        else:
            numbers.append(new_number)


def test_perm(perm):
    failures = 0
    for replacement_digit in range(10):
        test_perm = perm.replace('*', str(replacement_digit))
        if test_perm[0] == '0' or int(test_perm) not in primes:
            failures += 1
        if failures > 2:
            return False
    return True


def find_perm():
    digits = 4
    while True:
        numbers = []
        testable_numbers(digits-3, numbers)
        for test_n in numbers:
            arrangement = [d for d in str(test_n)] + ['*', '*', '*']
            permutations = list(multiset_permutations(arrangement))
            for permutation in permutations:
                permutation = ''.join(permutation)
                if test_perm(permutation):
                    return permutation
        digits += 1


def solution():
    answer_perm = find_perm()
    for i in range(10):
        smallest = answer_perm.replace('*', str(i))
        if int(smallest) in primes:
            return smallest


print(solution())
