# =============================================================================
# Python — Data Structures
# =============================================================================
# Topics: list, tuple, dict, set, deque, heapq, OrderedDict, Counter,
#         defaultdict, namedtuple, dataclass.
# Run: python 04_data_structures.py
# =============================================================================

from collections import deque, Counter, defaultdict, OrderedDict, namedtuple
from dataclasses import dataclass, field
import heapq
from typing import List

# TODO 1: List operations and time complexity
#   Know the Big-O for: append, pop, insert(0), delete by index, in-operator
#   Practice: rotate a list left by k positions WITHOUT slicing (in-place)
#
# def rotate_left(lst: list, k: int) -> None:
#     pass  # in-place, O(n)

# TODO 2: dict operations
#   TODO 2a: merge two dicts (prefer values from second dict on conflict)
#   TODO 2b: invert a dict {k: v} → {v: k} (handle duplicate values by storing list)
#   TODO 2c: deep merge two nested dicts
#
# def deep_merge(base: dict, override: dict) -> dict:
#     pass

# TODO 3: Counter
#   Given a string, use Counter to:
#   - Find most common 3 characters
#   - Find characters that appear exactly once
#   - Compute the difference between two Counters
#
# from collections import Counter
# text = "abracadabra"

# TODO 4: defaultdict
#   Group a list of (word, count) tuples by first letter using defaultdict(list):
#   Input: [("apple", 3), ("ant", 1), ("bear", 2)]
#   Output: {"a": [("apple",3), ("ant",1)], "b": [("bear",2)]}

# TODO 5: deque — implement a sliding window max tracker
#   Use deque as a monotonic queue to track maximum in O(1) amortized.
#   (Same as LeetCode #239 but implemented as a class)
#
# class SlidingWindowMax:
#     def __init__(self, k: int):
#         self.k = k
#         self.dq = deque()  # stores indices
#     def add(self, val: int, idx: int) -> int:
#         pass  # returns current max

# TODO 6: heapq — min-heap operations
#   TODO 6a: Find K largest elements using a min-heap of size K
#   TODO 6b: Merge K sorted lists using heapq.merge or manual heap
#   TODO 6c: Implement a priority queue with (priority, item) tuples
#
# def k_largest(nums: list, k: int) -> list:
#     pass

# TODO 7: dataclass
#   Define a Product dataclass with:
#   - name: str, price: float, tags: List[str] = field(default_factory=list)
#   - __post_init__ validation: price must be > 0
#   - Custom __str__ method
#   - frozen=True to make it hashable (for use in sets/dict keys)
#
# @dataclass(frozen=True)
# class Product:
#     name: str
#     price: float
#     tags: List[str] = field(default_factory=list)
#
#     def __post_init__(self):
#         pass
