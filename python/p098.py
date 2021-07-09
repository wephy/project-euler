# Anagramic squares

import os
import numpy as np
from itertools import combinations

data = set(np.char.strip(np.loadtxt(os.path.join("..", "data", "p098.txt"),
                                    delimiter=",", dtype=str), '"'))

words = {i: [w for w in data if len(w) == i] for i in range(15)}
w_hashes = {w: hash(tuple(sorted(w))) for w in data}
anagrams = np.array([(x, y) for lengths in words.values() for (x, y) in
                     combinations(lengths, 2) if w_hashes[x] == w_hashes[y]
                     and x != y[::-1]])

squares = set([i**2 for i in range(int(
               10**len(max(anagrams[:, 0], key=len))**0.5))])
s_hashes = {sq: hash(tuple(sorted(tuple(i for i, c in enumerate(str(sq))
            if c == y) for y in set(str(sq))))) for sq in squares}

solutions = []
for w, pair in anagrams:
    struct = {x: tuple(i for i, c in enumerate(w) if c == x) for x in set(w)}
    for sq in squares:
        if hash(tuple(sorted(struct.values()))) == s_hashes[sq]:
            substitutions = {x: str(sq)[struct[x][0]] for x in struct.keys()}
            number = "".join([substitutions[x] for x in pair])
            if number[0] != "0" and int(number) in squares:
                solutions += [sq, int(number)]

print(max(solutions))
