const std = @import("std");
// TOPIC: Linked Lists — LeetCode | zig run linked_lists.zig
// Zig linked lists use explicit allocators and optional pointers (?*Node).

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();
    try stdout.print("Linked Lists LeetCode — TODO: implement\n", .{});
}

// Node definition (uncomment when implementing):
// const Node = struct {
//     val: i32,
//     next: ?*Node = null,
//     fn create(allocator: std.mem.Allocator, val: i32) !*Node {
//         const n = try allocator.create(Node);
//         n.* = .{ .val = val };
//         return n;
//     }
// };

// TODO 1: Reverse Linked List — LeetCode #206
//   fn reverse(head: ?*Node) ?*Node
//   Three-pointer iterative: prev=null, curr=head, next=curr.next. O(n).

// TODO 2: Merge Two Sorted Lists — LeetCode #21
//   fn mergeSorted(l1: ?*Node, l2: ?*Node, allocator: std.mem.Allocator) !?*Node
//   Dummy head trick; compare and link smaller node each step. O(n+m).

// TODO 3: Linked List Cycle — LeetCode #141
//   fn hasCycle(head: ?*Node) bool
//   Floyd's tortoise and hare: slow += 1, fast += 2. O(n) O(1).

// TODO 4: Find Duplicate Number — LeetCode #287
//   fn findDuplicate(nums: []const i32) i32
//   Treat array as linked list; Floyd's cycle detection. O(n) O(1).

// TODO 5: Remove Nth Node From End — LeetCode #19
//   fn removeNthFromEnd(head: ?*Node, n: usize) ?*Node
//   Two-pointer gap of n; when fast reaches end, slow.next is target. O(L).

// TODO 6: Reorder List — LeetCode #143
//   fn reorderList(head: ?*Node) void
//   Find middle, reverse second half, interleave. O(n) O(1).

// TODO 7: LRU Cache — LeetCode #146
//   Design LRUCache(capacity) with get/put in O(1).
//   Use doubly-linked list + AutoHashMap(i32, *DLLNode).

// TODO 8: Merge K Sorted Lists — LeetCode #23
//   fn mergeKLists(lists: []?*Node, allocator: std.mem.Allocator) !?*Node
//   Divide and conquer: pair-merge repeatedly. O(n log k).
