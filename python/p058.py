# Spiral primes

from sympy import isprime


def solution(side=1, diagonals=[1]):
    primes = set()
    while True:
        side += 2
        for _ in range(4):
            new_diagonal = diagonals[-1] + side - 1
            diagonals.append(new_diagonal)
            if isprime(new_diagonal):
                primes.add(new_diagonal)
        if len(primes) / len(diagonals) < 0.1:
            return side


print(solution())
