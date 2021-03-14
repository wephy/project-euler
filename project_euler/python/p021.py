# Amicable numbers

def d(n):
    divList = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            divList.append(i)
    divSum = 0
    for divisor in divList:
        divSum += divisor
    return divSum    


amicSum = 0

for a in range(1, 10000):
    dA = d(a)
    for b in range(a+2, 3*a, 2):
        if a == b or dA != b or b >= 10000:
            continue
        dB = d(b)

        if dB == a:
            amicSum += a + b
    
print(amicSum)
