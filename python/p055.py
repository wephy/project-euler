# Lychrel numbers

LIMIT = 10_000


def solve():
    def is_lychrel(n):
        for _ in range(50):
            n = n + int(str(n)[::-1])
            if str(n) == str(n)[::-1]:
                return False
        return True

    return sum(is_lychrel(i) for i in range(1, LIMIT))


if __name__ == "__main__":
    print(solve())
