# Counting Sundays

from datetime import datetime


def solve():
    return sum(
        datetime(y, m, 1).weekday() == 6 for y in range(1901, 2000 + 1)
        for m in range(1, 12 + 1))


if __name__ == "__main__":
    print(solve())
