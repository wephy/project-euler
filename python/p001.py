# Multiples of 3 and 5

LIMIT = 1000


def solve():
    return sum(i for i in range(LIMIT) if i % 3 == 0 or i % 5 == 0)


if __name__ == "__main__":
    print(solve())
