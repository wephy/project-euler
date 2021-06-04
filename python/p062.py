# Cubic permutations

i = hash = 0
perms = {i: hash}
while perms[hash] != 5:
    hash = tuple(sorted([*str(i ** 3)]))
    if hash not in perms:
        perms[hash] = 0
    perms[hash] += 1
    i += 1

i = 0
while tuple(sorted([*str(i ** 3)])) != hash:
    i += 1

print(i ** 3)
