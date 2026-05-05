// TOPIC: Tree LeetCode Problems | dart trees.dart

class TreeNode {
  int val;
  TreeNode? left;
  TreeNode? right;
  TreeNode([this.val = 0, this.left, this.right]);
}

// TODO 1: Maximum Depth of Binary Tree — LC #104
//   int maxDepth(TreeNode? root)
//   - Base: null → 0; 1 + max(maxDepth(left), maxDepth(right))

// TODO 2: Invert Binary Tree — LC #226
//   TreeNode? invertTree(TreeNode? root)
//   - Swap left and right at each node recursively

// TODO 3: Binary Tree Level Order Traversal — LC #102
//   List<List<int>> levelOrder(TreeNode? root)
//   - BFS with Queue; track level size each iteration

// TODO 4: Validate Binary Search Tree — LC #98
//   bool isValidBST(TreeNode? root, {double min = double.negativeInfinity, double max = double.infinity})
//   - Pass min/max bounds; return false if node.val out of range

// TODO 5: Kth Smallest Element in BST — LC #230
//   int kthSmallest(TreeNode? root, int k)
//   - In-order traversal; decrement k each visit; return when k hits 0

// TODO 6: Lowest Common Ancestor of BST — LC #235
//   TreeNode? lowestCommonAncestor(TreeNode? root, TreeNode p, TreeNode q)
//   - Both < root: go left; both > root: go right; else root is LCA

// TODO 7: Subtree of Another Tree — LC #572
//   bool isSubtree(TreeNode? root, TreeNode? subRoot)
//   - DFS; at each node check isSameTree(node, subRoot)

void main() {}
