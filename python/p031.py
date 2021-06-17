# Coin sums

def solve(target, coins, start=0, index=0, count=0):
    if index < 7:
        for i in range(start, target+1, coins[index]):
            count = solve(target, coins, i, index+1, count)
    return count + (index >= 7)


print(solve(200, [200, 100, 50, 20, 10, 5, 2, 1]))
