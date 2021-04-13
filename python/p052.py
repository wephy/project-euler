# Permuted multiples

def solve(x=1):
    while True:
        if len(set(map(lambda x: ''.join(sorted(str(x))),
                       [x, x*2, x*3, x*4, x*5, x*6]))) == 1:
            return x
        x += 1


%time print(solve())