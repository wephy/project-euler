-- Multiples of 3 and 5

multiples :: [Int]
multiples = [x | x <- [1..999], (x `mod` 3 == 0) || (x `mod` 5 == 0)]


main :: IO ()
main = do
    print (sum multiples)
