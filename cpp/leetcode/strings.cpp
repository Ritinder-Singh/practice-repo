#include <iostream>
#include <string>
#include <unordered_map>
#include <algorithm>
// TOPIC: Strings — LeetCode | g++ -std=c++20 -o out strings.cpp && ./out

int main() { std::cout << "Strings LeetCode — TODO: implement\n"; return 0; }

// TODO 1: Valid Anagram — LeetCode #242
//   bool isAnagram(string s, string t)
//   int freq[26] = {}; increment for s, decrement for t; all zero → true. O(n).

// TODO 2: Valid Palindrome — LeetCode #125
//   bool isPalindrome(string s)
//   Two pointers; skip non-alphanumeric; compare tolower. O(n).

// TODO 3: Longest Substring Without Repeating Characters — LeetCode #3
//   int lengthOfLongestSubstring(string s)
//   Sliding window + unordered_map<char,int> for last-seen index. O(n).

// TODO 4: Group Anagrams — LeetCode #49
//   vector<vector<string>> groupAnagrams(vector<string>& strs)
//   Sort each string as key in unordered_map. O(n·k log k).

// TODO 5: Longest Palindromic Substring — LeetCode #5
//   string longestPalindrome(string s)
//   Expand around center for each i (odd) and i,i+1 (even). O(n²).

// TODO 6: Encode and Decode Strings — LintCode #659
//   string encode(vector<string>& strs)   // "4#word4#love"
//   vector<string> decode(string s)
//   Length-prefix encoding avoids delimiter collisions.

// TODO 7: Find All Anagrams in a String — LeetCode #438
//   vector<int> findAnagrams(string s, string p)
//   Fixed-size sliding window; compare freq arrays. O(n).

// TODO 8: Minimum Window Substring — LeetCode #76
//   string minWindow(string s, string t)
//   Sliding window with need/have counters. O(n).
