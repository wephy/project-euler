# Sum square difference

LIMIT = 100


def solve():
    return sum(range(LIMIT + 1))**2 - sum(n**2 for n in range(LIMIT + 1))


if __name__ == '__main__':
    print(solve())
