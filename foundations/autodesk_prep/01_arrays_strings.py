# =============================================================================
# Autodesk Prep — Arrays, Strings, Intervals (Days 1–3)
# =============================================================================
# Run: python 01_arrays_strings.py
# =============================================================================

from collections import defaultdict, Counter
import heapq


# =============================================================================
# DAY 1 — ARRAYS & TWO POINTERS
# =============================================================================

# LC 238 — Product of Array Except Self  O(n) time, O(1) extra space
def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    out = [1] * n
    prefix = 1
    for i in range(n):
        out[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        out[i] *= suffix
        suffix *= nums[i]
    return out

# LC 53 — Maximum Subarray (Kadane's)  O(n)
def max_subarray(nums: list[int]) -> int:
    best = cur = nums[0]
    for n in nums[1:]:
        cur = max(n, cur + n)
        best = max(best, cur)
    return best

# LC 15 — 3Sum  O(n²)
def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    res = []
    for i, n in enumerate(nums):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = n + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                res.append([n, nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]: l += 1
                while l < r and nums[r] == nums[r - 1]: r -= 1
                l += 1; r -= 1
    return res

# LC 42 — Trapping Rain Water  O(n)  [Autodesk: 2D terrain/elevation profile]
def trap(height: list[int]) -> int:
    l, r = 0, len(height) - 1
    max_l = max_r = water = 0
    while l < r:
        if height[l] < height[r]:
            if height[l] >= max_l: max_l = height[l]
            else: water += max_l - height[l]
            l += 1
        else:
            if height[r] >= max_r: max_r = height[r]
            else: water += max_r - height[r]
            r -= 1
    return water

# LC 48 — Rotate Image 90° clockwise  O(n²)  [Autodesk: matrix transform]
def rotate(matrix: list[list[int]]) -> None:
    n = len(matrix)
    # Step 1: transpose
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Step 2: reverse each row
    for row in matrix:
        row.reverse()


# =============================================================================
# DAY 2 — SLIDING WINDOW + INTERVALS
# =============================================================================

# LC 3 — Longest Substring Without Repeating  O(n)
def length_of_longest_substring(s: str) -> int:
    seen = {}
    best = l = 0
    for r, ch in enumerate(s):
        if ch in seen and seen[ch] >= l:
            l = seen[ch] + 1
        seen[ch] = r
        best = max(best, r - l + 1)
    return best

# LC 76 — Minimum Window Substring  O(n)
def min_window(s: str, t: str) -> str:
    if not t: return ""
    need = Counter(t)
    have, total = 0, len(need)
    window = {}
    best = (float("inf"), 0, 0)
    l = 0
    for r, ch in enumerate(s):
        window[ch] = window.get(ch, 0) + 1
        if ch in need and window[ch] == need[ch]:
            have += 1
        while have == total:
            if (r - l + 1) < best[0]:
                best = (r - l + 1, l, r)
            window[s[l]] -= 1
            if s[l] in need and window[s[l]] < need[s[l]]:
                have -= 1
            l += 1
    return s[best[1]: best[2] + 1] if best[0] != float("inf") else ""

# LC 56 — Merge Intervals  O(n log n)  [Autodesk: BIM construction scheduling]
def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort()
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged

# LC 57 — Insert Interval  O(n)
def insert_interval(intervals: list[list[int]], new: list[int]) -> list[list[int]]:
    res = []
    for i, (s, e) in enumerate(intervals):
        if new[1] < s:
            res.append(new)
            return res + intervals[i:]
        elif new[0] > e:
            res.append([s, e])
        else:
            new = [min(new[0], s), max(new[1], e)]
    res.append(new)
    return res

# LC 253 — Meeting Rooms II  O(n log n)  [Autodesk: cloud resource allocation]
def min_meeting_rooms(intervals: list[list[int]]) -> int:
    if not intervals: return 0
    intervals.sort()
    heap = []  # end times of active meetings
    for start, end in intervals:
        if heap and heap[0] <= start:
            heapq.heapreplace(heap, end)
        else:
            heapq.heappush(heap, end)
    return len(heap)


# =============================================================================
# DAY 3 — STRINGS + HASHING
# =============================================================================

# LC 49 — Group Anagrams  O(n * k log k)
def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups = defaultdict(list)
    for s in strs:
        groups[tuple(sorted(s))].append(s)
    return list(groups.values())

# LC 424 — Longest Repeating Character Replacement  O(n)
def character_replacement(s: str, k: int) -> int:
    count = {}
    best = l = max_count = 0
    for r, ch in enumerate(s):
        count[ch] = count.get(ch, 0) + 1
        max_count = max(max_count, count[ch])
        while (r - l + 1) - max_count > k:
            count[s[l]] -= 1
            l += 1
        best = max(best, r - l + 1)
    return best

# LC 271 — Encode/Decode Strings  [Autodesk: file format serialization]
def encode(strs: list[str]) -> str:
    return "".join(f"{len(s)}#{s}" for s in strs)

def decode(s: str) -> list[str]:
    res, i = [], 0
    while i < len(s):
        j = s.index("#", i)
        length = int(s[i:j])
        res.append(s[j + 1: j + 1 + length])
        i = j + 1 + length
    return res

# LC 5 — Longest Palindromic Substring  O(n²)
def longest_palindrome(s: str) -> str:
    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l + 1: r]
    best = ""
    for i in range(len(s)):
        for start in [expand(i, i), expand(i, i + 1)]:
            if len(start) > len(best):
                best = start
    return best

# LC 394 — Decode String  O(n)  [Autodesk: macro/script parsing in AutoCAD]
def decode_string(s: str) -> str:
    stack = []
    cur_str = ""
    cur_num = 0
    for ch in s:
        if ch.isdigit():
            cur_num = cur_num * 10 + int(ch)
        elif ch == "[":
            stack.append((cur_str, cur_num))
            cur_str, cur_num = "", 0
        elif ch == "]":
            prev_str, num = stack.pop()
            cur_str = prev_str + cur_str * num
        else:
            cur_str += ch
    return cur_str


# =============================================================================
# TEST
# =============================================================================

if __name__ == "__main__":
    # Day 1
    assert product_except_self([1,2,3,4]) == [24,12,8,6]
    assert max_subarray([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert sorted(map(sorted, three_sum([-1,0,1,2,-1,-4]))) == [[-1,-1,2],[-1,0,1]]
    assert trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    m = [[1,2,3],[4,5,6],[7,8,9]]; rotate(m); assert m == [[7,4,1],[8,5,2],[9,6,3]]

    # Day 2
    assert length_of_longest_substring("abcabcbb") == 3
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
    assert merge_intervals([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert insert_interval([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]]
    assert min_meeting_rooms([[0,30],[5,10],[15,20]]) == 2

    # Day 3
    assert sorted(map(sorted, group_anagrams(["eat","tea","tan","ate","nat","bat"]))) == [['ate', 'eat', 'tea'], ['bat'], ['nat', 'tan']]
    assert character_replacement("AABABBA", 1) == 4
    assert decode(encode(["hello","world"])) == ["hello","world"]
    assert longest_palindrome("babad") in ("bab", "aba")
    assert decode_string("3[a]2[bc]") == "aaabcbc"
    assert decode_string("3[a2[c]]") == "accaccacc"

    print("All Day 1-3 tests passed.")
