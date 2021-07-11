# Product-sum numbers

def solve(cache, target, limit, val=1, prod=[], depth=0, cumul=0):
    start = prod[-1] if depth > 0 else 2
    for i in range(start, target):
        new_val = val * i
        if new_val > limit:
            return
        new_prod = prod + [i]
        k = depth + 1 + new_val - (cumul + i)
        if k not in cache:
            cache[k] = new_val
        elif new_val < cache[k]:
            cache[k] = new_val
        solve(cache, target, limit, new_val, new_prod, depth+1, cumul+i)


target = 12_000
cache = {}
solve(cache, target, target * 2)

print(sum({cache[k] for k in cache if k >= 2 and k <= target}))
