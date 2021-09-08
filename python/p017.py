# Number letter counts


def solve():
    letters = 0
    for i in range(1, 1001):
        word = to_word(i)
        letters += len(word.replace(" ", ""))
    return letters


def to_word(n):
    below_20 = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
    }
    above_20 = {
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety",
    }
    powers = {1000: "thousand", 100: "hundred"}

    word = ""

    if n == 1000:
        word += " ".join([below_20[n // 1000], powers[1000]])
        n = int(str(n)[-3:])

    if n >= 100:
        word += " ".join([below_20[n // 100], powers[100]])
        n = int(str(n)[-2:])
        if n > 0:
            word += " and "

    if n >= 20:
        word += " ".join([above_20[n // 10]])
        n = int(str(n)[-1:])
        if n >= 1:
            word += " " + below_20[n]

    elif n >= 1:
        word += below_20[n]

    return word


if __name__ == "__main__":
    print(solve())
