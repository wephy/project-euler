# Permuted multiples

from itertools import count


def solve():
    for i in count(1):
        if len(set(map(lambda x: "".join(sorted(str(x))),
                       [i, i * 2, i * 3, i * 4, i * 5, i * 6]))) == 1:
            return i


if __name__ == "__main__":
    print(solve())
