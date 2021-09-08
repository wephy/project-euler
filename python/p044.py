# Pentagon numbers

from itertools import count


def solve():
    def pentagon(n):
        return (3 * (n**2) - n) // 2

    def is_pentagon(n):
        return ((24 * n + 1)**0.5 + 1) % 6 == 0

    pentagons = {}
    for j in count():
        x = pentagon(j)
        pentagons[j] = x
        for k in range(j - 1, 0, -1):
            y = pentagons[k]
            if is_pentagon(x - y) and is_pentagon(x + y):
                return x - y


if __name__ == "__main__":
    print(solve())
