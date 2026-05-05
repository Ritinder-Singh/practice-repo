module DynamicProgramming where
-- TOPIC: Dynamic Programming LeetCode Problems | ghci: :load dynamic_programming.hs
import Data.Array (Array, array, (!), bounds, listArray)

-- TODO 1: Climbing Stairs — LC #70
-- climbStairs :: Int -> Int
-- climbStairs n = fibs !! n
--   where fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

-- TODO 2: Coin Change — LC #322
-- coinChange :: [Int] -> Int -> Int
-- coinChange coins amount = dp ! amount
--   where dp = array (0, amount) [(i, solve i) | i <- [0..amount]]
--         solve 0 = 0
--         solve i = minimum $ (-1) : [dp ! (i-c) + 1 | c <- coins, c <= i, dp ! (i-c) >= 0]

-- TODO 3: Longest Increasing Subsequence — LC #300
-- lengthOfLIS :: [Int] -> Int
-- -- O(n²): dp[i] = 1 + max (dp[j] | j < i, nums[j] < nums[i])

-- TODO 4: Longest Common Subsequence — LC #1143
-- longestCommonSubsequence :: String -> String -> Int
-- lcs s t = dp ! (m, n)
--   where m = length s; n = length t
--         sa = listArray (1,m) s; ta = listArray (1,n) t
--         dp = array ((0,0),(m,n)) [((i,j), go i j) | i<-[0..m], j<-[0..n]]
--         go 0 _ = 0; go _ 0 = 0
--         go i j = if sa!i == ta!j then dp!(i-1,j-1)+1 else max (dp!(i-1,j)) (dp!(i,j-1))

-- TODO 5: 0/1 Knapsack (classic)
-- knapsack :: [Int] -> [Int] -> Int -> Int
-- -- dp[i][w] = max value with first i items, capacity w

-- TODO 6: Decode Ways — LC #91
-- numDecodings :: String -> Int
-- -- dp[i] = ways to decode s[0..i-1]

-- TODO 7: Word Break — LC #139
-- wordBreak :: String -> [String] -> Bool
-- -- dp[i] = can s[0..i-1] be segmented
