# =============================================================================
# Python LeetCode — Linked Lists  (Blind 75 / NeetCode 150)
# =============================================================================
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val; self.next = next

# LC #206 Reverse Linked List — iterative + recursive
# def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]: pass

# LC #21  Merge Two Sorted Lists — dummy node
# def merge_two_lists(l1, l2): pass

# LC #143 Reorder List — find mid, reverse half, merge
# def reorder_list(head: Optional[ListNode]) -> None: pass

# LC #19  Remove Nth From End — two pointers
# def remove_nth_from_end(head, n): pass

# LC #141 Linked List Cycle — fast/slow pointers
# def has_cycle(head): pass

# LC #142 Linked List Cycle II — find cycle start (Floyd's)
# def detect_cycle(head): pass

# LC #23  Merge K Sorted Lists — min-heap O(n log k)
# def merge_k_lists(lists): pass

# LC #146 LRU Cache — doubly linked list + hash map O(1)
# class LRUCache:
#     def __init__(self, capacity: int): pass
#     def get(self, key: int) -> int: pass
#     def put(self, key: int, value: int) -> None: pass
