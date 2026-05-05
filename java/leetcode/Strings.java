package leetcode;
// TOPIC: String LeetCode Problems | javac Strings.java && java leetcode.Strings
import java.util.*;

public class Strings {

    // TODO 1: Longest Substring Without Repeating Characters — LC #3 — sliding window
    //   int lengthOfLongestSubstring(String s)
    //   - Use HashMap<Character, Integer> to store char → latest index seen
    //   - Left pointer moves right when duplicate found: left = max(left, map.get(c) + 1)
    //   - Window size at each step: right - left + 1; track global max
    //   - Example: "abcabcbb" → 3 ("abc"),  "bbbbb" → 1,  "pwwkew" → 3 ("wke")

    // TODO 2: Valid Anagram — LC #242 — frequency count
    //   boolean isAnagram(String s, String t)
    //   - If lengths differ, return false immediately
    //   - Count character frequencies: int[26] for lowercase letters only
    //   - Increment for each char in s; decrement for each char in t
    //   - Return true if all counts are 0
    //   - Follow-up: handle Unicode using HashMap<Character, Integer>
    //   - Example: s="anagram", t="nagaram" → true;  s="rat", t="car" → false

    // TODO 3: Group Anagrams — LC #49 — sorted string as key
    //   List<List<String>> groupAnagrams(String[] strs)
    //   - Map<String, List<String>> map = new HashMap<>();
    //   - Key: sort each string's characters → Arrays.sort(chars); new String(chars)
    //   - Alternative key: int[26] frequency array converted to string "1#0#2#..."
    //   - Return new ArrayList<>(map.values())
    //   - Example: ["eat","tea","tan","ate","nat","bat"] → [["bat"],["nat","tan"],["ate","eat","tea"]]

    // TODO 4: Longest Palindromic Substring — LC #5 — expand around center
    //   String longestPalindrome(String s)
    //   - For each index i, expand outward for two cases:
    //     a) Odd length:  expand(s, i, i)     — single char center
    //     b) Even length: expand(s, i, i+1)   — two char center
    //   - Helper: String expand(String s, int left, int right) — while chars match, expand; return substring
    //   - Track longest result across all centers
    //   - Alternative: Manacher's algorithm O(n), but expand-around-center is O(n^2) and sufficient
    //   - Example: "babad" → "bab" or "aba";  "cbbd" → "bb"

    // TODO 5: Minimum Window Substring — LC #76 — sliding window with two maps
    //   String minWindow(String s, String t)
    //   - Count chars needed: Map<Character, Integer> need (freq of each char in t)
    //   - Expand right pointer, add char to window map, track 'formed' count (chars satisfying need)
    //   - When formed == need.size(): try to shrink left pointer while window is still valid
    //   - Track minimum window: int[] result = {-1, 0, 0}  // length, left, right
    //   - Example: s="ADOBECODEBANC", t="ABC" → "BANC"

    // TODO 6: Encode and Decode Strings — LC #271 (LeetCode Premium) — length-prefix encoding
    //   String encode(List<String> strs)
    //   String decode(String s) → List<String>
    //   - Encode: for each string, prepend its length and a delimiter: "4#word5#hello"
    //   - Decode: read length up to '#', parse int, read that many chars as next string, repeat
    //   - Handles strings with any characters including '#' and special chars
    //   - Alternative: use non-ASCII delimiter like '\0' or escape approach

    // TODO 7: Find All Anagrams in a String — LC #438 — fixed-size sliding window
    //   List<Integer> findAnagrams(String s, String p)
    //   - Count frequencies in p: int[26] pCount
    //   - Sliding window of size p.length() over s: int[26] sCount
    //   - Add rightmost char; remove leftmost char as window slides
    //   - If Arrays.equals(sCount, pCount): add left index to result list
    //   - Example: s="cbaebabacd", p="abc" → [0,6];  s="abab", p="ab" → [0,1,2]

    public static void main(String[] args) {
        // TODO: instantiate the class and call each method with test cases
        // Print expected vs actual output for each problem
    }
}
