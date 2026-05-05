#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>
// TOPIC: Dynamic Programming — LeetCode | g++ -std=c++20 -o out dynamic_programming.cpp && ./out

int main() { std::cout << "Dynamic Programming LeetCode — TODO: implement\n"; return 0; }

// TODO 1: Climbing Stairs — LeetCode #70
//   int climbStairs(int n)  — two rolling vars. O(n) O(1).

// TODO 2: House Robber — LeetCode #198
//   int rob(vector<int>& nums)  — dp = max(prev, curr + prev_prev). O(n) O(1).

// TODO 3: Coin Change — LeetCode #322
//   int coinChange(vector<int>& coins, int amount)
//   dp[i] = min over coins of dp[i-coin]+1. O(n*amount).

// TODO 4: Longest Increasing Subsequence — LeetCode #300
//   int lengthOfLIS(vector<int>& nums)
//   Patience sort + lower_bound. O(n log n).

// TODO 5: Word Break — LeetCode #139
//   bool wordBreak(string s, vector<string>& wordDict)
//   dp[i] = any dp[j] where s[j..i] in dict (unordered_set). O(n²).

// TODO 6: Longest Common Subsequence — LeetCode #1143
//   int longestCommonSubsequence(string t1, string t2)
//   2D DP: dp[i][j] = match ? dp[i-1][j-1]+1 : max(dp[i-1][j], dp[i][j-1]). O(m*n).

// TODO 7: Partition Equal Subset Sum — LeetCode #416
//   bool canPartition(vector<int>& nums)
//   0-1 knapsack: target = sum/2; dp[w] |= dp[w-num]. O(n * sum/2).

// TODO 8: Edit Distance — LeetCode #72
//   int minDistance(string word1, string word2)
//   Levenshtein DP; optimize to O(min(m,n)) space. O(m*n).
