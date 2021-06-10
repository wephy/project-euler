# Magic 5-gon ring

import numpy as np

solutions = set()
numbers = set(i for i in range(1, 11))
pairs = set()


def solve(total, sides=np.zeros((5, 3)), used=set(), n=0):
    if n == 15:
        if sum(sides[-1]) == total:
            for pair in sides:
                pairs.add(tuple(pair))
            solutions.add("".join([str(int(x)) for x in sides.flatten()]))
        return

    side, depth = divmod(n, 3)
    if side == 1:
        if tuple(sides[0]) in pairs:
            return
    if sides[side][depth] != 0:
        solve(total, sides, used, n+1)
    else:
        for number in numbers.difference(used):
            new_sides = sides.copy()
            new_sides[side][depth] = number
            if depth == 2:
                new_sides[side+1][1] = number
            if side == 0 and depth == 1:
                new_sides[-1][2] = number
            if depth != 2 or sum(new_sides[side]) == total:
                solve(total, new_sides, used.union(set([number])), n+1)


for total_sum in range(14, 17):
    solve(total_sum)

solutions = filter(lambda x: len(x) == 16, solutions)
print(max([*map(int, solutions)]))
