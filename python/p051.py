# Prime digit replacements

from sympy import isprime, nextprime
from itertools import repeat


def solve():
    def prime_gen():
        n = 1
        while True:
            yield (n := nextprime(n))

    for i in prime_gen():
        for d in map(str, range(10)):
            if (x := str(i)).count(d) >= 3:
                it = iter(
                    isprime(y) for j in range(10)
                    if (y := int(x.replace(d, str(j)))) >= i)
                if all(map(any, repeat(iter(it), 8))):
                    return i


if __name__ == "__main__":
    print(solve())
