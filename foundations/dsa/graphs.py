# =============================================================================
# DSA Foundations — Graphs
# =============================================================================
# Topics: adjacency list/matrix, BFS, DFS, topological sort, cycle detection,
#         Dijkstra, Bellman-Ford, Union-Find, Prim's MST.
# Run: python graphs.py
# Ref: NeetCode 150 — Graphs section
# =============================================================================

from collections import defaultdict, deque
import heapq
from typing import List, Optional

# -----------------------------------------------------------------------------
# TODO 1: Build Graph Representations
# -----------------------------------------------------------------------------
# 1a: Build undirected adjacency list from edge list
#     Input: n=5, edges=[(0,1),(1,2),(2,3)]
#     Output: defaultdict where graph[0]=[1], graph[1]=[0,2], etc.
#
# def build_adj_list(n: int, edges: list) -> dict:
#     pass
#
# 1b: Build adjacency matrix (n x n)
#
# def build_adj_matrix(n: int, edges: list) -> List[List[int]]:
#     pass

# -----------------------------------------------------------------------------
# TODO 2: Number of Islands — LeetCode #200 (Blind 75)
# -----------------------------------------------------------------------------
# Count connected components of '1's in a 2D grid. Sink visited cells.
# Implement with DFS (recursive) and BFS.
#
# def num_islands(grid: List[List[str]]) -> int:
#     pass

# -----------------------------------------------------------------------------
# TODO 3: Clone Graph — LeetCode #133 (Blind 75)
# -----------------------------------------------------------------------------
# Deep-copy a graph. Use a hash map {original_node: cloned_node}.
# BFS or DFS both work.
#
# class Node:
#     def __init__(self, val=0, neighbors=None):
#         self.val = val
#         self.neighbors = neighbors or []
#
# def clone_graph(node: Optional[Node]) -> Optional[Node]:
#     pass

# -----------------------------------------------------------------------------
# TODO 4: Course Schedule — LeetCode #207 (Blind 75)
# -----------------------------------------------------------------------------
# Determine if you can finish all courses (no cycles in dependency graph).
# Model as directed graph, detect cycle using DFS states (0=unvisited, 1=visiting, 2=done).
#
# def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
#     pass

# -----------------------------------------------------------------------------
# TODO 5: Course Schedule II — LeetCode #210 (Blind 75)
# -----------------------------------------------------------------------------
# Return a valid course ordering, or [] if impossible (has cycle).
# Topological sort using Kahn's algorithm (BFS + in-degree).
#
# def find_order(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
#     pass

# -----------------------------------------------------------------------------
# TODO 6: Pacific Atlantic Water Flow — LeetCode #417 (Blind 75)
# -----------------------------------------------------------------------------
# Find cells from which water can flow to both Pacific and Atlantic oceans.
# BFS/DFS from ocean borders inward (reverse flow: go uphill).
#
# def pacific_atlantic(heights: List[List[int]]) -> List[List[int]]:
#     pass

# -----------------------------------------------------------------------------
# TODO 7: Union-Find (Disjoint Set Union) from Scratch
# -----------------------------------------------------------------------------
# Implement with path compression + union by rank.
#   find(x) -> int      (find root with path compression)
#   union(x, y) -> bool (merge sets, return True if they were different)
#   connected(x, y) -> bool
#
# class UnionFind:
#     def __init__(self, n: int):
#         self.parent = list(range(n))
#         self.rank = [0] * n

# -----------------------------------------------------------------------------
# TODO 8: Dijkstra's Shortest Path
# -----------------------------------------------------------------------------
# Single source shortest path for non-negative weighted graphs.
# Use min-heap (heapq). Return dict {node: min_distance}.
# Related: LeetCode #743 (Network Delay Time), #787 (Cheapest Flights K Stops).
#
# def dijkstra(graph: dict, src: int) -> dict:
#     # graph[u] = [(v, weight), ...]
#     pass

# -----------------------------------------------------------------------------
# TODO 9: Word Ladder — LeetCode #127 (Blind 75)
# -----------------------------------------------------------------------------
# Find shortest transformation sequence from beginWord to endWord.
# Each step changes one letter; each intermediate word must be in wordList.
# BFS on the word graph. Return length of shortest path, or 0 if impossible.
#
# def ladder_length(begin_word: str, end_word: str, word_list: List[str]) -> int:
#     pass

# -----------------------------------------------------------------------------
# TODO 10: Alien Dictionary — LeetCode #269 (Blind 75, Premium)
# -----------------------------------------------------------------------------
# Given sorted words in an alien language, determine the character order.
# Build a directed graph of character precedences, then topological sort.
# Return "" if invalid (cycle detected).
#
# def alien_order(words: List[str]) -> str:
#     pass
