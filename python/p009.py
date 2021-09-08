# Special Pythagorean triplet

TRIPLET_SUM = 1000


def solve():
    for b in range(int(TRIPLET_SUM / (2 + 2**0.5)), TRIPLET_SUM // 2 + 1):
        for a in range(1, b):
            c = (a**2 + b**2)**0.5
            if a + b + c == TRIPLET_SUM:
                return int(a * b * c)


if __name__ == "__main__":
    print(solve())
