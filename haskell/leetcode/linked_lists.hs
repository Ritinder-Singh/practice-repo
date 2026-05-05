module LinkedLists where
-- TOPIC: Linked List LeetCode Problems | ghci: :load linked_lists.hs

-- Using regular Haskell lists as linked lists
-- For mutable linked lists, use IORef-based nodes

-- data ListNode a = Empty | Node a (ListNode a) deriving (Show)

-- TODO 1: Reverse Linked List — LC #206
-- reverseList :: [a] -> [a]
-- reverseList = foldl (flip (:)) []

-- TODO 2: Merge Two Sorted Lists — LC #21
-- mergeTwoLists :: Ord a => [a] -> [a] -> [a]
-- mergeTwoLists [] ys = ys
-- mergeTwoLists xs [] = xs
-- mergeTwoLists (x:xs) (y:ys)
--   | x <= y    = x : mergeTwoLists xs (y:ys)
--   | otherwise = y : mergeTwoLists (x:xs) ys

-- TODO 3: Linked List Cycle — LC #141
-- hasCycle :: Eq a => [a] -> Bool
-- -- Haskell lists are finite; in a mutable context use Floyd's with IORef nodes

-- TODO 4: Remove Nth Node From End — LC #19
-- removeNthFromEnd :: [a] -> Int -> [a]
-- -- Two-pass: length then drop; or one-pass with two pointers

-- TODO 5: Merge K Sorted Lists — LC #23
-- mergeKLists :: Ord a => [[a]] -> [a]
-- mergeKLists = foldr mergeTwoLists []  -- fold merge; use heap for O(n log k)

-- TODO 6: Reorder List — LC #143
-- reorderList :: [a] -> [a]
-- reorderList xs = interleave front (reverse back)
--   where mid = length xs `div` 2
--         (front, back) = splitAt mid xs
--         interleave [] ys = ys
--         interleave xs [] = xs
--         interleave (x:xs) (y:ys) = x : y : interleave xs ys
