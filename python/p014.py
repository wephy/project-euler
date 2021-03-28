# Longest Collatz sequence

counts = {}


def collatz(n):
    i = n
    counter = 1
    while i > 1:
        if i in counts:
            return counter + counts[i]
        if i % 2 == 0:
            i = i // 2
            counter += 1
        else:
            i = int(1.5 * i + 0.5)
            counter += 2
    return counter


for i in range(1, 1_000_000):
    counts[i] = collatz(i)

print(max(counts, key=lambda k: counts[k]))
