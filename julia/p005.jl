# Smallest multiple

using Primes

LIMIT = 20


function solve()
    return prod(n^floor(log(n, LIMIT)) for n in primes(LIMIT))
end


print(Int(solve()))
