# Counting rectangles

RECTANGLES = 2_000_000


def solve():
    def height(w):
        return ((1 + 16 * RECTANGLES / (w * (w + 1)))**0.5 - 1) / 2

    width = min(range(1, 54), key=lambda w: height(w) % 1)

    return width * round(height(width))


if __name__ == "__main__":
    print(solve())
