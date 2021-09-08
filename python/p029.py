# Distinct powers

LIMIT = 100


def solve():
    return len(
        set([a**b for a in range(2, LIMIT + 1) for b in range(2, LIMIT + 1)]))


if __name__ == "__main__":
    print(solve())
