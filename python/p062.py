# Cubic permutations

from itertools import count


def solve():
    perms = {}
    for i in count():
        x = hash(tuple(sorted(str(i**3))))
        if x not in perms:
            perms[x] = 0
        perms[x] += 1
        if perms[x] == 5:
            break

    for i in count():
        if hash(tuple(sorted(str(i**3)))) == x:
            return i**3


if __name__ == "__main__":
    print(solve())
