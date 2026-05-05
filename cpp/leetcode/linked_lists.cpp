#include <iostream>
// TOPIC: Linked Lists — LeetCode | g++ -std=c++20 -o out linked_lists.cpp && ./out

struct ListNode { int val; ListNode *next; ListNode(int v) : val(v), next(nullptr) {} };

int main() { std::cout << "Linked Lists LeetCode — TODO: implement\n"; return 0; }

// TODO 1: Reverse Linked List — LeetCode #206
//   ListNode* reverseList(ListNode* head)
//   Three-pointer iterative. O(n) O(1).

// TODO 2: Merge Two Sorted Lists — LeetCode #21
//   ListNode* mergeTwoLists(ListNode* l1, ListNode* l2)
//   Dummy head; link smaller node. O(n+m) O(1).

// TODO 3: Linked List Cycle — LeetCode #141
//   bool hasCycle(ListNode *head)
//   Floyd's tortoise and hare. O(n) O(1).

// TODO 4: Remove Nth Node From End — LeetCode #19
//   ListNode* removeNthFromEnd(ListNode* head, int n)
//   Two-pointer gap n; remove when right reaches end. O(L).

// TODO 5: Reorder List — LeetCode #143
//   void reorderList(ListNode* head)
//   Find mid, reverse second half, interleave. O(n) O(1).

// TODO 6: LRU Cache — LeetCode #146
//   class LRUCache — doubly-linked list + unordered_map. O(1) get/put.

// TODO 7: Copy List with Random Pointer — LeetCode #138
//   Node* copyRandomList(Node* head)
//   unordered_map<Node*,Node*> for old→new mapping. O(n).

// TODO 8: Merge K Sorted Lists — LeetCode #23
//   ListNode* mergeKLists(vector<ListNode*>& lists)
//   Min priority_queue<pair<int,ListNode*>>. O(n log k).
