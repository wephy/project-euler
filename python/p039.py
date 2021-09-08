# Integer right triangles

from sympy import divisors

LIMIT = 1000


def solve():
    solutions = {i: 0 for i in range(2, LIMIT, 2)}
    for r in range(2, LIMIT // 3, 2):
        r_divisors = divisors(r**2 // 2)
        for i in range((len(r_divisors) + 1) // 2):
            p = 3 * r + 2 * (r_divisors[i] + r_divisors[-i - 1])
            if p in solutions:
                solutions[p] += 1
    return max(solutions, key=solutions.get)


if __name__ == "__main__":
    print(solve())
