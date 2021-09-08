# Digit factorials

from math import factorial


def solve():
    factorials = [factorial(i) for i in range(10)]
    return sum(n for n in range(3, 2_540_160)
               if sum(factorials[int(i)] for i in str(n)) == n)


if __name__ == "__main__":
    print(solve())
