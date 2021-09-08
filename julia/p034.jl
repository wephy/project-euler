# Digit factorials

function solve()
    factorials = [factorial(i) for i in 0:9]
    return sum(n for n in 3:2_540_160
               if sum(factorials[parse(Int, i) + 1] for i in string(n)) == n)
end


print(Int(solve()))
