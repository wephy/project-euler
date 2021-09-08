# Large non-Mersenne prime


def solve():
    return (28433 * pow(2, 7830457, 10**10) + 1) % 10**10


if __name__ == "__main__":
    print(solve())
