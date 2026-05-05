# =============================================================================
# DSA Foundations — Trees
# =============================================================================
# Topics: binary tree traversals (BFS/DFS), BST operations, height/diameter,
#         lowest common ancestor, serialization, trie.
# Run: python trees.py
# Ref: NeetCode 150 — Trees section
# =============================================================================

from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# -----------------------------------------------------------------------------
# TODO 1: DFS Traversals (Recursive and Iterative)
# -----------------------------------------------------------------------------
# Implement all three DFS orders:
#   inorder(root)   → left, root, right   (gives sorted order for BST)
#   preorder(root)  → root, left, right   (useful for serialization)
#   postorder(root) → left, right, root   (useful for deletion)
# Each should return List[int]. Implement both recursive AND iterative versions.
#
# def inorder(root: Optional[TreeNode]) -> List[int]:
#     pass

# -----------------------------------------------------------------------------
# TODO 2: BFS — Level Order Traversal — LeetCode #102
# -----------------------------------------------------------------------------
# Return nodes level by level as List[List[int]].
# Use a queue (deque). Process all nodes at current level before moving on.
#
# def level_order(root: Optional[TreeNode]) -> List[List[int]]:
#     pass

# -----------------------------------------------------------------------------
# TODO 3: Maximum Depth — LeetCode #104 (Blind 75)
# -----------------------------------------------------------------------------
# Return the maximum depth (number of nodes along the longest path from root to leaf).
# Implement recursively and iteratively (BFS).
#
# def max_depth(root: Optional[TreeNode]) -> int:
#     pass

# -----------------------------------------------------------------------------
# TODO 4: Same Tree — LeetCode #100
# -----------------------------------------------------------------------------
# Return True if two trees are structurally identical with same node values.
#
# def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#     pass

# -----------------------------------------------------------------------------
# TODO 5: Invert Binary Tree — LeetCode #226 (Blind 75)
# -----------------------------------------------------------------------------
# Mirror the tree (swap left and right children at every node).
# Implement recursively and iteratively.
#
# def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
#     pass

# -----------------------------------------------------------------------------
# TODO 6: Subtree of Another Tree — LeetCode #572 (Blind 75)
# -----------------------------------------------------------------------------
# Return True if subRoot is a subtree of root.
# For every node in root, check if the subtree rooted there equals subRoot.
# Reuse is_same_tree from TODO 4.
#
# def is_subtree(root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
#     pass

# -----------------------------------------------------------------------------
# TODO 7: Lowest Common Ancestor of BST — LeetCode #235 (Blind 75)
# -----------------------------------------------------------------------------
# In a BST, LCA is the deepest node that has both p and q as descendants.
# Use BST property: if both p,q < node → go left; if both > node → go right.
#
# def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
#     pass

# -----------------------------------------------------------------------------
# TODO 8: Binary Tree Level Order Traversal — LeetCode #102
# -----------------------------------------------------------------------------
# (Already covered above — now implement zigzag level order — LeetCode #103)
# Alternate left-to-right and right-to-left on each level.
#
# def zigzag_level_order(root: Optional[TreeNode]) -> List[List[int]]:
#     pass

# -----------------------------------------------------------------------------
# TODO 9: Validate Binary Search Tree — LeetCode #98 (Blind 75)
# -----------------------------------------------------------------------------
# Return True if the tree is a valid BST.
# Pass min/max bounds down recursively. Each node's value must be within bounds.
#
# def is_valid_bst(root: Optional[TreeNode]) -> bool:
#     pass

# -----------------------------------------------------------------------------
# TODO 10: Kth Smallest Element in BST — LeetCode #230 (Blind 75)
# -----------------------------------------------------------------------------
# Return the kth smallest value in the BST (1-indexed).
# Use inorder traversal (gives sorted order) and count to k.
#
# def kth_smallest(root: Optional[TreeNode], k: int) -> int:
#     pass

# -----------------------------------------------------------------------------
# TODO 11: Construct Binary Tree from Preorder and Inorder — LeetCode #105 (Blind 75)
# -----------------------------------------------------------------------------
# Root = preorder[0]. Find root in inorder to split left/right subtrees.
# Use a hash map of {val: index} in inorder for O(1) lookup.
#
# def build_tree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#     pass

# -----------------------------------------------------------------------------
# TODO 12: Serialize and Deserialize Binary Tree — LeetCode #297 (Blind 75)
# -----------------------------------------------------------------------------
# Encode a tree to a string and decode back. Use BFS or DFS with null markers.
#
# class Codec:
#     def serialize(self, root: Optional[TreeNode]) -> str:
#         pass
#
#     def deserialize(self, data: str) -> Optional[TreeNode]:
#         pass

# -----------------------------------------------------------------------------
# TODO 13: Implement Trie (Prefix Tree) — LeetCode #208 (Blind 75)
# -----------------------------------------------------------------------------
# Build a Trie supporting:
#   insert(word)
#   search(word) -> bool       (exact match)
#   starts_with(prefix) -> bool
# Use a TrieNode with children dict and is_end flag.
#
# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.is_end = False
#
# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
