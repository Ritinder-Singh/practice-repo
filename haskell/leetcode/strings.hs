module Strings where
-- TOPIC: String LeetCode Problems | ghci: :load strings.hs
import qualified Data.Map.Strict as Map
import Data.List (sort, group, sortBy)

-- TODO 1: Longest Substring Without Repeating Characters — LC #3
-- lengthOfLongestSubstring :: String -> Int
-- -- Sliding window with Map of char → last index

-- TODO 2: Valid Anagram — LC #242
-- isAnagram :: String -> String -> Bool
-- isAnagram s t = sort s == sort t

-- TODO 3: Group Anagrams — LC #49
-- groupAnagrams :: [String] -> [[String]]
-- -- Map.fromListWith (++) [(sort s, [s]) | s <- strs]

-- TODO 4: Longest Palindromic Substring — LC #5
-- longestPalindrome :: String -> String
-- -- Expand around center; track by length

-- TODO 5: Minimum Window Substring — LC #76
-- minWindow :: String -> String -> String
-- -- Sliding window with frequency maps

-- TODO 6: Encode and Decode Strings — LC #271
-- encode :: [String] -> String
-- encode = concatMap (\s -> show (length s) ++ "#" ++ s)
-- decode :: String -> [String]
-- -- Parse length prefix until end of string

-- TODO 7: Find All Anagrams in a String — LC #438
-- findAnagrams :: String -> String -> [Int]
-- -- Fixed sliding window of size length p
