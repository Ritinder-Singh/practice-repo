#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
// TOPIC: Strings — LeetCode | gcc -o out strings.c && ./out

int main(void) { printf("Strings LeetCode — TODO: implement\n"); return 0; }

// TODO 1: Valid Anagram — LeetCode #242
//   bool isAnagram(char *s, char *t)
//   Count [26] int freq; increment for s, decrement for t; all zero → true. O(n).

// TODO 2: Valid Palindrome — LeetCode #125
//   bool isPalindrome(char *s)
//   Two pointers; skip non-alphanumeric with isalnum(); compare tolower(). O(n).

// TODO 3: Longest Substring Without Repeating Characters — LeetCode #3
//   int lengthOfLongestSubstring(char *s)
//   Sliding window + int last[128] = {-1}; shrink left when duplicate found. O(n).

// TODO 4: Longest Palindromic Substring — LeetCode #5
//   char *longestPalindrome(char *s)  (caller does NOT free — return ptr into s)
//   Expand-around-center; return best start pointer + store length. O(n²).

// TODO 5: Implement strstr (needle in haystack) — LeetCode #28
//   int strStr(char *haystack, char *needle)
//   KMP: build failure function for needle; single pass over haystack. O(n+m).

// TODO 6: Reverse Words in a String — LeetCode #151
//   char *reverseWords(char *s)
//   Reverse whole string; then reverse each word; trim spaces. O(n).

// TODO 7: String to Integer (atoi) — LeetCode #8
//   int myAtoi(char *s)
//   Skip whitespace, read sign, accumulate digits, clamp to INT_MIN/INT_MAX. O(n).

// TODO 8: Minimum Window Substring — LeetCode #76
//   char *minWindow(char *s, char *t)
//   Sliding window with need[128] / have counters; track best [start, len]. O(n).
