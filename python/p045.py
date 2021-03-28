# Triangular, pentagonal, and hexagonal

def is_pentagon(n):
    return ((24 * n + 1) ** 0.5 + 1) % 6 == 0


def hexagon(n):
    return (n * (2 * n - 1))


x = 144
while not is_pentagon(hexagon(x)):
    x += 1

print(hexagon(x))
