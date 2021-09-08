# Arithmetic expressions

from itertools import product, permutations


def solve():
    operations = (
        lambda x, y: x + y,
        lambda x, y: x - y,
        lambda x, y: x * y,
        lambda x, y: x / y if y != 0 else None,
    )

    longest_count = 0
    for s1 in range(1, 7):
        for s2 in range(s1 + 1, 8):
            for s3 in range(s2 + 1, 9):
                for s4 in range(s3 + 1, 10):
                    answers = []
                    for a, b, c, d in permutations((s1, s2, s3, s4)):
                        for x, y, z in product(operations, repeat=3):
                            answers.append(z(y(x(a, b), c), d))
                            answers.append(z(x(a, y(b, c)), d))
                            answers.append(x(a, z(y(b, c), d)))
                            answers.append(x(a, y(b, z(c, d))))
                            answers.append(y(x(a, b), z(c, d)))

                    count = longest(
                        sorted(
                            set([
                                n for n in answers
                                if n and n % 1 == 0 and n > 0
                            ])))
                    if count > longest_count:
                        longest_count = count
                        longest_set = f"{s1}{s2}{s3}{s4}"

    return longest_set


def longest(s):
    if s[0] != 1:
        return 0
    for i in range(len(s)):
        if s[i] != i + 1:
            return s[i - 1]
    return len(s)


if __name__ == "__main__":
    print(solve())
