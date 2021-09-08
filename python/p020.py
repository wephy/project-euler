# Factorial digit sum

from math import factorial

NUMBER = 100


def solve():
    return sum(int(digit) for digit in str(factorial(NUMBER)))


if __name__ == "__main__":
    print(solve())
