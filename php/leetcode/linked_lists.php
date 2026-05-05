<?php
declare(strict_types=1);
// TOPIC: Linked List LeetCode Problems | php linked_lists.php

class ListNode {
    public function __construct(
        public int $val = 0,
        public ?ListNode $next = null,
    ) {}
}

// TODO 1: Reverse Linked List — LC #206
//   function reverseList(?ListNode $head): ?ListNode
//   // Iterative: $prev=null, $curr=$head; swap pointers as you advance

// TODO 2: Merge Two Sorted Lists — LC #21
//   function mergeTwoLists(?ListNode $list1, ?ListNode $list2): ?ListNode
//   // Dummy node; compare heads, advance smaller

// TODO 3: Linked List Cycle — LC #141
//   function hasCycle(?ListNode $head): bool
//   // Floyd's: slow=head, fast=head; if they meet → cycle

// TODO 4: Remove Nth Node From End of List — LC #19
//   function removeNthFromEnd(?ListNode $head, int $n): ?ListNode
//   // Two pointers n apart

// TODO 5: Merge K Sorted Lists — LC #23
//   function mergeKLists(array $lists): ?ListNode
//   // Min-heap using SplMinHeap

// TODO 6: Reorder List — LC #143
//   function reorderList(?ListNode $head): void
//   // Find middle, reverse second half, merge alternating
