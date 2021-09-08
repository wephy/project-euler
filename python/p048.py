# Self powers

LIMIT = 1000


def solve():
    return str(sum(i**i for i in range(1, LIMIT + 1)))[-10:]


if __name__ == "__main__":
    print(solve())
