# Truncatable primes

def is_prime(num):
    if num > 1:
        for fac in range(2, int(num ** 0.5 + 1)):
            if (num % fac) == 0:
                return False
        return True


truncatable_primes = []

num = 11
while len(truncatable_primes) < 11:
    failed = False
    num_string = str(num)

    while not failed:
        if is_prime(num):
            for i in range(1, len(num_string)):
                if not (is_prime(int(num_string[:-i]))) or not (
                        is_prime(int(num_string[i:]))):
                    failed = True
        else:
            failed = True
            
        if not failed:
            truncatable_primes.append(num)
        break

    num += 2

print(truncatable_primes)
print(sum(truncatable_primes))