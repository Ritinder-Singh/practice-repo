# =============================================================================
# Autodesk Prep — Linked Lists, Stack, Queue (Day 4)
# =============================================================================
# Run: python 02_linked_lists_stack.py
# =============================================================================

from collections import deque
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def to_list(head: Optional[ListNode]) -> list:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

def from_list(vals: list) -> Optional[ListNode]:
    dummy = ListNode(0)
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


# =============================================================================
# LC 143 — Reorder List  O(n)
# Split → reverse second half → merge alternating
# =============================================================================
def reorder_list(head: Optional[ListNode]) -> None:
    if not head or not head.next:
        return
    # Find mid
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # Reverse second half
    prev, cur = None, slow.next
    slow.next = None
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    # Merge
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2


# =============================================================================
# LC 146 — LRU Cache  O(1) get/put
# [Autodesk: cache frequently accessed 3D assets / geometry data]
# Uses doubly-linked list + hashmap
# =============================================================================
class LRUCache:
    class _Node:
        def __init__(self, key=0, val=0):
            self.key = key; self.val = val
            self.prev = self.next = None

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache: dict[int, LRUCache._Node] = {}
        self.head = self._Node()   # least recently used end
        self.tail = self._Node()   # most recently used end
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_tail(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._insert_tail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = self._Node(key, value)
        self.cache[key] = node
        self._insert_tail(node)
        if len(self.cache) > self.cap:
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]


# =============================================================================
# LC 739 — Daily Temperatures  O(n)  Monotonic stack
# Pattern: "next greater element" — appears in many Autodesk variants
# =============================================================================
def daily_temperatures(temps: list[int]) -> list[int]:
    res = [0] * len(temps)
    stack = []  # indices of decreasing temps
    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            j = stack.pop()
            res[j] = i - j
        stack.append(i)
    return res


# =============================================================================
# LC 84 — Largest Rectangle in Histogram  O(n)  Monotonic stack
# [Autodesk: cross-sectional area computation in CAD profiles]
# =============================================================================
def largest_rectangle_area(heights: list[int]) -> int:
    stack = []  # (index, height) of increasing heights
    max_area = 0
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            idx, height = stack.pop()
            max_area = max(max_area, height * (i - idx))
            start = idx
        stack.append((start, h))
    for idx, height in stack:
        max_area = max(max_area, height * (len(heights) - idx))
    return max_area


# =============================================================================
# LC 20 — Valid Parentheses  O(n)
# [Autodesk: expression/formula validation in spreadsheet cells]
# =============================================================================
def is_valid_parens(s: str) -> bool:
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif not stack or stack[-1] != pairs[ch]:
            return False
        else:
            stack.pop()
    return not stack


# =============================================================================
# LC 155 — Min Stack  O(1) all ops
# =============================================================================
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        cur_min = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(cur_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def get_min(self) -> int:
        return self.min_stack[-1]


# =============================================================================
# BONUS: Sliding Window Maximum  LC 239  O(n)
# Monotonic deque — useful for streaming max in real-time telemetry
# =============================================================================
def max_sliding_window(nums: list[int], k: int) -> list[int]:
    dq = deque()  # stores indices, front is always the max
    res = []
    for i, n in enumerate(nums):
        while dq and nums[dq[-1]] <= n:
            dq.pop()
        dq.append(i)
        if dq[0] < i - k + 1:
            dq.popleft()
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res


# =============================================================================
# TEST
# =============================================================================

if __name__ == "__main__":
    # Reorder list
    head = from_list([1,2,3,4,5]); reorder_list(head)
    assert to_list(head) == [1,5,2,4,3]

    # LRU Cache
    lru = LRUCache(2)
    lru.put(1, 1); lru.put(2, 2)
    assert lru.get(1) == 1
    lru.put(3, 3)               # evicts key 2
    assert lru.get(2) == -1
    lru.put(4, 4)               # evicts key 1
    assert lru.get(1) == -1
    assert lru.get(3) == 3
    assert lru.get(4) == 4

    # Daily temps
    assert daily_temperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]

    # Largest rectangle
    assert largest_rectangle_area([2,1,5,6,2,3]) == 10

    # Valid parens
    assert is_valid_parens("()[]{}")
    assert not is_valid_parens("(]")

    # Min stack
    ms = MinStack()
    ms.push(-2); ms.push(0); ms.push(-3)
    assert ms.get_min() == -3
    ms.pop()
    assert ms.top() == 0
    assert ms.get_min() == -2

    # Sliding window max
    assert max_sliding_window([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]

    print("All Day 4 tests passed.")
