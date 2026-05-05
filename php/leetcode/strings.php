<?php
declare(strict_types=1);
// TOPIC: String LeetCode Problems | php strings.php

// TODO 1: Longest Substring Without Repeating Characters — LC #3
//   function lengthOfLongestSubstring(string $s): int
//   // Sliding window + hash map of char → last index

// TODO 2: Valid Anagram — LC #242
//   function isAnagram(string $s, string $t): bool
//   // count_chars($s, 1) and count_chars($t, 1) must match

// TODO 3: Group Anagrams — LC #49
//   function groupAnagrams(array $strs): array
//   // Key = sorted chars (str_split + sort + implode)

// TODO 4: Longest Palindromic Substring — LC #5
//   function longestPalindrome(string $s): string
//   // Expand around center; track longest

// TODO 5: Minimum Window Substring — LC #76
//   function minWindow(string $s, string $t): string
//   // Sliding window; $need and $have char counts

// TODO 6: Encode and Decode Strings — LC #271
//   function encode(array $strs): string   // "4#word3#foo"
//   function decode(string $s): array      // parse length prefix

// TODO 7: Find All Anagrams in a String — LC #438
//   function findAnagrams(string $s, string $p): array
//   // Fixed sliding window; compare freq arrays
