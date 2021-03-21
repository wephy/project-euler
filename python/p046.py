# Goldbach's other conjecture

squares = [{'n': 1, 's': 1}]
primes = [2]


def is_prime(num):
    if num > 1:
        for fac in range(2, int(num ** 0.5 + 1)):
            if (num % fac) == 0:
                return False
        return True


def prime_gen():
    n = primes[-1] + 1
    while True:
        if is_prime(n):
            primes.append(n)
            break
        n += 1


def square_gen():
    n = squares[-1]['n'] + 1
    squares.append({'n': n, 's': n**2})


def conjecture(c):
    while c > primes[-1]:
        prime_gen()
    for p in primes:
        while c > squares[-1]['s']:
            square_gen()
        for square in squares:
            if c == (p + 2 * square['s']):
                return True
    return False


c = 3
while True:
    # if C is composite
    if not is_prime(c):
        if not conjecture(c):
            print(c)
            break
    c += 2
