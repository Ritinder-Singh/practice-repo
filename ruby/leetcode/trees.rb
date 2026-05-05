# frozen_string_literal: true
# TOPIC: Tree LeetCode Problems | ruby trees.rb

class TreeNode
  attr_accessor :val, :left, :right
  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# TODO 1: Maximum Depth of Binary Tree — LC #104
#   def max_depth(root)
#     # Base: nil → 0; recursive: 1 + [max_depth(left), max_depth(right)].max
#   end

# TODO 2: Invert Binary Tree — LC #226
#   def invert_tree(root)
#     # Swap left and right at each node recursively
#   end

# TODO 3: Binary Tree Level Order Traversal — LC #102
#   def level_order(root)
#     # BFS with Queue; track level size each iteration
#   end

# TODO 4: Validate Binary Search Tree — LC #98
#   def is_valid_bst(root, min: -Float::INFINITY, max: Float::INFINITY)
#     # Pass bounds: left subtree max=node.val, right subtree min=node.val
#   end

# TODO 5: Kth Smallest Element in BST — LC #230
#   def kth_smallest(root, k)
#     # In-order traversal; decrement k each visit; return when k == 0
#   end

# TODO 6: Lowest Common Ancestor of BST — LC #235
#   def lowest_common_ancestor(root, p, q)
#     # Both < root → go left; both > root → go right; else root is LCA
#   end

# TODO 7: Subtree of Another Tree — LC #572
#   def is_subtree(root, sub_root)
#     # DFS; at each node check is_same_tree?(node, sub_root)
#   end
