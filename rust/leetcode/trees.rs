// =============================================================================
// Rust LeetCode — Trees
// =============================================================================
fn main() { println!("Rust trees leetcode"); }

use std::cell::RefCell;
use std::rc::Rc;

// LeetCode uses Rc<RefCell<TreeNode>> for shared mutable tree nodes
type TreeNodeRef = Option<Rc<RefCell<TreeNode>>>;
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode { pub val: i32, pub left: TreeNodeRef, pub right: TreeNodeRef }
impl TreeNode { pub fn new(val: i32) -> Rc<RefCell<Self>> { Rc::new(RefCell::new(Self { val, left: None, right: None })) } }

// LC #226 Invert Binary Tree
// fn invert_tree(root: TreeNodeRef) -> TreeNodeRef { None }

// LC #104 Maximum Depth
// fn max_depth(root: TreeNodeRef) -> i32 { 0 }

// LC #102 Level Order Traversal
// fn level_order(root: TreeNodeRef) -> Vec<Vec<i32>> { vec![] }

// LC #98  Validate BST
// fn is_valid_bst(root: TreeNodeRef) -> bool { false }
