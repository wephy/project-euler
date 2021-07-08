# Counting rectangles

def h(w):
    return ((1 + 16 * 2_000_000 / (w * (w + 1)))**0.5 - 1) / 2


width = min(range(1, 54), key=lambda w: h(w) % 1)

print(width * round(h(width)))
