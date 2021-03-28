
# Double-base palindromes

answer = 0

for d, b in map(lambda x: [str(x), bin(x)[2:]], range(1, 1_000_000)):
    if d == d[::-1] and b == b[::-1]:
        answer += int(d)

print(answer)
