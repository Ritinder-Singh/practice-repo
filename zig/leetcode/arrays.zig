const std = @import("std");
// TOPIC: Arrays & Slices — LeetCode | zig run arrays.zig
// Docs: https://ziglang.org/documentation/master/#Arrays

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();
    try stdout.print("Arrays LeetCode — TODO: implement\n", .{});
}

// TODO 1: Two Sum — LeetCode #1
//   fn twoSum(nums: []const i32, target: i32, allocator: std.mem.Allocator) ![2]usize
//   Use AutoHashMap(i32, usize): map[complement] → index. O(n) time.

// TODO 2: Best Time to Buy and Sell Stock — LeetCode #121
//   fn maxProfit(prices: []const i32) i32
//   Track min price seen so far; update max profit each step. O(n).

// TODO 3: Contains Duplicate — LeetCode #217
//   fn containsDuplicate(nums: []const i32, allocator: std.mem.Allocator) !bool
//   Insert into AutoHashMap; return true if key already exists.

// TODO 4: Product of Array Except Self — LeetCode #238
//   fn productExceptSelf(nums: []const i32, out: []i32) void
//   Two-pass prefix/suffix products — no division, O(n) time O(1) extra.

// TODO 5: Maximum Subarray — LeetCode #53
//   fn maxSubArray(nums: []const i32) i32
//   Kadane's algorithm: track current_sum, reset to 0 when negative.

// TODO 6: Rotate Array — LeetCode #189
//   fn rotate(nums: []i32, k: usize) void
//   Three-reversal trick in place: reverse all, reverse [0,k-1], reverse [k,n-1].

// TODO 7: Merge Intervals — LeetCode #56
//   fn merge(intervals: [][2]i32, allocator: std.mem.Allocator) ![][2]i32
//   Sort by start; iterate and merge overlapping. O(n log n).

// TODO 8: Find Minimum in Rotated Sorted Array — LeetCode #153
//   fn findMin(nums: []const i32) i32
//   Binary search: compare mid with right boundary to decide which half.
