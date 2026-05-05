package leetcode;
// TOPIC: Tree LeetCode Problems | javac Trees.java && java leetcode.Trees
// Docs: https://leetcode.com/tag/tree/

public class Trees {

    // Definition for a binary tree node
    static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val; this.left = left; this.right = right;
        }
    }

    // TODO 1: Maximum Depth of Binary Tree — LC #104
    //   int maxDepth(TreeNode root)
    //   - Recursive: 1 + max(maxDepth(left), maxDepth(right))
    //   - Iterative: BFS level count

    // TODO 2: Invert Binary Tree — LC #226
    //   TreeNode invertTree(TreeNode root)
    //   - Swap left and right children recursively

    // TODO 3: Binary Tree Level Order Traversal — LC #102
    //   List<List<Integer>> levelOrder(TreeNode root)
    //   - BFS with Queue<TreeNode>, track level size

    // TODO 4: Validate Binary Search Tree — LC #98
    //   boolean isValidBST(TreeNode root)
    //   - Pass min/max bounds recursively: isValid(node, Long.MIN_VALUE, Long.MAX_VALUE)

    // TODO 5: Kth Smallest Element in BST — LC #230
    //   int kthSmallest(TreeNode root, int k)
    //   - In-order traversal (Left → Root → Right), count nodes visited

    // TODO 6: Lowest Common Ancestor of BST — LC #235
    //   TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q)
    //   - If both p,q < root → go left; if both > root → go right; else root is LCA

    // TODO 7: Subtree of Another Tree — LC #572
    //   boolean isSubtree(TreeNode root, TreeNode subRoot)
    //   - For each node in root, check isSameTree(node, subRoot)

    // TODO 8: Binary Tree Right Side View — LC #199
    //   List<Integer> rightSideView(TreeNode root)
    //   - BFS, take last element of each level

    public static void main(String[] args) {}
}
