#include <stdio.h>
#include <stdlib.h>
// TOPIC: Trees — LeetCode | gcc -o out trees.c && ./out

typedef struct TreeNode { int val; struct TreeNode *left, *right; } TreeNode;

int main(void) { printf("Trees LeetCode — TODO: implement\n"); return 0; }

// TODO 1: Maximum Depth of Binary Tree — LeetCode #104
//   int maxDepth(TreeNode *root)
//   Recursive: 1 + max(left, right). Base: NULL → 0. O(n).

// TODO 2: Invert Binary Tree — LeetCode #226
//   TreeNode *invertTree(TreeNode *root)
//   Swap left/right, recurse both subtrees. O(n).

// TODO 3: Validate BST — LeetCode #98
//   bool isValidBST(TreeNode *root)
//   Pass long min/max bounds (use LONG_MIN/LONG_MAX to handle INT limits). O(n).

// TODO 4: Lowest Common Ancestor of BST — LeetCode #235
//   TreeNode *lowestCommonAncestor(TreeNode *root, TreeNode *p, TreeNode *q)
//   Navigate by value comparison in BST. O(h).

// TODO 5: Level Order Traversal — LeetCode #102
//   int **levelOrder(TreeNode *root, int *returnSize, int **returnColumnSizes)
//   BFS with queue (array-based); track level boundaries. O(n).

// TODO 6: Binary Tree Right Side View — LeetCode #199
//   int *rightSideView(TreeNode *root, int *returnSize)
//   BFS; record last node value per level. O(n).

// TODO 7: Construct Binary Tree from Preorder and Inorder — LeetCode #105
//   TreeNode *buildTree(int *preorder, int preSize, int *inorder, int inSize)
//   preorder[0] = root; find root in inorder to split left/right. O(n²) naive.

// TODO 8: Serialize / Deserialize Binary Tree — LeetCode #297
//   char *serialize(TreeNode *root)
//   TreeNode *deserialize(char *data)
//   BFS or preorder with "N" for nulls; strtok for deserialization. O(n).
