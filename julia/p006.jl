# Sum square difference

LIMIT = 100


function solve()
    return sum(1:LIMIT)^2 - sum(n^2 for n in 1:LIMIT)
end


print(Int(solve()))