# Triangular, pentagonal, and hexagonal

def is_pentagon(n):
    return ((24 * n + 1) ** 0.5 + 1) % 6 == 0


def hexagon(n):
    return (n * (2 * n - 1))


x = 144
while not is_pentagon(hexagon(x)):
    x += 1

print(hexagon(x))

# One-line solution:
# for x in (x for x in range(144, 999_999) if ((48*x**2-24*x+1)**0.5+1)%6==0): print(2*x**2-x); break