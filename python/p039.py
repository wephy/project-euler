# Integer right triangles

def get_solutions(p):
    solutions = []
    limit = int(p // (2 + (2 ** 0.5)))
    for i in range(1, limit):
        for n in range(i, limit*2+1):
            a = i
            b = n - i
            c = p - n
            # print(a, b ,c)
            if a ** 2 + b ** 2 == c ** 2:
                solutions.append((a, b, c))
    return solutions


max_solutions = 0
max_solution_p = 0
for p in range(1, 1001):
    solutions = get_solutions(p)
    if len(solutions) > max_solutions:
        max_solutions = len(solutions)
        max_solution_p = p
print(max_solution_p)