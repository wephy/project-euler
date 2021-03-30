# Prime permutations

from sympy import isprime

for i1 in [x for x in range(1000, 3340) if x != 1487]:
    i2, i3 = i1 + 3330, i1 + 2 * 3330
    if (any(isprime(x) is False for x in (i1, i2, i3)) or
            any(sorted(x) != sorted(str(i1)) for x in (map(str, [i2, i3])))):
        continue
    print(''.join(map(str, [i1, i2, i3])))
