# Su Doku

import os
import numpy as np
from itertools import chain

with open(os.path.join("..", "data", "p096.txt"), encoding="utf-8") as f:
    rows = np.delete(np.array(f.readlines()), slice(None, None, 10))
    sudokus = np.split(np.genfromtxt(rows, np.uint8, delimiter=[1]*9), 50)

digits = set(range(1, 10))
coords = list(np.ndindex(9, 9))


def solve(board):
    if 0 not in chain.from_iterable(board):
        return int("".join([str(i) for i in board[0, 0:3]]))
    candidates = {(y, x): digits - set([
        *board[y, :], *board[:, x],
        *chain.from_iterable(board[y//3*3:y//3*3+3, x//3*3:x//3*3+3])]
        ) for (y, x) in coords if board[y, x] == 0}
    coord = min(candidates, key=lambda x: len(candidates[x]))
    for i in candidates[coord]:
        board[coord] = i
        number = solve(board)
        if number:
            return number
        board[coord] = 0


print(sum(solve(sudokus[n]) for n in range(50)))
