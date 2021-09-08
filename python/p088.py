# Product-sum numbers

LIMIT = 12_000


def solve():
    cache = {}

    def kernel(limit, val=1, prod=[], depth=0, cumul=0):
        start = prod[-1] if depth > 0 else 2
        for i in range(start, LIMIT):
            new_val = val * i
            if new_val > limit:
                return
            new_prod = prod + [i]
            k = depth + 1 + new_val - (cumul + i)
            if k not in cache:
                cache[k] = new_val
            elif new_val < cache[k]:
                cache[k] = new_val
            kernel(limit, new_val, new_prod, depth + 1, cumul + i)

    kernel(LIMIT * 2)

    return sum({cache[k] for k in cache if k >= 2 and k <= LIMIT})


if __name__ == "__main__":
    print(solve())
