# Cyclical figurate numbers

def triangular(n): return ((8 * n + 1) ** 0.5 - 1) / 2
def square(n): return n ** 0.5
def pentagonal(n): return ((24 * n + 1) ** 0.5 + 1) / 6
def hexagonal(n): return ((8  *n + 1) ** 0.5 + 1) / 4
def heptagonal(n): return ((40 * n + 9) ** 0.5 + 3) / 10
def octagonal(n): return ((3 * n + 1) ** 0.5 + 1) / 3


for tri in [int(n * (n + 1) / 2) for n in range(
    int(triangular(1_000)), int(triangular(10_000)))]:

    for sqr in [int(n ** 2) for n in range(
    int(square(1_000)), int(square(10_000)))]:
        if str(sqr)[0:2] != str(tri)[2:4]:
            continue

        for pen in [int(n * (3 * n - 1) / 2) for n in range(
        int(pentagonal(1_000)), int(pentagonal(10_000)))]:
            if str(pen)[0:2] != str(sqr)[2:4]:
                continue
                    
            for hex in [int(n * (3 * n - 1) / 2) for n in range(
            int(hexagonal(1_000)), int(hexagonal(10_000)))]:
                if str(hex)[0:2] != str(pen)[2:4]:
                    continue

                for hep in [int(n * (5 * n - 3) / 2) for n in range(
                int(heptagonal(1_000)), int(heptagonal(10_000)))]:
                    if str(hep)[0:2] != str(hex)[2:4]:
                        continue
                            
                    for oct in [int(n * (3 * n - 2)) for n in range(
                    int(octagonal(1_000)), int(octagonal(10_000)))]:
                        if (str(oct)[0:2] != str(hep)[2:4]
                            or str(oct)[2:4] != str(tri)[0:2]):
                            continue
                        
                        print(sum([tri, sqr, pen, hex, hep, oct]))