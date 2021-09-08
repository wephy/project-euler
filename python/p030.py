# Digit fifth powers

EXPONENT = 5


def solve():
    powers = [i**EXPONENT for i in range(10)]

    return sum(i for i in range(2, (EXPONENT + 1) * ((9**EXPONENT)))
               if i == sum(powers[int(i)] for i in str(i)))


if __name__ == "__main__":
    print(solve())
