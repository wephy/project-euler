# Power digit sum

EXPONENT = 1000


def solve():
    return sum(int(digit) for digit in str(2**EXPONENT))


if __name__ == "__main__":
    print(solve())
