# Double-base palindromes

LIMIT = 1_000_000


def solve():
    return sum(
        int(d) for d, b in map(lambda x: (str(x), bin(x)[2:]), range(1, LIMIT))
        if d == d[::-1] and b == b[::-1])


if __name__ == "__main__":
    print(solve())
