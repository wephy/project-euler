# Anagramic squares

import os
import numpy as np

data = set(np.char.strip(np.loadtxt(os.path.join("..", "data", "p098.txt"),
                                    delimiter=",", dtype=str), '"'))

sorted_words = {word: sorted(word) for word in data}

anagrams = []
for word in data.copy():
    data.remove(word)
    for pair in data:
        if sorted_words[word] == sorted_words[pair] and pair != word[::-1]:
            anagrams.append((word, pair))

squares = set([i**2 for i in range(
    int(10**(max(len(x[0]) for x in anagrams) + 1)**0.5))])
squares_placements = {square: sorted(
        {x: tuple(i for i, c in enumerate(str(square)) if c == x)
         for x in set(str(square))}.values()) for square in squares}

solutions = []
for word, pair in anagrams:
    word_placements = {x: tuple(i for i, c in enumerate(word) if c == x)
                       for x in set(word)}
    for square in squares:
        if sorted(word_placements.values()) == squares_placements[square]:
            substitutions = {x: str(square)[word_placements[x][0]]
                             for x in word_placements.keys()}
            number = "".join([substitutions[x] for x in pair])
            if number[0] != "0" and int(number) in squares:
                solutions.append(square)
                solutions.append(int(number))

print(max(solutions))
