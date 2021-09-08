# Longest Collatz sequence

LIMIT = 1_000_000


def solve():
    chains = {}
    return max(range(LIMIT, 0, -1), key=lambda x: collatz(x, chains))


def collatz(n, chains):
    if n in chains.keys():
        return chains[n]
    elif n == 1:
        return 1

    if n % 2 == 0:
        length = collatz(n // 2, chains) + 1
    else:
        length = collatz(3 * n + 1, chains) + 1
    chains[n] = length
    return length


if __name__ == "__main__":
    print(solve())
