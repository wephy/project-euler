# Multiples of 3 and 5

def multiple_3_5(x):
    total = 0
    for m in range(x):
        if m % 5 == 0 or m % 3 == 0:
            total += m
            print(m, total)
    return total


multiple_3_5(1000)