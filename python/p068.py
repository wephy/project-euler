# Magic 5-gon ring

from itertools import combinations, chain

line_sum = (sum(i for i in range(6, 11)) + 2 * sum(i for i in range(1, 6))) / 5

external = [i for i in range(6, 11)]
internal = [i for i in range(1, 6)]
pairs = sorted(
    [*chain.from_iterable((x, x[::-1]) for x in combinations(internal, 2))],
    reverse=True)
pair_matches = []
for ex in external:
    for pair in pairs:
        if sum(pair) + ex == line_sum:
            pair_matches.append([ex, *pair])
pair_matches_sorted = sorted(pair_matches, reverse=True)


def solve(solution=[], used=set()):
    if len(solution) == 5:
        if solution[-1][2] == solution[0][1]:
            print(''.join(map(str, [*chain.from_iterable(solution)])))
            return True
    elif len(solution) == 0:
        for match in pair_matches:
            if solve([match], {match[0]}):
                break
    else:
        for match in [p for p in pair_matches_sorted if p[0] not in used]:
            if match[1] == solution[-1][2]:
                new_solution = solution + [match]
                new_used = used.copy()
                new_used.add(match[0])
                if solve(new_solution, new_used):
                    return True


solve()
