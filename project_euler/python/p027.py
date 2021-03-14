# Quadratic primes

def is_prime(num):
    if num > 1:
        for fac in range(2, int(num**0.5 + 1)):
            if (num % fac) == 0:
                return False
        else:
            return True


def quadratic_primes(a, b):
    n = 0
    while True:
        if not is_prime(n ** 2 + a * n + b):
            return n
        else:
            n += 1


bound = 1000
largest = 0
answer = 0

for a in range(-999, 1000):
    for b in range(-999, 1001):
        p = quadratic_primes(a, b)
        if p > largest:
            largest = p
            answer = a * b

print(answer)
