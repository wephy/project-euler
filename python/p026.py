# Reciprocal cycles

from itertools import count

LIMIT = 1000


def solve():
    return max(range(1, LIMIT), key=cycle_length)


def cycle_length(n):
    seen = {}
    x = 1
    for i in count():
        if x in seen:
            return i - seen[x]
        seen[x] = i
        x = (10 * x) % n


if __name__ == "__main__":
    print(solve())
