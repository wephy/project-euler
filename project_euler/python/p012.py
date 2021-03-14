# Highly divisible triangular number

def triangle(num):
    i=num
    n = 0
    while i>0:
        n += i
        i -= 1
    return n


def find_divisors(num):
    count = 0
    for i in range(1, int(num ** 0.5 + 1)):
        if num % i == 0:
            count += 2
    return count


found = False
n = 2
while not found:
    if find_divisors(triangle(n)) > 500:
        found = True
        print(triangle(n))
    n += 1
