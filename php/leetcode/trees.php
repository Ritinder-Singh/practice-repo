<?php
declare(strict_types=1);
// TOPIC: Tree LeetCode Problems | php trees.php

class TreeNode {
    public function __construct(
        public int $val = 0,
        public ?TreeNode $left = null,
        public ?TreeNode $right = null,
    ) {}
}

// TODO 1: Maximum Depth of Binary Tree — LC #104
//   function maxDepth(?TreeNode $root): int
//   // 1 + max(maxDepth($left), maxDepth($right))

// TODO 2: Invert Binary Tree — LC #226
//   function invertTree(?TreeNode $root): ?TreeNode

// TODO 3: Binary Tree Level Order Traversal — LC #102
//   function levelOrder(?TreeNode $root): array
//   // BFS with SplQueue; track level size

// TODO 4: Validate Binary Search Tree — LC #98
//   function isValidBST(?TreeNode $root, float $min = PHP_INT_MIN, float $max = PHP_INT_MAX): bool

// TODO 5: Kth Smallest Element in BST — LC #230
//   function kthSmallest(?TreeNode $root, int $k): int
//   // In-order traversal; decrement k each visit

// TODO 6: Lowest Common Ancestor of BST — LC #235
//   function lowestCommonAncestor(?TreeNode $root, TreeNode $p, TreeNode $q): ?TreeNode

// TODO 7: Subtree of Another Tree — LC #572
//   function isSubtree(?TreeNode $root, ?TreeNode $subRoot): bool
