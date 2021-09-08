# Sub-string divisibility


def solve():
    def solutions(primes, n="", remaining=set(range(10))):
        if (length := len(n)) >= 4 and int(n[-3:]) % primes[length - 4] != 0:
            return
        elif not remaining:
            yield int(n)
        else:
            for digit in remaining:
                yield from solutions(primes, n + str(digit),
                                     remaining - {digit})

    return sum(solutions([2, 3, 5, 7, 11, 13, 17]))


if __name__ == "__main__":
    print(solve())
