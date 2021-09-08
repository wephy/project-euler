# Square root digital expansion

from decimal import Decimal, getcontext

DIGITS = 100


def solve():
    getcontext().prec = 102

    return sum(
        sum(map(int, filter(str.isdigit,
                            str(Decimal(i).sqrt())[:101])))
        for i in range(1, DIGITS + 1) if i**0.5 % 1)


if __name__ == "__main__":
    print(solve())
