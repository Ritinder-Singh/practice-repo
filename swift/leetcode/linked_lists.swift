// TOPIC: Linked List Problems (LeetCode) | swift linked_lists.swift
// Run: swift linked_lists.swift

class ListNode {
    var val: Int
    var next: ListNode?
    init(_ val: Int, _ next: ListNode? = nil) {
        self.val = val
        self.next = next
    }
}

// TODO 1: LC #206 — Reverse Linked List
// Iteratively reverse pointers; return new head.
// func reverseList(_ head: ListNode?) -> ListNode?

// TODO 2: LC #21 — Merge Two Sorted Lists
// Use a dummy head node; compare values and stitch together in order.
// func mergeTwoLists(_ list1: ListNode?, _ list2: ListNode?) -> ListNode?

// TODO 3: LC #141 — Linked List Cycle
// Floyd's tortoise-and-hare algorithm; fast pointer moves 2, slow moves 1.
// func hasCycle(_ head: ListNode?) -> Bool

// TODO 4: LC #19 — Remove Nth Node From End of List
// Two-pointer gap of n; when fast hits nil, slow.next is the node to remove.
// func removeNthFromEnd(_ head: ListNode?, _ n: Int) -> ListNode?

// TODO 5: LC #23 — Merge K Sorted Lists
// Use a min-heap (priority queue) or divide-and-conquer merge pairs.
// func mergeKLists(_ lists: [ListNode?]) -> ListNode?

// TODO 6: LC #143 — Reorder List
// Find middle, reverse second half, then interleave first and reversed second half.
// func reorderList(_ head: ListNode?)
