// TOPIC: Linked List LeetCode Problems | dart linked_lists.dart

class ListNode {
  int val;
  ListNode? next;
  ListNode([this.val = 0, this.next]);
}

// TODO 1: Reverse Linked List — LC #206
//   ListNode? reverseList(ListNode? head)
//   - Iterative: prev=null, curr=head; while curr: tmp=curr.next, curr.next=prev, prev=curr, curr=tmp

// TODO 2: Merge Two Sorted Lists — LC #21
//   ListNode? mergeTwoLists(ListNode? list1, ListNode? list2)
//   - Dummy node; compare heads, advance the smaller pointer

// TODO 3: Linked List Cycle — LC #141
//   bool hasCycle(ListNode? head)
//   - Floyd's tortoise and hare: slow=head, fast=head; if they meet, cycle exists

// TODO 4: Remove Nth Node From End of List — LC #19
//   ListNode? removeNthFromEnd(ListNode? head, int n)
//   - Two pointers n apart; when fast reaches end, slow.next is the target

// TODO 5: Merge K Sorted Lists — LC #23
//   ListNode? mergeKLists(List<ListNode?> lists)
//   - Use priority queue (PriorityQueue from package:collection); min by val

// TODO 6: Reorder List — LC #143
//   void reorderList(ListNode? head)
//   - Find middle, reverse second half, merge two halves alternating

void main() {}
