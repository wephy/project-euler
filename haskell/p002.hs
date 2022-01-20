-- Even Fibonacci numbers

fib :: Int -> Int -> [Int]
fib a b = a : fib b (a + b)

evenFibonaccis :: [Int]
evenFibonaccis = [x | x <- takeWhile (< 4000000) (fib 1 1), even x]


main :: IO ()
main = do
    print (sum evenFibonaccis)
