# Multiples of 3 and 5

LIMIT = 1000


function solve()
    return sum((i % 3 == 0 || i % 5 == 0) ? i : 0 for i in 1:(LIMIT - 1))
end


print(Int(solve()))
