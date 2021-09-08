# Cyclical figurate numbers

from itertools import count


def solve():
    sets = {}

    def populate_set(set_order, formula):
        def f(x):
            return int(eval(formula.replace("n", f"{x}")))

        numbers = set()
        for i in count():
            y = f(i)
            if y > 10_000:
                break
            elif len(str(y)) == 4:
                numbers.add(y)
        sets[set_order] = numbers

    populate_set(0, "n * (n + 1) / 2")
    populate_set(1, "n ** 2")
    populate_set(2, "n * (3 * n - 1) / 2")
    populate_set(3, "n * (2 * n - 1)")
    populate_set(4, "n * (5 * n - 3) / 2")
    populate_set(5, "n * (3 * n - 2)")

    def find_solution(answer=[], types={x: False for x in [0, 1, 2, 3, 4, 5]}):
        if len(answer) > 0:
            first_two = str(answer[-1])[2:4]
        for i, s in sets.items():
            if types[i] is False:
                for x in s:
                    if (len(answer) == 5 and str(x)[0:2] == first_two
                            and str(x)[2:4] == str(answer[0])[0:2]):
                        yield sum(answer + [x])
                    elif len(answer) == 0 or str(x)[0:2] == first_two:
                        new_types = types.copy()
                        new_types[i] = True
                        yield from find_solution(answer + [x], new_types)

    return next(find_solution())


if __name__ == "__main__":
    print(solve())
