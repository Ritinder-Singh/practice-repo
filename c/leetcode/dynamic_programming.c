#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// TOPIC: Dynamic Programming — LeetCode | gcc -o out dynamic_programming.c && ./out

int main(void) { printf("Dynamic Programming LeetCode — TODO: implement\n"); return 0; }

// TODO 1: Climbing Stairs — LeetCode #70
//   int climbStairs(int n)
//   dp[i] = dp[i-1] + dp[i-2]; two variables suffice. O(n) O(1).

// TODO 2: House Robber — LeetCode #198
//   int rob(int *nums, int n)
//   dp[i] = max(dp[i-1], nums[i] + dp[i-2]). Rolling two vars. O(n) O(1).

// TODO 3: Coin Change — LeetCode #322
//   int coinChange(int *coins, int coinsSize, int amount)
//   dp[0]=0; dp[i] = min over coins of dp[i-coin]+1. Initialize to amount+1. O(n*amount).

// TODO 4: Longest Increasing Subsequence — LeetCode #300
//   int lengthOfLIS(int *nums, int n)
//   Patience sorting with binary search (tails array). O(n log n).

// TODO 5: 0-1 Knapsack
//   int knapsack(int *weights, int *values, int n, int W)
//   2D array dp[n+1][W+1]; or 1D rolling array for O(n*W) O(W) space.

// TODO 6: Word Break — LeetCode #139
//   bool wordBreak(char *s, char **wordDict, int wordDictSize)
//   bool dp[n+1]; dp[0]=true; dp[i]=true if dp[j] && s[j..i] in dict. O(n²*m).

// TODO 7: Unique Paths — LeetCode #62
//   int uniquePaths(int m, int n)
//   dp[j] += dp[j-1] with single 1D array (space-optimized). O(m*n) O(n).

// TODO 8: Edit Distance — LeetCode #72
//   int minDistance(char *word1, char *word2)
//   Classic Levenshtein DP table; can optimize to O(min(m,n)) space. O(m*n).
