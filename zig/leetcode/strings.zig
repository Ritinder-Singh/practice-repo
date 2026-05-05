const std = @import("std");
// TOPIC: Strings & Slices — LeetCode | zig run strings.zig
// Zig strings are []const u8 (UTF-8 byte slices). Use std.mem for operations.

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();
    try stdout.print("Strings LeetCode — TODO: implement\n", .{});
}

// TODO 1: Valid Anagram — LeetCode #242
//   fn isAnagram(s: []const u8, t: []const u8) bool
//   Count char frequencies in a [26]i32; compare arrays. O(n).

// TODO 2: Valid Palindrome — LeetCode #125
//   fn isPalindrome(s: []const u8) bool
//   Two-pointer, skip non-alphanumeric, compare std.ascii.toLower.

// TODO 3: Longest Substring Without Repeating Characters — LeetCode #3
//   fn lengthOfLongestSubstring(s: []const u8, allocator: std.mem.Allocator) !usize
//   Sliding window + AutoHashMap(u8, usize) for last-seen index. O(n).

// TODO 4: Group Anagrams — LeetCode #49
//   fn groupAnagrams(strs: [][]const u8, allocator: std.mem.Allocator) ![][]const []const u8
//   Sort each string as key into StringHashMap(ArrayList). O(n·k log k).

// TODO 5: Longest Palindromic Substring — LeetCode #5
//   fn longestPalindrome(s: []const u8) []const u8
//   Expand-around-center: try each i (odd) and i,i+1 (even) as center. O(n²).

// TODO 6: String to Integer (atoi) — LeetCode #8
//   fn myAtoi(s: []const u8) i32
//   Handle leading whitespace, sign, digit accumulation, and i32 overflow.

// TODO 7: Count and Say — LeetCode #38
//   fn countAndSay(n: u32, allocator: std.mem.Allocator) ![]u8
//   Iteratively build next sequence by run-length encoding previous. O(n·|seq|).

// TODO 8: Minimum Window Substring — LeetCode #76
//   fn minWindow(s: []const u8, t: []const u8, allocator: std.mem.Allocator) ![]const u8
//   Sliding window with need/have counters and frequency maps. O(n).
