# =============================================================================
# DSA Foundations — Hash Maps & Hash Sets
# =============================================================================
# Topics: hash map from scratch (open addressing & chaining), anagram grouping,
#         frequency counting, top-K elements, union/intersection.
# Run: python hash_map.py
# Ref: NeetCode 150 — Arrays & Hashing section
# =============================================================================

from collections import Counter, defaultdict
from typing import List

# -----------------------------------------------------------------------------
# TODO 1: Implement Hash Map from Scratch (Separate Chaining)
# -----------------------------------------------------------------------------
# Build a HashMap class with dynamic resizing (resize when load > 0.75).
# Use an array of linked list buckets for collision handling.
#   put(key, val)
#   get(key) -> val or None
#   remove(key)
#   contains(key) -> bool
#   size() -> int
#
# class HashMap:
#     def __init__(self, initial_capacity=16):
#         self._buckets = [[] for _ in range(initial_capacity)]
#         self._size = 0
#         self._capacity = initial_capacity
#
#     def _hash(self, key) -> int:
#         return hash(key) % self._capacity

# -----------------------------------------------------------------------------
# TODO 2: Valid Anagram — LeetCode #242 (Blind 75)
# -----------------------------------------------------------------------------
# Return True if t is an anagram of s (same characters, same frequencies).
# Solve using a frequency counter (dict or Counter). O(n).
#
# def is_anagram(s: str, t: str) -> bool:
#     pass

# -----------------------------------------------------------------------------
# TODO 3: Group Anagrams — LeetCode #49 (Blind 75)
# -----------------------------------------------------------------------------
# Group strings that are anagrams of each other.
# Key: sorted string (or tuple of 26 char counts). Value: list of strings.
#
# def group_anagrams(strs: List[str]) -> List[List[str]]:
#     pass

# -----------------------------------------------------------------------------
# TODO 4: Top K Frequent Elements — LeetCode #347 (Blind 75)
# -----------------------------------------------------------------------------
# Return the k most frequent elements. O(n) using bucket sort (freq as index).
# Alternative: use a heap for O(n log k).
#
# def top_k_frequent(nums: List[int], k: int) -> List[int]:
#     pass

# -----------------------------------------------------------------------------
# TODO 5: Encode and Decode Strings — LeetCode #271 (Blind 75)
# -----------------------------------------------------------------------------
# Design encode(strs) -> str and decode(s) -> List[str].
# Handle strings containing any character including the delimiter.
# Use length-prefix encoding: "4#word4#test"
#
# def encode(strs: List[str]) -> str:
#     pass
#
# def decode(s: str) -> List[str]:
#     pass

# -----------------------------------------------------------------------------
# TODO 6: Longest Consecutive Sequence — LeetCode #128 (Blind 75)
# -----------------------------------------------------------------------------
# Find the length of the longest consecutive integer sequence.
# Convert to a set. For each num that is a sequence start (num-1 not in set),
# count forward. O(n).
#
# def longest_consecutive(nums: List[int]) -> int:
#     pass

# -----------------------------------------------------------------------------
# TODO 7: Two Sum (all pairs) — Extension of LeetCode #1
# -----------------------------------------------------------------------------
# Return ALL pairs of indices (i, j) where i < j and nums[i] + nums[j] == target.
# (LeetCode #1 guarantees one solution; this extension finds all.)
#
# def two_sum_all(nums: List[int], target: int) -> List[List[int]]:
#     pass

# -----------------------------------------------------------------------------
# TODO 8: Subarray Sum Equals K — LeetCode #560
# -----------------------------------------------------------------------------
# Count the number of contiguous subarrays that sum to k.
# Use prefix sum + hash map. O(n).
# Key insight: if prefix[j] - prefix[i] == k, then subarray [i+1..j] sums to k.
#
# def subarray_sum(nums: List[int], k: int) -> int:
#     pass
