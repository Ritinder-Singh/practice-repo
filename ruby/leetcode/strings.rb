# frozen_string_literal: true
# TOPIC: String LeetCode Problems | ruby strings.rb

# TODO 1: Longest Substring Without Repeating Characters — LC #3
#   def length_of_longest_substring(s)
#     # Sliding window + hash map of char → last index; update left = max(left, map[c]+1)
#   end

# TODO 2: Valid Anagram — LC #242
#   def is_anagram(s, t)
#     # Count char frequencies; Hash.new(0); s each +1, t each -1; all values == 0
#   end

# TODO 3: Group Anagrams — LC #49
#   def group_anagrams(strs)
#     # Key = sorted chars; group_by { |s| s.chars.sort.join }
#   end

# TODO 4: Longest Palindromic Substring — LC #5
#   def longest_palindrome(s)
#     # Expand around center for each index (odd) and each pair (even)
#   end

# TODO 5: Minimum Window Substring — LC #76
#   def min_window(s, t)
#     # Sliding window; need hash, have hash; shrink left when all needed chars are in window
#   end

# TODO 6: Encode and Decode Strings — LC #271
#   def encode(strs)
#     # Format: "#{str.length}##{str}" joined — length prefix handles any character
#   end
#   def decode(s)
#     # Parse length prefix, extract str, advance pointer
#   end

# TODO 7: Find All Anagrams in a String — LC #438
#   def find_anagrams(s, p)
#     # Fixed-size sliding window; compare freq arrays; O(n) with running counts
#   end
