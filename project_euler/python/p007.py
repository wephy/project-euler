# 10001st prime

def is_prime(num):
    if num > 1:
        for fac in range(2, int(num ** 0.5 + 1)):
            if (num % fac) == 0:
                return False
        else:
            return True 


primes = []

n = 2
while len(primes) <= 10000:
    if is_prime(n):
        primes.append(n)
    n += 1

primes[10001 - 1]