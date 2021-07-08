# Almost equilateral triangles

answer = 0
v0, v1 = 0, 1
u0, u1 = 1, 2
while True:
    p = 2 * (u1**2 + v1**2) + 2 * (u1**2 - v1**2)
    if p > 1_000_000_000:
        break
    answer += p

    v0, v1 = v1, 4 * v1 - v0
    u0, u1 = u1, 4 * u1 - u0

    p = 2 * (v0**2 + v1**2) + (4 * v1 * v0)
    if p > 1_000_000_000:
        break
    answer += p

print(answer)
