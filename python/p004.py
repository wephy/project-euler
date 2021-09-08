# Largest palindrome product

DIGITS = 3


def solve():
    return max(p for x in range(10**(DIGITS - 1), 10**DIGITS)
               for y in range(x, 10**DIGITS)
               if str(p := x * y) == str(p)[::-1])


if __name__ == "__main__":
    print(solve())
