// TOPIC: String Problems (LeetCode) | swift strings.swift
// Run: swift strings.swift

// TODO 1: LC #3 — Longest Substring Without Repeating Characters
// Sliding window with a Set to track characters in the current window.
// func lengthOfLongestSubstring(_ s: String) -> Int

// TODO 2: LC #242 — Valid Anagram
// Sort both strings and compare, or use a frequency dictionary.
// func isAnagram(_ s: String, _ t: String) -> Bool

// TODO 3: LC #49 — Group Anagrams
// Group strings that are anagrams of each other; use sorted string as key.
// func groupAnagrams(_ strs: [String]) -> [[String]]

// TODO 4: LC #5 — Longest Palindromic Substring
// Expand around center for each character and each pair; track the longest found.
// func longestPalindrome(_ s: String) -> String

// TODO 5: LC #76 — Minimum Window Substring
// Sliding window with two frequency maps; shrink left when all chars covered.
// func minWindow(_ s: String, _ t: String) -> String

// TODO 6: LC #271 — Encode and Decode Strings
// Encode array of strings to single string; decode back (use length-prefix scheme).
// func encode(_ strs: [String]) -> String
// func decode(_ s: String) -> [String]

// TODO 7: LC #438 — Find All Anagrams in a String
// Sliding window of length p; compare frequency maps at each position.
// func findAnagrams(_ s: String, _ p: String) -> [Int]
