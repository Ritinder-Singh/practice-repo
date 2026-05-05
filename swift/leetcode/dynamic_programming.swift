// TOPIC: Dynamic Programming Problems (LeetCode) | swift dynamic_programming.swift
// Run: swift dynamic_programming.swift

// TODO 1: LC #70 — Climbing Stairs
// dp[i] = dp[i-1] + dp[i-2]; base cases dp[1]=1, dp[2]=2.
// func climbStairs(_ n: Int) -> Int

// TODO 2: LC #322 — Coin Change
// dp[amount] = min coins needed; for each coin, dp[i] = min(dp[i], dp[i-coin]+1).
// func coinChange(_ coins: [Int], _ amount: Int) -> Int

// TODO 3: LC #300 — Longest Increasing Subsequence
// dp[i] = longest LIS ending at index i; use patience sorting for O(n log n).
// func lengthOfLIS(_ nums: [Int]) -> Int

// TODO 4: LC #1143 — Longest Common Subsequence
// 2D DP table; dp[i][j] = LCS of text1[0..<i] and text2[0..<j].
// func longestCommonSubsequence(_ text1: String, _ text2: String) -> Int

// TODO 5: 0-1 Knapsack (Classic)
// dp[i][w] = max value using first i items with capacity w; include or exclude each item.
// func knapsack(_ weights: [Int], _ values: [Int], _ capacity: Int) -> Int

// TODO 6: LC #91 — Decode Ways
// dp[i] = number of ways to decode s[0..<i]; check single and two-digit decodings.
// func numDecodings(_ s: String) -> Int

// TODO 7: LC #139 — Word Break
// dp[i] = true if s[0..<i] can be segmented; for each i check all words in wordDict.
// func wordBreak(_ s: String, _ wordDict: [String]) -> Bool
