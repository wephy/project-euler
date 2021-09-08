# Even Fibonacci numbers

LIMIT = 4_000_000


function solve()
    a, b = 1, 2
    answer = 0
    while a < LIMIT
        if a % 2 == 0
            answer += a
        end
        a, b = b, a + b
    end
    return answer
end


print(Int(solve()))
