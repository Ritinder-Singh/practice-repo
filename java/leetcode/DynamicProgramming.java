package leetcode;
// TOPIC: Dynamic Programming LeetCode Problems | javac DynamicProgramming.java && java leetcode.DynamicProgramming
// Docs: https://leetcode.com/tag/dynamic-programming/

public class DynamicProgramming {

    // TODO 1: Climbing Stairs — LC #70
    //   int climbStairs(int n)
    //   - dp[i] = dp[i-1] + dp[i-2]; optimize to O(1) space with two variables

    // TODO 2: Coin Change — LC #322
    //   int coinChange(int[] coins, int amount)
    //   - dp[i] = min coins to make amount i; dp[0]=0, dp[i]=MIN(dp[i-coin]+1)

    // TODO 3: Longest Increasing Subsequence — LC #300
    //   int lengthOfLIS(int[] nums)
    //   - O(n²) DP: dp[i] = max(dp[j]+1) for j < i where nums[j] < nums[i]
    //   - O(n log n) patience sorting with binary search

    // TODO 4: Longest Common Subsequence — LC #1143
    //   int longestCommonSubsequence(String text1, String text2)
    //   - 2D DP: dp[i][j] = LCS of text1[0..i] and text2[0..j]

    // TODO 5: 0/1 Knapsack (classic)
    //   int knapsack(int[] weights, int[] values, int capacity)
    //   - dp[i][w] = max value using first i items with capacity w

    // TODO 6: Decode Ways — LC #91
    //   int numDecodings(String s)
    //   - dp[i] = ways to decode s[0..i-1]; check single digit and double digit

    // TODO 7: Word Break — LC #139
    //   boolean wordBreak(String s, List<String> wordDict)
    //   - dp[i] = true if s[0..i-1] can be segmented; check dp[j] && dict contains s[j..i]

    // TODO 8: House Robber — LC #198
    //   int rob(int[] nums)
    //   - dp[i] = max(dp[i-1], dp[i-2] + nums[i]); can't rob adjacent houses

    public static void main(String[] args) {}
}
