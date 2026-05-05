#include <stdio.h>
#include <stdlib.h>
// TOPIC: Linked Lists — LeetCode | gcc -o out linked_lists.c && ./out

typedef struct ListNode { int val; struct ListNode *next; } ListNode;

int main(void) { printf("Linked Lists LeetCode — TODO: implement\n"); return 0; }

// TODO 1: Reverse Linked List — LeetCode #206
//   ListNode *reverseList(ListNode *head)
//   Three-pointer iterative: prev=NULL, curr=head. O(n) O(1).

// TODO 2: Merge Two Sorted Lists — LeetCode #21
//   ListNode *mergeTwoLists(ListNode *l1, ListNode *l2)
//   Dummy head; compare and link smaller. O(n+m) O(1).

// TODO 3: Linked List Cycle — LeetCode #141
//   bool hasCycle(ListNode *head)
//   Floyd's: slow=head, fast=head; fast && fast->next or return false. O(n) O(1).

// TODO 4: Remove Nth Node From End — LeetCode #19
//   ListNode *removeNthFromEnd(ListNode *head, int n)
//   Two pointers n apart; when right reaches end, delete left->next. O(L).

// TODO 5: Reorder List — LeetCode #143
//   void reorderList(ListNode *head)
//   Find mid (slow/fast), reverse second half, interleave. O(n) O(1).

// TODO 6: Find Duplicate Number — LeetCode #287
//   int findDuplicate(int *nums, int n)
//   Treat array as linked list; Floyd's cycle detection. O(n) O(1).

// TODO 7: LRU Cache — LeetCode #146
//   Design with doubly-linked list + hash table (uthash or custom). O(1) per op.

// TODO 8: Merge K Sorted Lists — LeetCode #23
//   ListNode *mergeKLists(ListNode **lists, int k)
//   Min-heap of size k; pop min node, push its next. O(n log k).
