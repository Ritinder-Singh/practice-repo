package leetcode
// TOPIC: String Problems | kotlinc strings.kt -include-runtime -d out.jar && java -jar out.jar
// Docs: https://kotlinlang.org/docs/strings.html

fun main() {
    // TODO 1: LC #3 — Longest Substring Without Repeating Characters
    //   - Input: s = "abcabcbb" → Output: 3 ("abc")
    //   - Strategy: sliding window with HashMap<Char, Int> tracking last seen index
    //   - fun lengthOfLongestSubstring(s: String): Int
    //   - Move left pointer to max(left, lastSeen[c] + 1) on repeat; O(n) time

    // TODO 2: LC #242 — Valid Anagram
    //   - Input: s = "anagram", t = "nagaram" → Output: true
    //   - Strategy A: sort both strings, compare — O(n log n)
    //   - Strategy B: IntArray(26) freq count, increment for s, decrement for t — O(n)
    //   - fun isAnagram(s: String, t: String): Boolean
    //   - Handle Unicode: use HashMap<Char, Int> instead of fixed-size array

    // TODO 3: LC #49 — Group Anagrams
    //   - Input: strs = ["eat","tea","tan","ate","nat","bat"] → Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    //   - Strategy A: group by sorted string key — HashMap<String, MutableList<String>>
    //   - Strategy B: group by char frequency array as key (avoids sort)
    //   - fun groupAnagrams(strs: Array<String>): List<List<String>>
    //   - O(n * k log k) for sort strategy, O(n * k) for frequency strategy

    // TODO 4: LC #5 — Longest Palindromic Substring
    //   - Input: s = "babad" → Output: "bab" (or "aba")
    //   - Strategy: expand-around-center — for each center (odd + even), expand while palindrome
    //   - fun longestPalindrome(s: String): String
    //   - O(n^2) time, O(1) space — Manacher's algorithm is O(n) but complex
    //   - Track start index and max length, extract substring at end

    // TODO 5: LC #76 — Minimum Window Substring
    //   - Input: s = "ADOBECODEBANC", t = "ABC" → Output: "BANC"
    //   - Strategy: sliding window with two frequency maps (need, window)
    //   - fun minWindow(s: String, t: String): String
    //   - Expand right until valid window, then shrink left while still valid
    //   - Track formed count vs required count; O(|s| + |t|) time

    // TODO 6: LC #271 — Encode and Decode Strings
    //   - Design encode/decode for list of strings (network transmission)
    //   - Strategy: length-prefix encoding — "{len}#{str}" for each string
    //   - fun encode(strs: List<String>): String
    //   - fun decode(s: String): List<String>
    //   - Handle edge cases: empty strings, strings containing '#'

    // TODO 7: LC #438 — Find All Anagrams in a String
    //   - Input: s = "cbaebabacd", p = "abc" → Output: [0, 6]
    //   - Strategy: sliding window of size p.length, compare frequency arrays
    //   - fun findAnagrams(s: String, p: String): List<Int>
    //   - Use IntArray(26) for both window and pattern; slide window, update counts
    //   - O(n) time — add right char, remove left char, compare arrays each step
}
