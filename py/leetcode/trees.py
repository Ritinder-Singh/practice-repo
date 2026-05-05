# =============================================================================
# Python LeetCode — Trees  (Blind 75 / NeetCode 150)
# =============================================================================
from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val; self.left=left; self.right=right

# LC #226 Invert Binary Tree
# def invert_tree(root): pass

# LC #104 Maximum Depth
# def max_depth(root): pass

# LC #100 Same Tree
# def is_same_tree(p, q): pass

# LC #572 Subtree of Another Tree
# def is_subtree(root, sub_root): pass

# LC #235 LCA of BST
# def lowest_common_ancestor(root, p, q): pass

# LC #102 Level Order Traversal — BFS
# def level_order(root) -> List[List[int]]: pass

# LC #98  Validate BST — pass min/max bounds
# def is_valid_bst(root): pass

# LC #230 Kth Smallest in BST — inorder
# def kth_smallest(root, k): pass

# LC #105 Build Tree from Preorder+Inorder
# def build_tree(preorder, inorder): pass

# LC #297 Serialize/Deserialize Binary Tree
# class Codec:
#     def serialize(self, root): pass
#     def deserialize(self, data): pass

# LC #208 Implement Trie
# class Trie:
#     def insert(self, word): pass
#     def search(self, word) -> bool: pass
#     def starts_with(self, prefix) -> bool: pass
