-- Largest palindrome product

products :: [Int]
products = do
    [ x * y | x <- [1..limit], y <- [1..limit]]
    where
        limit = 10^(3 :: Int) - 1

palindromeTest :: Int -> Bool
palindromeTest x = reverse (show x) == show x

palindromes :: [Int]
palindromes = filter palindromeTest products


main :: IO ()
main = do
    print (maximum palindromes)
