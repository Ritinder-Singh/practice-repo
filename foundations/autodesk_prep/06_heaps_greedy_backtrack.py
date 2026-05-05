# =============================================================================
# Autodesk Prep — Heaps, Greedy, Backtracking (Days 12–13)
# =============================================================================
# Run: python 06_heaps_greedy_backtrack.py
# =============================================================================

import heapq
from collections import Counter, OrderedDict


# =============================================================================
# DAY 12 — HEAPS + GREEDY
# =============================================================================

# LC 215 — Kth Largest Element  O(n log k) heap  /  O(n) avg quickselect
def find_kth_largest(nums: list[int], k: int) -> int:
    heap = []
    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]

# LC 347 — Top K Frequent Elements  O(n log k)
def top_k_frequent(nums: list[int], k: int) -> list[int]:
    count = Counter(nums)
    return [x for x, _ in count.most_common(k)]

# LC 295 — Find Median from Data Stream  O(log n) add, O(1) find
# [Autodesk: real-time analytics on streaming telemetry / render times]
class MedianFinder:
    def __init__(self):
        self.small = []  # max-heap (negated) — stores lower half
        self.large = []  # min-heap — stores upper half

    def add_num(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        # Ensure max(small) <= min(large)
        if self.large and -self.small[0] > self.large[0]:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        # Balance sizes: small can be at most 1 larger
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def find_median(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2

# LC 621 — Task Scheduler  O(n log n)
# [Autodesk: render farm job scheduling with cooldown constraints]
def least_interval(tasks: list[str], n: int) -> int:
    count = Counter(tasks)
    heap = [-c for c in count.values()]
    heapq.heapify(heap)
    time = 0
    queue = []  # (available_at_time, count)
    while heap or queue:
        time += 1
        if heap:
            cnt = heapq.heappop(heap) + 1  # use one task
            if cnt:
                queue.append((time + n, cnt))
        if queue and queue[0][0] == time:
            heapq.heappush(heap, queue.pop(0)[1])
    return time

# LC 45 — Jump Game II  O(n) Greedy BFS
def jump(nums: list[int]) -> int:
    jumps = cur_end = far = 0
    for i in range(len(nums) - 1):
        far = max(far, i + nums[i])
        if i == cur_end:
            jumps += 1
            cur_end = far
    return jumps

# LC 134 — Gas Station  O(n)
def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    if sum(gas) < sum(cost): return -1
    tank = start = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            tank = 0
            start = i + 1
    return start

# LC 846 — Hand of Straights  O(n log n)
def is_n_straight_hand(hand: list[int], group_size: int) -> bool:
    if len(hand) % group_size: return False
    count = Counter(hand)
    for card in sorted(count):
        if count[card] > 0:
            n = count[card]
            for i in range(group_size):
                if count[card + i] < n: return False
                count[card + i] -= n
    return True


# =============================================================================
# DAY 13 — BACKTRACKING + HARD
# =============================================================================

# LC 39 — Combination Sum  O(2^t * k)  [t = target/min_coin, k = combo length]
def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    res = []
    def backtrack(start, combo, remaining):
        if remaining == 0:
            res.append(combo[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining: break
            combo.append(candidates[i])
            backtrack(i, combo, remaining - candidates[i])
            combo.pop()
    candidates.sort()
    backtrack(0, [], target)
    return res

# LC 90 — Subsets II (with duplicates)  O(2^n)
def subsets_with_dup(nums: list[int]) -> list[list[int]]:
    res = []
    nums.sort()
    def backtrack(start, subset):
        res.append(subset[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]: continue
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
    backtrack(0, [])
    return res

# LC 79 — Word Search  O(m*n*4^L)
# [Autodesk: 2D grid path search in floor plan / CAD layer grid]
def word_search(board: list[list[str]], word: str) -> bool:
    rows, cols = len(board), len(board[0])
    visited = set()
    def dfs(r, c, i):
        if i == len(word): return True
        if r < 0 or c < 0 or r >= rows or c >= cols: return False
        if board[r][c] != word[i] or (r, c) in visited: return False
        visited.add((r, c))
        found = any(dfs(r+dr, c+dc, i+1) for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)])
        visited.remove((r, c))
        return found
    return any(dfs(r, c, 0) for r in range(rows) for c in range(cols))

# LC 51 — N-Queens  O(n!)
def solve_n_queens(n: int) -> list[list[str]]:
    res = []
    cols = set(); pos_diag = set(); neg_diag = set()
    board = [["."] * n for _ in range(n)]
    def backtrack(row):
        if row == n:
            res.append(["".join(r) for r in board])
            return
        for col in range(n):
            if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                continue
            cols.add(col); pos_diag.add(row+col); neg_diag.add(row-col)
            board[row][col] = "Q"
            backtrack(row + 1)
            cols.remove(col); pos_diag.remove(row+col); neg_diag.remove(row-col)
            board[row][col] = "."
    backtrack(0)
    return res

# LC 4 — Median of Two Sorted Arrays  O(log(min(m,n)))
def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    m, n = len(nums1), len(nums2)
    lo, hi = 0, m
    while lo <= hi:
        i = (lo + hi) // 2
        j = (m + n + 1) // 2 - i
        max_l1 = float("-inf") if i == 0 else nums1[i-1]
        min_r1 = float("inf")  if i == m else nums1[i]
        max_l2 = float("-inf") if j == 0 else nums2[j-1]
        min_r2 = float("inf")  if j == n else nums2[j]
        if max_l1 <= min_r2 and max_l2 <= min_r1:
            if (m + n) % 2: return float(max(max_l1, max_l2))
            return (max(max_l1, max_l2) + min(min_r1, min_r2)) / 2
        elif max_l1 > min_r2:
            hi = i - 1
        else:
            lo = i + 1


# =============================================================================
# TEST
# =============================================================================

if __name__ == "__main__":
    # Heaps + Greedy
    assert find_kth_largest([3,2,1,5,6,4], 2) == 5
    assert find_kth_largest([3,2,3,1,2,4,5,5,6], 4) == 4
    assert sorted(top_k_frequent([1,1,1,2,2,3], 2)) == [1, 2]

    mf = MedianFinder()
    for n in [1, 2]: mf.add_num(n)
    assert mf.find_median() == 1.5
    mf.add_num(3)
    assert mf.find_median() == 2.0

    assert least_interval(list("AAABBB"), 2) == 8
    assert jump([2,3,1,1,4]) == 2
    assert jump([2,3,0,1,4]) == 2
    assert can_complete_circuit([1,2,3,4,5],[3,4,5,1,2]) == 3
    assert can_complete_circuit([2,3,4],[3,4,3]) == -1
    assert is_n_straight_hand([1,2,3,6,2,3,4,7,8], 3)
    assert not is_n_straight_hand([1,2,3,4,5], 4)

    # Backtracking
    result = combination_sum([2,3,6,7], 7)
    assert sorted(map(sorted, result)) == [[2,2,3],[7]]
    assert len(subsets_with_dup([1,2,2])) == 6
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    assert word_search([row[:] for row in board], "ABCCED")
    assert not word_search([row[:] for row in board], "ABCB")
    queens = solve_n_queens(4)
    assert len(queens) == 2
    assert find_median_sorted_arrays([1,3],[2]) == 2.0
    assert find_median_sorted_arrays([1,2],[3,4]) == 2.5

    print("All Day 12–13 tests passed.")
