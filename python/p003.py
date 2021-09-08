# Largest prime factor

NUMBER = 600_851_475_143


def solve():
    n = NUMBER
    i = 2
    while n > 1:
        if n % i == 0:
            n /= i
        else:
            i += 1
    return i


if __name__ == "__main__":
    print(solve())
