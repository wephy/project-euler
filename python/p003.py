# Largest prime factor

n = 600_851_475_143
i = 2
while n > 1:
    if n % i == 0:
        n /= i
    else:
        i += 1

print(i)
