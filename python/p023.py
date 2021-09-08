# Non-abundant sums

from sympy import divisors

LIMIT = 28123


def solve():
    abundants = set()
    for i in range(1, LIMIT):
        if sum(divisors(i)[:-1]) > i:
            abundants.add(i)

    answer = 0
    for i in range(1, LIMIT):
        for abundant in abundants:
            diff = i - abundant
            if diff in abundants:
                break
        if diff not in abundants:
            answer += i
    return answer


if __name__ == "__main__":
    print(solve())
