# =============================================================================
# DSA Foundations — Sorting Algorithms
# =============================================================================
# Topics: bubble, selection, insertion, merge, quick, heap sort.
#         Analysis: time/space complexity for each.
# Run: python sorting.py
# =============================================================================

from typing import List
import random

# -----------------------------------------------------------------------------
# TODO 1: Bubble Sort — O(n²) time, O(1) space
# -----------------------------------------------------------------------------
# Repeatedly swap adjacent elements if out of order.
# Optimization: stop early if no swaps in a pass (already sorted).
#
# def bubble_sort(arr: List[int]) -> List[int]:
#     pass

# -----------------------------------------------------------------------------
# TODO 2: Selection Sort — O(n²) time, O(1) space
# -----------------------------------------------------------------------------
# Find the minimum in the unsorted portion, swap it to the sorted position.
#
# def selection_sort(arr: List[int]) -> List[int]:
#     pass

# -----------------------------------------------------------------------------
# TODO 3: Insertion Sort — O(n²) worst, O(n) best, O(1) space
# -----------------------------------------------------------------------------
# Build sorted portion by inserting each element into correct position.
# Efficient for nearly sorted arrays.
#
# def insertion_sort(arr: List[int]) -> List[int]:
#     pass

# -----------------------------------------------------------------------------
# TODO 4: Merge Sort — O(n log n) time, O(n) space
# -----------------------------------------------------------------------------
# Divide array in half recursively, then merge sorted halves.
# Stable sort. Used in Python's Timsort.
#
# def merge_sort(arr: List[int]) -> List[int]:
#     pass
#
# def merge(left: List[int], right: List[int]) -> List[int]:
#     pass

# -----------------------------------------------------------------------------
# TODO 5: Quick Sort — O(n log n) avg, O(n²) worst, O(log n) space
# -----------------------------------------------------------------------------
# Pick a pivot, partition array so elements < pivot are left, > pivot are right.
# Recurse on both sides. Randomize pivot to avoid worst case.
#
# def quick_sort(arr: List[int], low: int = 0, high: int = None) -> None:
#     pass  # in-place
#
# def partition(arr: List[int], low: int, high: int) -> int:
#     pass

# -----------------------------------------------------------------------------
# TODO 6: Heap Sort — O(n log n) time, O(1) space
# -----------------------------------------------------------------------------
# Build a max-heap (heapify), then repeatedly extract max to sorted position.
# Not stable, but in-place.
#
# def heap_sort(arr: List[int]) -> None:
#     pass  # in-place
#
# def heapify(arr: List[int], n: int, i: int) -> None:
#     pass

# -----------------------------------------------------------------------------
# TODO 7: Counting Sort — O(n + k) time, O(k) space
# -----------------------------------------------------------------------------
# For integers in range [0, k]. Count occurrences, compute prefix sums,
# place elements in output array. Stable.
#
# def counting_sort(arr: List[int]) -> List[int]:
#     pass

# -----------------------------------------------------------------------------
# TODO 8: Sort Colors — LeetCode #75 (Dutch National Flag)
# -----------------------------------------------------------------------------
# Sort array containing only 0s, 1s, 2s in-place in one pass.
# Three-pointer approach: lo (0 boundary), mid (current), hi (2 boundary).
#
# def sort_colors(nums: List[int]) -> None:
#     pass

# -----------------------------------------------------------------------------
# TODO 9: Kth Largest Element — LeetCode #215
# -----------------------------------------------------------------------------
# Find the kth largest element without full sorting.
# Use Quickselect (partition-based) for average O(n).
# Or use a min-heap of size k for O(n log k).
#
# def find_kth_largest(nums: List[int], k: int) -> int:
#     pass

# -----------------------------------------------------------------------------
# TODO 10: Merge Intervals — LeetCode #56 (Blind 75)
# -----------------------------------------------------------------------------
# Merge all overlapping intervals. Sort by start time first.
#
# def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
#     pass
