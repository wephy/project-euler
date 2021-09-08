# 1000-digit Fibonacci number

from itertools import count

DIGITS = 1000


def solve():
    fibs = [1, 1]
    for i in count():
        fibs.append(fibs[-1] + fibs[-2])
        if len(str(fibs[-1])) == DIGITS:
            return i + 3


if __name__ == "__main__":
    print(solve())
