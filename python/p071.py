# Ordered fractions

LIMIT = 1_000_000


def solve():
    return (LIMIT - (LIMIT % 7 - 5) % 7) * 3 // 7


if __name__ == "__main__":
    print(solve())
