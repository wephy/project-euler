# Special Pythagorean triplet

def pythag(d):
    for a in range(1, d // 2):
        for b in range(1, d // 2):
            c = (a ** 2 + b ** 2) ** 0.5
            if a + b + c == d:
                return int(a * b * c)


pythag(1000)
