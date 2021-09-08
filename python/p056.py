# Powerful digit sum


def solve():
    return max(
        sum(map(int, [digit for digit in str(a**b)]))
        for a in range(1, 100) for b in range(1, 100))


if __name__ == "__main__":
    print(solve())
