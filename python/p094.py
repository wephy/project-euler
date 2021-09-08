# Almost equilateral triangles

LIMIT = 1_000_000_000


def solve():
    answer = 0
    v0, v1 = 0, 1
    u0, u1 = 1, 2
    while True:
        v0, v1 = v1, 4 * v1 - v0
        u0, u1 = u1, 4 * u1 - u0
        for p in [
                2 * (u0**2 + v0**2) + 2 * (u0**2 - v0**2),
                2 * (v0**2 + v1**2) + (4 * v1 * v0),
        ]:
            if p > LIMIT:
                return answer
            answer += p


if __name__ == "__main__":
    print(solve())
