# Number spiral diagonals

SIZE = 1001


def solve():
    n = (SIZE - 1) // 2
    return 1 + (10 * n**2) + ((16 * n**3) + (26 * n)) // 3


if __name__ == "__main__":
    print(solve())
