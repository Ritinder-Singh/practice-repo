module Arrays where
-- TOPIC: Array LeetCode Problems | ghci: :load arrays.hs
import qualified Data.Map.Strict as Map

-- TODO 1: Two Sum — LC #1
-- twoSum :: [Int] -> Int -> Maybe (Int, Int)
-- twoSum nums target = go Map.empty (zip [0..] nums)
--   where go _ [] = Nothing
--         go seen ((i,x):xs) = case Map.lookup (target - x) seen of
--           Just j  -> Just (j, i)
--           Nothing -> go (Map.insert x i seen) xs

-- TODO 2: Best Time to Buy and Sell Stock — LC #121
-- maxProfit :: [Int] -> Int
-- maxProfit [] = 0
-- maxProfit (p:ps) = snd $ foldl (\(minP, maxPr) price -> (min minP price, max maxPr (price - minP))) (p, 0) ps

-- TODO 3: Container With Most Water — LC #11
-- maxArea :: [Int] -> Int
-- maxArea heights = go 0 (length heights - 1) 0
--   where arr = listArray (0, length heights - 1) heights
--         go left right best
--           | left >= right = best
--           | arr ! left <= arr ! right = go (left+1) right (max best $ arr ! left * (right - left))
--           | otherwise = go left (right-1) (max best $ arr ! right * (right - left))

-- TODO 4: Product of Array Except Self — LC #238
-- productExceptSelf :: [Int] -> [Int]
-- -- Pass 1: prefix products; Pass 2: multiply by suffix products

-- TODO 5: Maximum Subarray (Kadane's) — LC #53
-- maxSubArray :: [Int] -> Int
-- maxSubArray (x:xs) = snd $ foldl (\(curr, best) n ->
--   let c = max n (curr + n) in (c, max best c)) (x, x) xs

-- TODO 6: Merge Intervals — LC #56
-- merge :: [[Int]] -> [[Int]]
-- -- Sort by start, merge overlapping intervals

-- TODO 7: Find Minimum in Rotated Sorted Array — LC #153
-- findMin :: [Int] -> Int
-- -- Binary search on array
