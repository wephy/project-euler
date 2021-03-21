# Summation of primes

def is_prime(num):
    if num > 1:
        for fac in range(2, int(num ** 0.5 + 1)):
            if (num % fac) == 0:
                return False
        else:
            return True 


primes = []
i = 2

while i < 2000000:
    if is_prime(i):
        primes.append(i)
    i += 1

sum(primes)
