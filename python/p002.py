# Even Fibonacci numbers

LIMIT = 4_000_000


def solve():
    a, b = 1, 2
    answer = 0
    while a < LIMIT:
        if a % 2 == 0:
            answer += a
        a, b = b, a + b
    return answer


if __name__ == "__main__":
    print(solve())
