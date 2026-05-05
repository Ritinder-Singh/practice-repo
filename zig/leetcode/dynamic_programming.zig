const std = @import("std");
// TOPIC: Dynamic Programming — LeetCode | zig run dynamic_programming.zig

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();
    try stdout.print("Dynamic Programming LeetCode — TODO: implement\n", .{});
}

// TODO 1: Climbing Stairs — LeetCode #70
//   fn climbStairs(n: u32) u32
//   dp[i] = dp[i-1] + dp[i-2]; use only two variables. O(n) O(1).

// TODO 2: House Robber — LeetCode #198
//   fn rob(nums: []const i32) i32
//   dp[i] = max(dp[i-1], nums[i] + dp[i-2]). Rolling two vars. O(n) O(1).

// TODO 3: Coin Change — LeetCode #322
//   fn coinChange(coins: []const i32, amount: i32) i32
//   Bottom-up: dp[0]=0, dp[i] = min over coins of dp[i-coin]+1. O(n*amount).

// TODO 4: Longest Increasing Subsequence — LeetCode #300
//   fn lengthOfLIS(nums: []const i32) i32
//   Patience sorting with binary search: maintain tails array. O(n log n).

// TODO 5: 0-1 Knapsack
//   fn knapsack(weights: []const u32, values: []const u32, capacity: u32) u32
//   2D DP table dp[i][w] = max value using first i items with capacity w. O(n*W).

// TODO 6: Word Break — LeetCode #139
//   fn wordBreak(s: []const u8, wordDict: [][]const u8, allocator: std.mem.Allocator) !bool
//   dp[i] = true if s[0..i] can be segmented. Check each word ending at i. O(n²*m).

// TODO 7: Unique Paths — LeetCode #62
//   fn uniquePaths(m: u32, n: u32) u32
//   dp[i][j] = dp[i-1][j] + dp[i][j-1]; top row and left col = 1. O(m*n).

// TODO 8: Edit Distance — LeetCode #72
//   fn minDistance(word1: []const u8, word2: []const u8, allocator: std.mem.Allocator) !u32
//   Classic Levenshtein DP table. O(m*n) time and space.
