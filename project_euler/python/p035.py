# Circular primes

def is_prime(num):
    if num > 1:
        for fac in range(2, int((num ** 0.5) + 1)):
            if (num % fac) == 0:
                return False
        return True


primes = []

for num in range(2, 1000000):
    if is_prime(num):
        primes.append(num)

primes_circular = []

for prime in primes:
    prime_string = str(prime)

    failed = False
    for _ in range(len(prime_string)):
        prime_string += prime_string[0]
        prime_string = prime_string[1:]
        if not is_prime(int(prime_string)):
            failed = True
    if not failed:
        primes_circular.append(prime)

print(len(primes_circular))
