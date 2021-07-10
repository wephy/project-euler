# Cube digit pairs

from itertools import combinations

squares = [str(i**2).zfill(2) for i in range(1, 10)]


def test(cube1, cube2):
    combinations = set()

    for cube in [cube1, cube2]:
        if "6" in cube:
            cube.append("9")
        if "9" in cube:
            cube.append("6")

    for left in cube1:
        for right in cube2:
            combinations.add(f"{left}{right}")
            combinations.add(f"{right}{left}")
    for square in squares:
        if square not in combinations:
            return False
    return True


tested = set()
answer = 0
for perm1 in combinations([str(i) for i in range(10)], 6):
    tested.add(perm1)
    for perm2 in combinations([str(i) for i in range(10)], 6):
        if perm2 in tested:
            continue
        if test(list(perm1), list(perm2)):
            answer += 1

print(answer)
