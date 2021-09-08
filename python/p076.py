# Counting summations

from itertools import count


def solve():
    generalized = [1]
    for n in count(1):
        if generalized[-1] > 100:
            break
        generalized.append(n * (3 * n - 1) // 2)
        generalized.append((-n) * (3 * (-n) - 1) // 2)

    partitions = {0: 1}
    for x in range(1, 100 + 1):
        y = 0
        for i, p in enumerate([p for p in generalized[1:] if p <= x]):
            y += (-1)**((i // 2) % 2) * partitions[x - p]
        partitions[x] = y

    return partitions[100] - 1


if __name__ == "__main__":
    print(solve())
