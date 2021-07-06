# Arranged probability

blue = 15
total = 21

while total < 1e12:
    blue, total = (3 * blue) + (2 * total) - 2, (4 * blue) + (3 * total) - 3

print(blue)
