# Special Pythagorean triplet

TRIPLET_SUM = 1000


function solve()
    for b in floor(Int, TRIPLET_SUM / (2 + 2^0.5)):(TRIPLET_SUM // 2)
        for a in 1:(b - 1)
            c = (a^2 + b^2)^0.5
            if a + b + c == TRIPLET_SUM
                return a * b * c
            end
        end
    end
end


print(Int(solve()))
