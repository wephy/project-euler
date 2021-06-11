# Totient permutation

from sympy import isprime

def test(n):
    m = n / 11
    if m.is_integer():
        m = int(m - 1) * 10
        if sorted(str(m)) == sorted(str(n)):
            return True
    return False


x = 10 ** 7
while not test(x):
    x -= 1

print(x)

test(9899890)