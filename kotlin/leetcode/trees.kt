package leetcode
// TOPIC: Tree Problems | kotlinc trees.kt -include-runtime -d out.jar && java -jar out.jar

class TreeNode(var `val`: Int, var left: TreeNode? = null, var right: TreeNode? = null)

// Helper: insert into BST
fun insertBST(root: TreeNode?, value: Int): TreeNode {
    if (root == null) return TreeNode(value)
    if (value < root.`val`) root.left = insertBST(root.left, value)
    else root.right = insertBST(root.right, value)
    return root
}

// Helper: build BST from vararg values
fun buildBST(vararg vals: Int): TreeNode? {
    var root: TreeNode? = null
    for (v in vals) root = insertBST(root, v)
    return root
}

fun main() {
    // TODO 1: LC #104 — Maximum Depth of Binary Tree
    //   - Input: [3,9,20,null,null,15,7] → Output: 3
    //   - Strategy A (recursive DFS): 1 + max(depth(left), depth(right))
    //   - Strategy B (iterative BFS): level-order traversal, count levels
    //   - fun maxDepth(root: TreeNode?): Int
    //   - Base case: null → 0

    // TODO 2: LC #226 — Invert Binary Tree
    //   - Input: [4,2,7,1,3,6,9] → Output: [4,7,2,9,6,3,1]
    //   - Strategy (recursive): swap left and right, recurse on both children
    //   - fun invertTree(root: TreeNode?): TreeNode?
    //   - One-liner with apply: root?.apply { left = invertTree(right).also { right = invertTree(left) } }

    // TODO 3: LC #102 — Binary Tree Level Order Traversal
    //   - Input: [3,9,20,null,null,15,7] → Output: [[3],[9,20],[15,7]]
    //   - Strategy: BFS with ArrayDeque — process all nodes at current level before next
    //   - fun levelOrder(root: TreeNode?): List<List<Int>>
    //   - Snapshot queue size at start of each level to know how many to process

    // TODO 4: LC #98 — Validate Binary Search Tree
    //   - Input: [2,1,3] → Output: true; [5,1,4,null,null,3,6] → Output: false
    //   - Strategy: DFS with min/max bounds — each node must satisfy (min < val < max)
    //   - fun isValidBST(root: TreeNode?): Boolean
    //   - Pass Long.MIN_VALUE/Long.MAX_VALUE initially; update bounds going left/right
    //   - Alternative: in-order traversal should produce strictly ascending sequence

    // TODO 5: LC #230 — Kth Smallest Element in a BST
    //   - Input: root = [3,1,4,null,2], k = 1 → Output: 1
    //   - Strategy A (recursive in-order): collect values, return k-th
    //   - Strategy B (iterative in-order with early stop): stop when count reaches k
    //   - fun kthSmallest(root: TreeNode?, k: Int): Int
    //   - Iterative uses explicit stack — push left nodes until null, pop, count, go right

    // TODO 6: LC #235 — Lowest Common Ancestor of BST
    //   - Input: root = [6,2,8,0,4,7,9], p=2, q=8 → Output: 6
    //   - Strategy: leverage BST property — if both p,q < root → go left; both > root → go right; else root is LCA
    //   - fun lowestCommonAncestor(root: TreeNode?, p: TreeNode?, q: TreeNode?): TreeNode?
    //   - O(h) time where h = height; O(1) space with iterative approach

    // TODO 7: LC #572 — Subtree of Another Tree
    //   - Input: root = [3,4,5,1,2], subRoot = [4,1,2] → Output: true
    //   - Strategy: for each node in root, check if subtree rooted there equals subRoot
    //   - fun isSubtree(root: TreeNode?, subRoot: TreeNode?): Boolean
    //   - Helper: fun isSameTree(s: TreeNode?, t: TreeNode?): Boolean
    //   - O(m*n) naive; O(m+n) with tree serialization + KMP/hashing
}
