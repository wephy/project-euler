# Coin partitions

generalized = [1]
n = 1
while generalized[-1] < 100_000:
    generalized.append(n * (3 * n - 1) // 2)
    generalized.append((-n) * (3 * (-n) - 1) // 2)
    n += 1

partitions = {0: 1}
for n in range(1, 100_000 + 1):
    count = 0
    for i, p in enumerate([p for p in generalized[1:] if p <= n]):
        count += (-1) ** ((i // 2) % 2) * partitions[n - p]
    if count % 1_000_000 == 0:
        print(n)
        break
    partitions[n] = count
