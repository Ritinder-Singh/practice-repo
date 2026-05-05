module Trees where
-- TOPIC: Tree LeetCode Problems | ghci: :load trees.hs
import Data.Maybe (fromMaybe)
import qualified Data.Map.Strict as Map

data Tree a = Leaf | Node (Tree a) a (Tree a) deriving (Show, Eq)

-- TODO 1: Maximum Depth of Binary Tree — LC #104
-- maxDepth :: Tree a -> Int
-- maxDepth Leaf = 0
-- maxDepth (Node l _ r) = 1 + max (maxDepth l) (maxDepth r)

-- TODO 2: Invert Binary Tree — LC #226
-- invertTree :: Tree a -> Tree a
-- invertTree Leaf = Leaf
-- invertTree (Node l v r) = Node (invertTree r) v (invertTree l)

-- TODO 3: Binary Tree Level Order Traversal — LC #102
-- levelOrder :: Tree a -> [[a]]
-- -- BFS using a queue (list of lists)
-- levelOrder Leaf = []
-- levelOrder root = go [root]
--   where go [] = []
--         go level = [v | Node _ v _ <- level] : go [child | Node l _ r <- level, child <- [l, r], child /= Leaf]

-- TODO 4: Validate Binary Search Tree — LC #98
-- isValidBST :: Ord a => Tree a -> Bool
-- isValidBST = go Nothing Nothing
--   where go lo hi Leaf = True
--         go lo hi (Node l v r) =
--           maybe True (<v) lo && maybe True (>v) hi &&
--           go lo (Just v) l && go (Just v) hi r

-- TODO 5: Kth Smallest Element in BST — LC #230
-- kthSmallest :: Tree a -> Int -> Maybe a
-- kthSmallest root k = inorder root !! (k-1)
--   where inorder Leaf = []
--         inorder (Node l v r) = inorder l ++ [v] ++ inorder r

-- TODO 6: Lowest Common Ancestor of BST — LC #235
-- lowestCommonAncestor :: Ord a => Tree a -> a -> a -> Maybe a
-- -- Both < root: go left; both > root: go right; else root is LCA

-- TODO 7: Subtree of Another Tree — LC #572
-- isSubtree :: Eq a => Tree a -> Tree a -> Bool
-- isSubtree Leaf _ = False
-- isSubtree tree sub = tree == sub || isSubtree' tree sub
--   where isSubtree' Leaf _ = False
--         isSubtree' (Node l _ r) sub = l == sub || r == sub || isSubtree' l sub || isSubtree' r sub
