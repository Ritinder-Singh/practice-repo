// TOPIC: Dynamic Programming LeetCode Problems | dart dynamic_programming.dart

// TODO 1: Climbing Stairs — LC #70
//   int climbStairs(int n)
//   - dp[i] = dp[i-1] + dp[i-2]; optimize to two int variables

// TODO 2: Coin Change — LC #322
//   int coinChange(List<int> coins, int amount)
//   - dp = List.filled(amount+1, amount+1); dp[0]=0

// TODO 3: Longest Increasing Subsequence — LC #300
//   int lengthOfLIS(List<int> nums)
//   - O(n²) dp[i] = max(dp[j]+1) for j<i where nums[j]<nums[i]
//   - O(n log n) patience sorting with binary search

// TODO 4: Longest Common Subsequence — LC #1143
//   int longestCommonSubsequence(String text1, String text2)
//   - 2D dp table; dp[i][j] = if chars match: dp[i-1][j-1]+1 else max(dp[i-1][j], dp[i][j-1])

// TODO 5: 0/1 Knapsack (classic)
//   int knapsack(List<int> weights, List<int> values, int capacity)
//   - dp[w] = max value with capacity w; iterate backwards to avoid reuse

// TODO 6: Decode Ways — LC #91
//   int numDecodings(String s)
//   - dp[i] = ways to decode s[0..i-1]; check 1-digit and 2-digit

// TODO 7: Word Break — LC #139
//   bool wordBreak(String s, List<String> wordDict)
//   - dp[i] = true if s.substring(0,i) can be segmented using wordDict

void main() {}
