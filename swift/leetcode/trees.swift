// TOPIC: Tree Problems (LeetCode) | swift trees.swift
// Run: swift trees.swift

class TreeNode {
    var val: Int
    var left: TreeNode?
    var right: TreeNode?
    init(_ val: Int, _ left: TreeNode? = nil, _ right: TreeNode? = nil) {
        self.val = val
        self.left = left
        self.right = right
    }
}

// TODO 1: LC #104 — Maximum Depth of Binary Tree
// Recursive DFS: return 1 + max(depth(left), depth(right)); base case nil returns 0.
// func maxDepth(_ root: TreeNode?) -> Int

// TODO 2: LC #226 — Invert Binary Tree
// Recursively swap left and right children at every node.
// func invertTree(_ root: TreeNode?) -> TreeNode?

// TODO 3: LC #102 — Binary Tree Level Order Traversal
// BFS with a queue; collect all nodes at each level into a separate array.
// func levelOrder(_ root: TreeNode?) -> [[Int]]

// TODO 4: LC #98 — Validate Binary Search Tree
// Pass valid (min, max) range down; left subtree max = node.val, right subtree min = node.val.
// func isValidBST(_ root: TreeNode?) -> Bool

// TODO 5: LC #230 — Kth Smallest Element in a BST
// In-order traversal yields sorted values; return the kth one visited.
// func kthSmallest(_ root: TreeNode?, _ k: Int) -> Int

// TODO 6: LC #235 — Lowest Common Ancestor of a BST
// If both p and q are less than node, go left; if both greater, go right; else current is LCA.
// func lowestCommonAncestor(_ root: TreeNode?, _ p: TreeNode?, _ q: TreeNode?) -> TreeNode?

// TODO 7: LC #572 — Subtree of Another Tree
// For each node, check if the subtree rooted there equals `subRoot` using isSameTree helper.
// func isSubtree(_ root: TreeNode?, _ subRoot: TreeNode?) -> Bool
