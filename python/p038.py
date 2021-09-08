# Pandigital multiples

from itertools import count


def solve():
    return concatenated_product(max(range(10_000), key=concatenated_product))


def concatenated_product(n):
    x = ""
    for i in count(1):
        if len(x) < 9:
            x += str(n * i)
        elif "".join(sorted(x)) == "123456789":
            return int(x)
        else:
            return 0


if __name__ == "__main__":
    print(solve())
