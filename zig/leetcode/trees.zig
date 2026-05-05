const std = @import("std");
// TOPIC: Trees — LeetCode | zig run trees.zig

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();
    try stdout.print("Trees LeetCode — TODO: implement\n", .{});
}

// TreeNode definition:
// const TreeNode = struct {
//     val: i32,
//     left:  ?*TreeNode = null,
//     right: ?*TreeNode = null,
// };

// TODO 1: Maximum Depth of Binary Tree — LeetCode #104
//   fn maxDepth(root: ?*TreeNode) i32
//   Recursive: 1 + max(left, right). Base case: null → 0. O(n).

// TODO 2: Invert Binary Tree — LeetCode #226
//   fn invertTree(root: ?*TreeNode) ?*TreeNode
//   Swap left/right, recurse both subtrees. O(n).

// TODO 3: Same Tree — LeetCode #100
//   fn isSameTree(p: ?*TreeNode, q: ?*TreeNode) bool
//   Both null → true; one null → false; compare val, recurse. O(n).

// TODO 4: Validate BST — LeetCode #98
//   fn isValidBST(root: ?*TreeNode) bool
//   Pass min/max bounds; each node must be strictly within (min, max). O(n).

// TODO 5: Lowest Common Ancestor of BST — LeetCode #235
//   fn lowestCommonAncestor(root: ?*TreeNode, p: i32, q: i32) ?*TreeNode
//   If both > root.val → go right; both < → go left; else root is LCA. O(h).

// TODO 6: Level Order Traversal — LeetCode #102
//   fn levelOrder(root: ?*TreeNode, allocator: std.mem.Allocator) ![][]i32
//   BFS with ArrayList as queue; swap levels each iteration. O(n).

// TODO 7: Binary Tree Right Side View — LeetCode #199
//   fn rightSideView(root: ?*TreeNode, allocator: std.mem.Allocator) ![]i32
//   BFS; capture last node value of each level. O(n).

// TODO 8: Serialize / Deserialize Binary Tree — LeetCode #297
//   fn serialize(root: ?*TreeNode, allocator: std.mem.Allocator) ![]u8
//   fn deserialize(data: []const u8, allocator: std.mem.Allocator) !?*TreeNode
//   Pre-order with null markers ("N"). O(n).
