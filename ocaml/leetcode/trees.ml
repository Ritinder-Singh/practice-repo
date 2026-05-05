(* TOPIC: Tree LeetCode Problems | ocaml trees.ml *)

(* Binary tree definition *)
(* type 'a tree = Leaf | Node of 'a tree * 'a * 'a tree *)

(* TODO 1: Maximum Depth of Binary Tree — LC #104
   let max_depth root =
     (* match root with Leaf -> 0 | Node(l,_,r) -> 1 + max (max_depth l) (max_depth r) *)  *)

(* TODO 2: Invert Binary Tree — LC #226
   let invert_tree root =
     (* match root with Leaf -> Leaf | Node(l,v,r) -> Node(invert_tree r, v, invert_tree l) *)  *)

(* TODO 3: Binary Tree Level Order Traversal — LC #102
   let level_order root =
     (* BFS using Queue; track level size *)  *)

(* TODO 4: Validate Binary Search Tree — LC #98
   let is_valid_bst root =
     (* Pass bounds: is_valid (min_opt, max_opt) node *)  *)

(* TODO 5: Kth Smallest Element in BST — LC #230
   let kth_smallest root k =
     (* In-order traversal; track count with ref *)  *)

(* TODO 6: Lowest Common Ancestor of BST — LC #235
   let lowest_common_ancestor root p q =
     (* Both < root: go left; both > root: go right; else root is LCA *)  *)

(* TODO 7: Subtree of Another Tree — LC #572
   let is_subtree root sub_root =
     (* For each node check is_same_tree *)  *)

let () = print_endline "TODO: implement tree problems"
