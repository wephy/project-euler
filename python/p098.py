# Anagramic squares

import os
import numpy as np

data = set(np.char.strip(np.loadtxt(os.path.join("..", "data", "p098.txt"),
                                    delimiter=",", dtype=str), '"'))

sorted_words = {word: sorted(word) for word in data}


longest = 0
anagrams = []
for word1 in data.copy():
    for word2 in data:
        if (sorted_words[word1] == sorted_words[word2]
           and word2 not in [word1, word1[::-1]]):
            anagrams.append((word1, word2))
            if len(word1) > longest:
                longest = len(word1)
    data.remove(word1)

squares = set([i**2 for i in range(1, int(10**6**0.5))])
squares_placements = {square: sorted(
        {x: tuple(i for i, c in enumerate(str(square)) if c == x)
         for x in set(str(square))}.values()) for square in squares}

solutions = []
for word1, word2 in anagrams:
    word_placements = {x: tuple(i for i, c in enumerate(word1) if c == x)
                       for x in set(word1)}

    for square in squares:
        if sorted(word_placements.values()) == squares_placements[square]:
            substitutions = {k: str(square)[word_placements[k][0]]
                             for k in word_placements.keys()}

            new = ""
            for letter in word2:
                new += substitutions[letter]

            if new[0] == "0":
                continue
            elif int(new) in squares:
                solutions.append(square)
                solutions.append(int(new))

print(max(solutions))
