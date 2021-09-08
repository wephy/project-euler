# Pandigital products


def solve():
    return sum(
        set(c for a in range(1, 100) for b in range(100, 10_000 // a)
            if "".join(sorted(str(a) + str(b) +
                              str(c := a * b))) == "123456789"))


if __name__ == "__main__":
    print(solve())
