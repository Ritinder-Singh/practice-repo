// =============================================================================
// Rust LeetCode — Linked Lists
// =============================================================================
// Note: Linked lists are notoriously tricky in Rust due to ownership.
// Recommended: use Box<ListNode> for simple singly-linked list.
fn main() { println!("Rust linked lists leetcode"); }

#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode { pub val: i32, pub next: Option<Box<ListNode>> }

// LC #206 Reverse Linked List
// fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> { None }

// LC #21  Merge Two Sorted Lists
// fn merge_two_lists(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> { None }

// LC #141 Linked List Cycle — use HashSet of raw pointers (unsafe) or Floyd's algorithm
// fn has_cycle(head: Option<Box<ListNode>>) -> bool { false }
// Note: Rust's ownership makes cycles impossible in safe code — use raw pointers for this problem.
