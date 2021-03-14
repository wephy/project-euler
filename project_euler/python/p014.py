# Longest Collatz sequence

def collatz_count(n):
    counter = 1
    while n > 1:
        if n % 2 == 0:
            n = n/2
            counter += 1
        else:
            n = 1.5*n + 0.5
            counter += 2
    return counter


upper = 1000000
maxC = 0
maxN = 0

for i in range(int(upper/2), upper):
    if collatz_count(i) > maxC:
        maxC = collatz_count(i)
        maxN = i

print(maxN, maxC)
