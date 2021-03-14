# Smallest multiple

def is_prime(num):
    if num > 1:
        for fac in range(2, int(num ** 0.5 + 1)):
            if (num % fac) == 0:
                return False
        else:
            return True 


def find_factors(num):
    list = []
    while num > 1:
        for n in range(2, int(num + 1)):
            if num % n == 0:
                if is_prime(n):
                    num /= n
                    list.append(n)
    return list


def smallest_multiple(upper):
    list = []
    for n in range(2,upper + 1):
        list.append(find_factors(n))

    answer = []
    for p in range(2,upper + 1):
        if is_prime(p):
            count = 0
            for factors in list:
                if factors.count(p) > count:
                    count = factors.count(p)
            for n in range(count):
                answer.append(p)

    print(answer)
    x = 1
    for i in answer:
        x *= i
    return x


smallest_multiple(30)
