# Coin sums

COINS = [200, 100, 50, 20, 10, 5, 2, 1]
TARGET = 200


def ways(start=0, index=0, count=0):
    if index < 7:
        for i in range(start, TARGET+1, COINS[index]):
            count = ways(i, index+1, count)
    else:
        count += 1
    return count


print(ways())
