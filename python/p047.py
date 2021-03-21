# Distinct primes factors


number_factors = {}


def generate_factors(n, c):
    factors = []
    factors_count = 0
    i = 2

    x = n
    while i <= x:
        if factors_count > c:
            number_factors[n] = False
            return False

        count = 0
        while x % i == 0:
            x /= i
            count += 1

        if count > 0:
            factors.append(i ** count)
            factors_count += 1

        i += 1

    if factors_count != c:
        number_factors[n] = False
        return False

    number_factors[n] = factors


def test(n, c):
    generate_factors(n+c-1, c)

    factors = set()
    for i in range(n, n+c):
        if not number_factors[i]:
            return False
        for factor in number_factors[i]:
            if factor in factors:
                return False
            factors.add(factor)
    return True


C = 4
for i in range(1, C):
    generate_factors(i, C)


n = 1
while True:
    if test(n, C):
        print(n)
        break
    print(n)
    n += 1
