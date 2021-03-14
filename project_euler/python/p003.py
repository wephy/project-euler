# Largest prime factor

def is_prime(num):
    if num > 1:
        for factor in range(2, int(num ** 0.5 + 1)):
            if (num % factor) == 0:
                return False
        return True


def largest_prime_factor(num):
    i = 2
    while num > 1:
        if num % i == 0:
            num /= i
        else:
            i += 1
    return i


largest_prime_factor(13195)
