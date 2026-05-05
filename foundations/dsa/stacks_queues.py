# =============================================================================
# DSA Foundations — Stacks & Queues
# =============================================================================
# Topics: stack/queue from scratch, monotonic stack, deque-based queue,
#         balanced parentheses, next greater element, sliding window max.
# Run: python stacks_queues.py
# Ref: NeetCode 150 — Stack section
# =============================================================================

from collections import deque
from typing import List

# -----------------------------------------------------------------------------
# TODO 1: Implement Stack from Scratch
# -----------------------------------------------------------------------------
# Build a Stack class using a Python list as the backing store.
#   push(val)       — add to top
#   pop() -> val    — remove and return top (raise if empty)
#   peek() -> val   — return top without removing
#   is_empty() -> bool
#   size() -> int
#
# class Stack:
#     pass

# -----------------------------------------------------------------------------
# TODO 2: Implement Queue from Scratch (Two Stacks)
# -----------------------------------------------------------------------------
# Implement a Queue using two stacks.
# Amortized O(1) enqueue and dequeue.
#   enqueue(val)
#   dequeue() -> val
#   peek() -> val
#   is_empty() -> bool
#
# class QueueFromStacks:
#     pass

# -----------------------------------------------------------------------------
# TODO 3: Valid Parentheses — LeetCode #20 (Blind 75)
# -----------------------------------------------------------------------------
# Return True if the string of brackets is valid (properly nested/closed).
# Use a stack. Push open brackets, pop and check on close brackets.
#
# def is_valid(s: str) -> bool:
#     pass

# -----------------------------------------------------------------------------
# TODO 4: Min Stack — LeetCode #155
# -----------------------------------------------------------------------------
# Design a stack that supports push, pop, top, and retrieving the minimum
# element in O(1). Use an auxiliary stack tracking minimums.
#
# class MinStack:
#     def push(self, val: int) -> None: pass
#     def pop(self) -> None: pass
#     def top(self) -> int: pass
#     def get_min(self) -> int: pass

# -----------------------------------------------------------------------------
# TODO 5: Evaluate Reverse Polish Notation — LeetCode #150
# -----------------------------------------------------------------------------
# Evaluate an expression in RPN (postfix). Operands are integers, operators
# are "+", "-", "*", "/". Division truncates toward zero.
# Use a stack: push operands, pop two on operators.
#
# def eval_rpn(tokens: List[str]) -> int:
#     pass

# -----------------------------------------------------------------------------
# TODO 6: Generate Parentheses — LeetCode #22
# -----------------------------------------------------------------------------
# Generate all combinations of n pairs of valid parentheses.
# Use backtracking: track open and close counts.
#
# def generate_parentheses(n: int) -> List[str]:
#     pass

# -----------------------------------------------------------------------------
# TODO 7: Daily Temperatures — LeetCode #739
# -----------------------------------------------------------------------------
# For each day, find how many days until a warmer temperature.
# Return result array. Use a monotonic decreasing stack of indices.
#
# def daily_temperatures(temperatures: List[int]) -> List[int]:
#     pass

# -----------------------------------------------------------------------------
# TODO 8: Next Greater Element I — LeetCode #496
# -----------------------------------------------------------------------------
# For each element in nums1, find the next greater element in nums2.
# Use a monotonic stack + hash map. O(n+m).
#
# def next_greater_element(nums1: List[int], nums2: List[int]) -> List[int]:
#     pass

# -----------------------------------------------------------------------------
# TODO 9: Largest Rectangle in Histogram — LeetCode #84
# -----------------------------------------------------------------------------
# Find the largest rectangle that can be formed in the histogram.
# Use a monotonic increasing stack of (index, height).
#
# def largest_rectangle(heights: List[int]) -> int:
#     pass

# -----------------------------------------------------------------------------
# TODO 10: Implement Circular Queue
# -----------------------------------------------------------------------------
# Build a CircularQueue (ring buffer) of fixed capacity using a list.
#   enqueue(val) -> bool
#   dequeue() -> bool
#   front() -> int
#   rear() -> int
#   is_empty() -> bool
#   is_full() -> bool
# Track head, tail, and size.
#
# class CircularQueue:
#     def __init__(self, k: int):
#         pass
