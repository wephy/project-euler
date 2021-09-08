# Coin sums

TARGET = 200
COINS = [200, 100, 50, 20, 10, 5, 2, 1]


def solve():
    ways = [1] + ([0] * TARGET)
    for coin in COINS:
        for i in range(coin, TARGET + 1):
            ways[i] += ways[i - coin]
    return int(ways[-1])


if __name__ == "__main__":
    print(solve())
