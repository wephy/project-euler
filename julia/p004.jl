# Largest palindrome product

DIGITS = 3


function solve()
    return maximum((string(p) == reverse(string(p))) ? p : 0
                   for p in (x * y for x in 10^(DIGITS - 1):(10^DIGITS - 1)
                   for y in x:(10^DIGITS - 1)))
end


print(Int(solve()))
