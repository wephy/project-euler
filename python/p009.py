# Special Pythagorean triplet

for a in range(int(1000 / (2 + 2 ** 0.5)), 1000 // 2 + 1):
    for b in range(1, a):
        c = (a ** 2 + b ** 2) ** 0.5
        if a + b + c == 1000:
            print(int(a * b * c))
