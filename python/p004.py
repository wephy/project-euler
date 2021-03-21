# Largest palindrome product

def test(num):
    num = str(num)
    if num == num[::-1]:
        return True
    return False


largest = 0
for x in range(100, 1000):
    for y in range(100, 1000):
        if test(x*y):
            if (x*y) > largest:
                largest = x*y


print(largest)
