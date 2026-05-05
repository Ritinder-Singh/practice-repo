# =============================================================================
# DSA Foundations — Dynamic Programming
# =============================================================================
# Topics: memoization (top-down), tabulation (bottom-up), 1D DP, 2D DP,
#         knapsack variants, LCS, LIS, coin change, edit distance.
# Run: python dynamic_programming.py
# Ref: NeetCode 150 — 1D DP, 2D DP sections
# =============================================================================

from functools import lru_cache
from typing import List

# =============================================================================
# 1D DYNAMIC PROGRAMMING
# =============================================================================

# -----------------------------------------------------------------------------
# TODO 1: Climbing Stairs — LeetCode #70
# -----------------------------------------------------------------------------
# Count distinct ways to climb n stairs (1 or 2 steps at a time).
# It's Fibonacci! dp[i] = dp[i-1] + dp[i-2].
# Implement: recursive + memo, bottom-up tabulation, space-optimized O(1).
#
# def climb_stairs(n: int) -> int:
#     pass

# -----------------------------------------------------------------------------
# TODO 2: House Robber — LeetCode #198 (Blind 75)
# -----------------------------------------------------------------------------
# Rob houses; cannot rob adjacent. Maximize amount.
# dp[i] = max(dp[i-1], dp[i-2] + nums[i]). Space-optimize to two variables.
#
# def rob(nums: List[int]) -> int:
#     pass

# -----------------------------------------------------------------------------
# TODO 3: House Robber II — LeetCode #213 (Blind 75)
# -----------------------------------------------------------------------------
# Same as above but houses are in a circle (first and last are adjacent).
# Run rob() twice: once on nums[:-1], once on nums[1:]. Take the max.
#
# def rob_ii(nums: List[int]) -> int:
#     pass

# -----------------------------------------------------------------------------
# TODO 4: Coin Change — LeetCode #322 (Blind 75)
# -----------------------------------------------------------------------------
# Find minimum number of coins to make amount. Return -1 if impossible.
# Bottom-up: dp[i] = min coins to make amount i.
# dp[i] = min(dp[i - c] + 1 for c in coins if i >= c)
#
# def coin_change(coins: List[int], amount: int) -> int:
#     pass

# -----------------------------------------------------------------------------
# TODO 5: Coin Change II — LeetCode #518
# -----------------------------------------------------------------------------
# Count number of combinations (not permutations) to make amount.
# dp[i] += dp[i - coin] for each coin. Outer loop: coins, inner: amounts.
#
# def change(amount: int, coins: List[int]) -> int:
#     pass

# -----------------------------------------------------------------------------
# TODO 6: Longest Increasing Subsequence — LeetCode #300 (Blind 75)
# -----------------------------------------------------------------------------
# Find length of longest strictly increasing subsequence.
# O(n²) DP: dp[i] = max(dp[j]+1 for j<i if nums[j]<nums[i]).
# O(n log n) with patience sorting (binary search on tails array).
#
# def length_of_lis(nums: List[int]) -> int:
#     pass

# -----------------------------------------------------------------------------
# TODO 7: Word Break — LeetCode #139 (Blind 75)
# -----------------------------------------------------------------------------
# Can s be segmented into words from wordDict?
# dp[i] = True if s[:i] can be segmented.
# dp[i] = any(dp[j] and s[j:i] in word_set for j in range(i))
#
# def word_break(s: str, word_dict: List[str]) -> bool:
#     pass

# =============================================================================
# 2D DYNAMIC PROGRAMMING
# =============================================================================

# -----------------------------------------------------------------------------
# TODO 8: Unique Paths — LeetCode #62 (Blind 75)
# -----------------------------------------------------------------------------
# Count paths from top-left to bottom-right of m x n grid (only right/down moves).
# dp[i][j] = dp[i-1][j] + dp[i][j-1]. Space-optimize with 1D array.
#
# def unique_paths(m: int, n: int) -> int:
#     pass

# -----------------------------------------------------------------------------
# TODO 9: Longest Common Subsequence — LeetCode #1143 (Blind 75)
# -----------------------------------------------------------------------------
# Find length of LCS of text1 and text2.
# dp[i][j] = dp[i-1][j-1]+1 if chars match, else max(dp[i-1][j], dp[i][j-1]).
#
# def longest_common_subsequence(text1: str, text2: str) -> int:
#     pass

# -----------------------------------------------------------------------------
# TODO 10: Edit Distance — LeetCode #72 (Blind 75)
# -----------------------------------------------------------------------------
# Minimum operations (insert, delete, replace) to convert word1 to word2.
# dp[i][j] = min edits to convert word1[:i] to word2[:j].
#
# def min_distance(word1: str, word2: str) -> int:
#     pass

# -----------------------------------------------------------------------------
# TODO 11: 0/1 Knapsack
# -----------------------------------------------------------------------------
# Given weights and values arrays and capacity W, maximize total value
# without exceeding weight limit. Each item used at most once.
# dp[i][w] = max value using first i items with capacity w.
#
# def knapsack(weights: List[int], values: List[int], W: int) -> int:
#     pass

# -----------------------------------------------------------------------------
# TODO 12: Burst Balloons — LeetCode #312 (Hard)
# -----------------------------------------------------------------------------
# Burst balloons to maximize coins. dp[i][j] = max coins from subarray (i..j).
# Try each balloon as the LAST to burst in the range.
#
# def max_coins(nums: List[int]) -> int:
#     pass
