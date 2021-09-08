# Largest product in a series

function solve()
    open(joinpath("..", "data", "p008.txt")) do data
        number = join(readlines(data))
        return maximum(
            prod(parse(Int, n) for n in (number[i:(i + 12)]))
            for i in 1:(1000 - 13))
    end
end


print(Int(solve()))
