# frozen_string_literal: true
# TOPIC: Dynamic Programming LeetCode Problems | ruby dynamic_programming.rb

# TODO 1: Climbing Stairs — LC #70
#   def climb_stairs(n)
#     # dp[i] = dp[i-1] + dp[i-2]; optimize to two variables a, b
#   end

# TODO 2: Coin Change — LC #322
#   def coin_change(coins, amount)
#     # dp = Array.new(amount+1, Float::INFINITY); dp[0]=0
#     # dp[i] = coins.reduce(dp[i]) { |min, c| i >= c ? [min, dp[i-c]+1].min : min }
#   end

# TODO 3: Longest Increasing Subsequence — LC #300
#   def length_of_lis(nums)
#     # dp[i] = length of LIS ending at i; O(n²) or O(n log n) with binary search
#   end

# TODO 4: Longest Common Subsequence — LC #1143
#   def longest_common_subsequence(text1, text2)
#     # 2D DP table; dp[i][j] = LCS of text1[0..i-1] and text2[0..j-1]
#   end

# TODO 5: 0/1 Knapsack (classic)
#   def knapsack(weights, values, capacity)
#     # dp[i][w] = max value with first i items and capacity w
#   end

# TODO 6: Decode Ways — LC #91
#   def num_decodings(s)
#     # dp[i] = ways to decode s[0..i-1]; check single and double digit
#   end

# TODO 7: Word Break — LC #139
#   def word_break(s, word_dict)
#     # dp[i] = can s[0..i-1] be segmented; dp[0]=true
#   end
