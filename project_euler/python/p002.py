# Even Fibonacci numbers

fib = [1, 2]


def fib_gen():
    fib.append(fib[-2] + fib[-1])


def fib_max(max):
    while True:
        fib_gen()
        if fib[-1] > max:
            return fib[:-1]


def even_count(list_input):
    print(list_input)
    total = 0
    for num in list_input:
        if num % 2 == 0:
            total += num
    return total


even_count(fib_max(4000000))
