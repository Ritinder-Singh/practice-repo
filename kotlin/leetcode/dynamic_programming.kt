package leetcode
// TOPIC: Dynamic Programming LeetCode Problems | kotlinc dynamic_programming.kt -include-runtime -d out.jar && java -jar out.jar

// TODO 1: Climbing Stairs — LC #70
//   fun climbStairs(n: Int): Int
//   - dp[i] = dp[i-1] + dp[i-2]; optimize to two variables

// TODO 2: Coin Change — LC #322
//   fun coinChange(coins: IntArray, amount: Int): Int
//   - dp[i] = min coins for amount i; Int.MAX_VALUE for unreachable

// TODO 3: Longest Increasing Subsequence — LC #300
//   fun lengthOfLIS(nums: IntArray): Int
//   - O(n log n) with patience sorting using binarySearch

// TODO 4: Longest Common Subsequence — LC #1143
//   fun longestCommonSubsequence(text1: String, text2: String): Int
//   - 2D DP table: dp[i][j] = LCS of text1[0..i] and text2[0..j]

// TODO 5: 0/1 Knapsack (classic)
//   fun knapsack(weights: IntArray, values: IntArray, capacity: Int): Int
//   - dp[i][w] = max value using first i items with capacity w

// TODO 6: Decode Ways — LC #91
//   fun numDecodings(s: String): Int
//   - dp[i] = ways to decode s[0..i-1]

// TODO 7: Word Break — LC #139
//   fun wordBreak(s: String, wordDict: List<String>): Boolean
//   - dp[i] = can s[0..i-1] be segmented

// TODO 8: House Robber — LC #198
//   fun rob(nums: IntArray): Int
//   - dp[i] = max(dp[i-1], dp[i-2] + nums[i])

fun main() {}
