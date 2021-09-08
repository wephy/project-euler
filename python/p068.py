# Magic 5-gon ring

from itertools import combinations, chain


def solve():
    external = range(6, 11)
    internal = range(1, 6)
    line_sum = (sum(external) + (2 * sum(internal))) / 5

    pairs = sorted(
        chain.from_iterable((x, x[::-1]) for x in combinations(internal, 2)),
        reverse=True,
    )
    pair_matches = []
    for ex in external:
        for pair in pairs:
            if sum(pair) + ex == line_sum:
                pair_matches.append([ex, *pair])
    pair_matches_sorted = sorted(pair_matches, reverse=True)

    def find_solution(solution=[], used=set()):
        if len(solution) == 5:
            if solution[-1][2] == solution[0][1]:
                yield "".join(map(str, [*chain.from_iterable(solution)]))
        elif len(solution) == 0:
            for match in pair_matches:
                yield from find_solution([match], {match[0]})
        else:
            for match in [p for p in pair_matches_sorted if p[0] not in used]:
                if match[1] == solution[-1][2]:
                    new_solution = solution + [match]
                    new_used = used.copy()
                    new_used.add(match[0])
                    yield from find_solution(new_solution, new_used)

    return next(find_solution())


if __name__ == "__main__":
    print(solve())
