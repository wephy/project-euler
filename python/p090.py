# Cube digit pairs

from itertools import combinations


def solve():
    squares = [str(i**2).zfill(2) for i in range(1, 10)]

    def test(cube1, cube2):
        for cube in [cube1, cube2]:
            if "6" in cube:
                cube.append("9")
            if "9" in cube:
                cube.append("6")
        for square in squares:
            x, y = square
            if (x not in cube1 or y not in cube2) and (x not in cube2
                                                       or y not in cube1):
                return False
        return True

    tested = set()
    answer = 0
    for cube1 in combinations([str(i) for i in range(1, 10)], 5):
        cube1 = tuple("0") + cube1
        missing = {"1", "2", "3", "4", "5", "8"}.difference(set([*cube1]))
        not_missing = {str(d) for d in range(10)}.difference(missing)
        tested.add(cube1)
        no6or9 = "6" not in cube1 and "9" not in cube1
        for cube2 in combinations(list(not_missing), 6 - len(missing)):
            if no6or9 and ("6" not in cube2 and "9" not in cube2):
                continue
            cube2 += tuple(missing)
            if tuple(sorted(cube2)) in tested:
                continue
            if test(list(cube1), list(cube2)):
                answer += 1

    return answer


if __name__ == "__main__":
    print(solve())
