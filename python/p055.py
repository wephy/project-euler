# Lychrel numbers

def lychrel(n):
    for _ in range(50):
        n = int(n) + int(str(n)[::-1])
        if str(n) == str(n)[::-1]:
            return False
    return True


answer = 0
for n in range(10_000):
    if lychrel(n):
        answer += 1

print(answer)
