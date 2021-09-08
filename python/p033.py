# Digit cancelling fractions

import numpy as np


def solve():
    fractions = np.array([(n, d) for d in range(10, 100) for n in range(10, d)
                          if test(n, d)])
    x, y = np.prod(fractions, axis=0)
    return y // np.gcd(x, y)


def test(x, y):
    return (y % 10 != 0
            and ((x % 10 == y // 10 and x / y == (x // 10) / (y % 10)) or
                 (x // 10 == y % 10 and x / y == (x % 10) / (y // 10))))


if __name__ == "__main__":
    print(solve())
