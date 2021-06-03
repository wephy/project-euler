# # Cyclical figurate numbers

def populate_set(sets, set_order, formula):
    def f(x): return int(eval(formula.replace("n", f"{x}")))
    numbers = set()
    i = 0
    while f(i) < 10_000:
        if len(str(f(i))) == 4:
            numbers.add(f(i))
        i += 1
    sets[set_order] = numbers


def solve(sets, answer=[], types={x: False for x in [0, 1, 2, 3, 4, 5]}):
    if len(answer) > 0:
        first_two = str(answer[-1])[2:4]
    for i, s in sets.items():
        if types[i] == True:
            continue
        for x in s:
            if (len(answer) == 5 and str(x)[0:2] == first_two
                and str(x)[2:4] == str(answer[0])[0:2]):
                return sum(answer + [x])
            if len(answer) == 0 or str(x)[0:2] == first_two:
                new_types = types.copy()
                new_types[i] = True
                solution = solve(sets, answer + [x], new_types)
                if solution:
                    return solution


sets = {}

populate_set(sets, 0, "n * (n + 1) / 2")
populate_set(sets, 1, "n ** 2")
populate_set(sets, 2, "n * (3 * n - 1) / 2")
populate_set(sets, 3, "n * (2 * n - 1)")
populate_set(sets, 4, "n * (5 * n - 3) / 2")
populate_set(sets, 5, "n * (3 * n - 2)")

print(solve(sets))
