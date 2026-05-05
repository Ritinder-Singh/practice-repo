# =============================================================================
# DSA Foundations — Arrays
# =============================================================================
# Topics: static/dynamic arrays, two-pointer, sliding window, prefix sums,
#         binary search on arrays, sorting-based techniques.
# Run: python arrays.py
# Ref: NeetCode 150 — Arrays & Hashing section
#      LeetCode Blind 75 — Array problems
# =============================================================================

from collections import defaultdict, deque
from typing import List

# -----------------------------------------------------------------------------
# TODO 1: Two Sum — LeetCode #1 (Blind 75)
# -----------------------------------------------------------------------------
# Given nums: List[int] and target: int, return indices of the two numbers
# that add up to target. Solve in O(n) using a hash map.
# Constraint: exactly one solution exists, cannot use same element twice.
#
# def two_sum(nums: List[int], target: int) -> List[int]:
#     pass

# -----------------------------------------------------------------------------
# TODO 2: Best Time to Buy and Sell Stock — LeetCode #121 (Blind 75)
# -----------------------------------------------------------------------------
# Given prices[], find the max profit from one buy and one sell.
# You must buy before you sell. Return 0 if no profit possible.
# Solve in O(n) with a single pass tracking the minimum price seen so far.
#
# def max_profit(prices: List[int]) -> int:
#     pass

# -----------------------------------------------------------------------------
# TODO 3: Contains Duplicate — LeetCode #217
# -----------------------------------------------------------------------------
# Return True if any value appears at least twice in the array.
# Solve in O(n) using a set.
#
# def contains_duplicate(nums: List[int]) -> bool:
#     pass

# -----------------------------------------------------------------------------
# TODO 4: Product of Array Except Self — LeetCode #238 (Blind 75)
# -----------------------------------------------------------------------------
# Return an array output where output[i] = product of all elements except nums[i].
# Solve in O(n) WITHOUT using division. Use prefix and suffix product arrays.
#
# def product_except_self(nums: List[int]) -> List[int]:
#     pass

# -----------------------------------------------------------------------------
# TODO 5: Maximum Subarray — LeetCode #53 (Blind 75)
# -----------------------------------------------------------------------------
# Find the contiguous subarray with the largest sum (Kadane's Algorithm).
# Return the sum. Array contains at least one element.
#
# def max_subarray(nums: List[int]) -> int:
#     pass

# -----------------------------------------------------------------------------
# TODO 6: Maximum Product Subarray — LeetCode #152 (Blind 75)
# -----------------------------------------------------------------------------
# Find the contiguous subarray with the largest product.
# Track both max and min products at each step (negatives can flip sign).
#
# def max_product(nums: List[int]) -> int:
#     pass

# -----------------------------------------------------------------------------
# TODO 7: Find Minimum in Rotated Sorted Array — LeetCode #153 (Blind 75)
# -----------------------------------------------------------------------------
# Array was sorted ascending then rotated. Find the minimum in O(log n).
# Use binary search.
#
# def find_min(nums: List[int]) -> int:
#     pass

# -----------------------------------------------------------------------------
# TODO 8: Search in Rotated Sorted Array — LeetCode #33 (Blind 75)
# -----------------------------------------------------------------------------
# Search for target in rotated sorted array. Return index or -1. O(log n).
# Determine which half is sorted, then decide which half to search.
#
# def search(nums: List[int], target: int) -> int:
#     pass

# -----------------------------------------------------------------------------
# TODO 9: 3Sum — LeetCode #15 (Blind 75)
# -----------------------------------------------------------------------------
# Find all unique triplets that sum to zero. Return List[List[int]].
# Sort the array first, then use two-pointer for each fixed element.
# Skip duplicates carefully.
#
# def three_sum(nums: List[int]) -> List[List[int]]:
#     pass

# -----------------------------------------------------------------------------
# TODO 10: Container With Most Water — LeetCode #11 (Blind 75)
# -----------------------------------------------------------------------------
# Find two lines that together form a container holding the most water.
# Use two-pointer from both ends, move the shorter side inward.
#
# def max_area(height: List[int]) -> int:
#     pass

# -----------------------------------------------------------------------------
# TODO 11: Sliding Window Maximum — LeetCode #239
# -----------------------------------------------------------------------------
# Return max of each sliding window of size k.
# Use a deque to maintain decreasing order of indices. O(n).
#
# def max_sliding_window(nums: List[int], k: int) -> List[int]:
#     pass

# -----------------------------------------------------------------------------
# TODO 12: Implement Dynamic Array from Scratch
# -----------------------------------------------------------------------------
# Build a resizable array class (like Python's list) backed by a fixed-size array.
# When capacity is exceeded, double the backing array.
# Methods: append(val), pop() -> val, get(i) -> val, set(i, val), insert(i, val), delete(i)
# Track: length (logical size) vs capacity (backing array size)
#
# class DynamicArray:
#     def __init__(self):
#         self._capacity = 1
#         self._length = 0
#         self._data = [None] * self._capacity
#
#     def append(self, val):
#         pass
#
#     def pop(self):
#         pass
#
#     def _resize(self):
#         pass

# -----------------------------------------------------------------------------
# TODO 13: Prefix Sum Array
# -----------------------------------------------------------------------------
# Build a prefix sum array from nums. Answer range sum queries [l, r] in O(1).
# Then implement: range_sum(prefix, l, r) -> sum of nums[l..r] inclusive.
#
# def build_prefix(nums: List[int]) -> List[int]:
#     pass
#
# def range_sum(prefix: List[int], l: int, r: int) -> int:
#     pass
