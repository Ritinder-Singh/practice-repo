// TOPIC: String LeetCode Problems | dart strings.dart

// TODO 1: Longest Substring Without Repeating Characters — LC #3
//   int lengthOfLongestSubstring(String s)
//   - Sliding window + Map<String, int> of char → last index

// TODO 2: Valid Anagram — LC #242
//   bool isAnagram(String s, String t)
//   - Count char frequencies; Map<String,int>; all values 0 at end

// TODO 3: Group Anagrams — LC #49
//   List<List<String>> groupAnagrams(List<String> strs)
//   - Key = sorted chars; Map<String, List<String>>

// TODO 4: Longest Palindromic Substring — LC #5
//   String longestPalindrome(String s)
//   - Expand around center for each index (odd and even length)

// TODO 5: Minimum Window Substring — LC #76
//   String minWindow(String s, String t)
//   - Sliding window; need map, have map; shrink left when all chars present

// TODO 6: Encode and Decode Strings — LC #271
//   String encode(List<String> strs)  — "4#word3#foo" format
//   List<String> decode(String s)     — parse length prefix

// TODO 7: Find All Anagrams in a String — LC #438
//   List<int> findAnagrams(String s, String p)
//   - Fixed sliding window size p.length; compare freq maps

void main() {}
