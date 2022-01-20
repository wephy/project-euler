-- Largest prime factor

factor :: Int -> Int -> Int
factor n i
    | n <= 1    = i
    | otherwise = factor (n `div` d) d where
        d = head [x | x <- [i..n], n `mod` x == 0]

largestPrimeFactor :: Int -> Int
largestPrimeFactor n = factor n 2


main :: IO ()
main = do
    print (largestPrimeFactor 600851475143)
