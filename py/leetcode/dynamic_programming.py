# =============================================================================
# Python LeetCode — Dynamic Programming  (Blind 75 / NeetCode 150)
# =============================================================================
from typing import List

# LC #70  Climbing Stairs — Fibonacci O(n) / O(1)
# def climb_stairs(n: int) -> int: pass

# LC #198 House Robber — dp[i] = max(dp[i-1], dp[i-2]+nums[i])
# def rob(nums: List[int]) -> int: pass

# LC #213 House Robber II — run rob() on nums[:-1] and nums[1:]
# def rob_ii(nums: List[int]) -> int: pass

# LC #322 Coin Change — bottom-up O(amount * coins)
# def coin_change(coins: List[int], amount: int) -> int: pass

# LC #518 Coin Change II — count combinations
# def change(amount: int, coins: List[int]) -> int: pass

# LC #300 Longest Increasing Subsequence — O(n²) dp / O(n log n) patience sort
# def length_of_lis(nums: List[int]) -> int: pass

# LC #1143 Longest Common Subsequence — 2D dp O(m*n)
# def longest_common_subsequence(text1: str, text2: str) -> int: pass

# LC #139 Word Break — dp[i] = any(dp[j] and s[j:i] in wordSet)
# def word_break(s: str, word_dict: List[str]) -> bool: pass

# LC #62  Unique Paths — dp[i][j] = dp[i-1][j] + dp[i][j-1]
# def unique_paths(m: int, n: int) -> int: pass

# LC #72  Edit Distance — 2D dp insert/delete/replace
# def min_distance(word1: str, word2: str) -> int: pass

# LC #312 Burst Balloons — interval dp O(n³)
# def max_coins(nums: List[int]) -> int: pass
