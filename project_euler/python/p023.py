# Non-abundant sums
import datetime


def is_prime(num):
    if num > 1:
        for fac in range(2, int(num ** 0.5 + 1)):
            if (num % fac) == 0:
                return False
        return True


def divisors_sum(num):
    total = 0
    for i in range(1, (num // 2) + 1):
        if num % i == 0:
            total += i
    return total


print("Calculating abundant numbers...")
abundant_numbers = []
for n in range(1, 28123):
    if is_prime(n):
        continue
    if divisors_sum(n) > n:
        abundant_numbers.append(n)
print("OK\n")

print("Calculating abundant sums...")
abundant_sums = set()
for abundant1 in abundant_numbers:
    for abundant2 in abundant_numbers:
        abundant_sums.add(abundant1 + abundant2)
print("OK\n")

print("Calculating sum...")
total_sum = 0
for i in range(1, 28123):
    if i in abundant_sums:
        continue
    else:
        total_sum += i
print("OK\n")

print(total_sum)
