# =============================================================================
# DSA Foundations — Linked Lists
# =============================================================================
# Topics: singly linked list from scratch, doubly linked list, fast/slow pointers,
#         reversal, cycle detection, merge, Floyd's algorithm.
# Run: python linked_list.py
# Ref: NeetCode 150 — Linked List section
# =============================================================================

from typing import Optional

# Node definition — used throughout this file
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper to build a linked list from a Python list
# def build_list(vals: list) -> Optional[ListNode]: ...
# Helper to convert linked list to Python list for printing
# def to_list(head: Optional[ListNode]) -> list: ...

# -----------------------------------------------------------------------------
# TODO 1: Implement Singly Linked List from Scratch
# -----------------------------------------------------------------------------
# Build a SinglyLinkedList class with:
#   append(val)         — add to tail
#   prepend(val)        — add to head
#   delete(val)         — remove first node with this value
#   search(val) -> bool — check if value exists
#   length() -> int     — count nodes
#   to_list() -> list   — convert to Python list
#
# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None

# -----------------------------------------------------------------------------
# TODO 2: Reverse a Linked List — LeetCode #206 (Blind 75)
# -----------------------------------------------------------------------------
# Reverse the list iteratively. Return new head.
# Then implement recursively as well.
#
# def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
#     pass

# -----------------------------------------------------------------------------
# TODO 3: Detect Cycle — LeetCode #141 (Blind 75)
# -----------------------------------------------------------------------------
# Use Floyd's fast/slow pointer algorithm. Return True if cycle exists.
#
# def has_cycle(head: Optional[ListNode]) -> bool:
#     pass

# -----------------------------------------------------------------------------
# TODO 4: Find Cycle Start — LeetCode #142
# -----------------------------------------------------------------------------
# Return the node where the cycle begins, or None.
# Floyd's algorithm: after detecting meeting point, move one pointer to head,
# advance both one step at a time — they meet at cycle start.
#
# def detect_cycle(head: Optional[ListNode]) -> Optional[ListNode]:
#     pass

# -----------------------------------------------------------------------------
# TODO 5: Merge Two Sorted Lists — LeetCode #21 (Blind 75)
# -----------------------------------------------------------------------------
# Merge two sorted linked lists into one sorted list. Return head.
# Implement iteratively (using a dummy node) and recursively.
#
# def merge_two_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#     pass

# -----------------------------------------------------------------------------
# TODO 6: Reorder List — LeetCode #143 (Blind 75)
# -----------------------------------------------------------------------------
# Reorder: L0→L1→…→Ln-1→Ln into L0→Ln→L1→Ln-1→L2→Ln-2→…
# Steps: 1) Find middle (slow/fast), 2) Reverse second half, 3) Merge halves.
#
# def reorder_list(head: Optional[ListNode]) -> None:
#     pass

# -----------------------------------------------------------------------------
# TODO 7: Remove Nth Node From End — LeetCode #19 (Blind 75)
# -----------------------------------------------------------------------------
# Remove the nth node from the end in one pass.
# Use two pointers: advance the first pointer n steps, then move both until
# first reaches the end.
#
# def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
#     pass

# -----------------------------------------------------------------------------
# TODO 8: Find Middle of Linked List — LeetCode #876
# -----------------------------------------------------------------------------
# Return middle node (if two middles, return the second one).
# Use slow/fast pointer — slow moves 1 step, fast moves 2 steps.
#
# def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
#     pass

# -----------------------------------------------------------------------------
# TODO 9: Merge K Sorted Lists — LeetCode #23 (Blind 75)
# -----------------------------------------------------------------------------
# Merge k sorted linked lists into one sorted list.
# Use a min-heap of (val, index, node) tuples for O(n log k).
#
# import heapq
# def merge_k_lists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
#     pass

# -----------------------------------------------------------------------------
# TODO 10: Implement LRU Cache — LeetCode #146
# -----------------------------------------------------------------------------
# Design an LRU (Least Recently Used) Cache with O(1) get and put.
# Use a doubly linked list + hash map.
#   get(key) -> int: return value or -1 if not found (mark as recently used)
#   put(key, val): insert/update, evict LRU if over capacity
#
# class LRUCache:
#     def __init__(self, capacity: int):
#         pass
#
#     def get(self, key: int) -> int:
#         pass
#
#     def put(self, key: int, value: int) -> None:
#         pass
