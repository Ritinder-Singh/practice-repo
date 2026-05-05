# =============================================================================
# Autodesk Prep — Dynamic Programming (Days 9–10)
# =============================================================================
# Run: python 04_dp.py
# Framework: define STATE → TRANSITION → BASE CASE → direction
# =============================================================================


# =============================================================================
# DAY 9 — 1D DP
# =============================================================================

# LC 300 — Longest Increasing Subsequence  O(n log n) with patience sort
def length_of_lis(nums: list[int]) -> int:
    import bisect
    tails = []
    for n in nums:
        pos = bisect.bisect_left(tails, n)
        if pos == len(tails): tails.append(n)
        else: tails[pos] = n
    return len(tails)

# LC 139 — Word Break  O(n² * m)
# [Autodesk: tokenize AutoCAD command strings / script parser]
def word_break(s: str, word_dict: list[str]) -> bool:
    words = set(word_dict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[n]

# LC 91 — Decode Ways  O(n)
def num_decodings(s: str) -> int:
    if s[0] == "0": return 0
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        one = int(s[i-1])
        two = int(s[i-2:i])
        if one != 0: dp[i] += dp[i-1]
        if 10 <= two <= 26: dp[i] += dp[i-2]
    return dp[n]

# LC 322 — Coin Change  O(amount * len(coins))
def coin_change(coins: list[int], amount: int) -> int:
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return dp[amount] if dp[amount] != float("inf") else -1

# LC 213 — House Robber II (circular)  O(n)
def rob(nums: list[int]) -> int:
    def rob_linear(arr):
        a = b = 0
        for n in arr:
            a, b = b, max(b, a + n)
        return b
    if len(nums) == 1: return nums[0]
    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))


# =============================================================================
# DAY 10 — 2D DP + GRID
# =============================================================================

# LC 1143 — Longest Common Subsequence  O(m*n)
def lcs(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

# LC 72 — Edit Distance  O(m*n)
# [Autodesk: diff files in Autodesk Docs / version control]
def min_distance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    dp = list(range(n + 1))
    for i in range(1, m + 1):
        prev = dp[0]
        dp[0] = i
        for j in range(1, n + 1):
            temp = dp[j]
            if word1[i-1] == word2[j-1]:
                dp[j] = prev
            else:
                dp[j] = 1 + min(prev, dp[j], dp[j-1])
            prev = temp
    return dp[n]

# LC 221 — Maximal Square  O(m*n)
# [Autodesk: largest clear rectangular region in a 2D CAD grid/floor plan]
def maximal_square(matrix: list[list[str]]) -> int:
    rows, cols = len(matrix), len(matrix[0])
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]
    best = 0
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            if matrix[r-1][c-1] == "1":
                dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1
                best = max(best, dp[r][c])
    return best * best

# LC 62 — Unique Paths  O(m*n)
def unique_paths(m: int, n: int) -> int:
    dp = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j-1]
    return dp[n-1]

# LC 312 — Burst Balloons  O(n³)  Interval DP
def max_coins(nums: list[int]) -> int:
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n):
        for left in range(0, n - length):
            right = left + length
            for k in range(left + 1, right):
                dp[left][right] = max(
                    dp[left][right],
                    nums[left] * nums[k] * nums[right] + dp[left][k] + dp[k][right]
                )
    return dp[0][n-1]

# LC 97 — Interleaving String  O(m*n)
def is_interleave(s1: str, s2: str, s3: str) -> bool:
    m, n = len(s1), len(s2)
    if m + n != len(s3): return False
    dp = [False] * (n + 1)
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 and j == 0:
                dp[j] = True
            elif i == 0:
                dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
            elif j == 0:
                dp[j] = dp[j] and s1[i-1] == s3[i-1]
            else:
                dp[j] = (dp[j] and s1[i-1] == s3[i+j-1]) or \
                         (dp[j-1] and s2[j-1] == s3[i+j-1])
    return dp[n]


# =============================================================================
# TEST
# =============================================================================

if __name__ == "__main__":
    # Day 9
    assert length_of_lis([10,9,2,5,3,7,101,18]) == 4
    assert word_break("leetcode", ["leet","code"])
    assert not word_break("catsandog", ["cats","dog","sand","and","cat"])
    assert num_decodings("12") == 2
    assert num_decodings("226") == 3
    assert num_decodings("06") == 0
    assert coin_change([1,5,11], 11) == 1
    assert coin_change([2], 3) == -1
    assert rob([2,3,2]) == 3
    assert rob([1,2,3,1]) == 4

    # Day 10
    assert lcs("abcde", "ace") == 3
    assert lcs("abc", "abc") == 3
    assert min_distance("horse", "ros") == 3
    assert min_distance("intention", "execution") == 5
    assert maximal_square([["1","0","1","0"],["1","0","1","1"],["1","1","1","1"],["1","0","0","1"]]) == 4
    assert unique_paths(3, 7) == 28
    assert max_coins([3,1,5,8]) == 167
    assert is_interleave("aabcc", "dbbca", "aadbbcbcac")
    assert not is_interleave("aabcc", "dbbca", "aadbbbaccc")

    print("All Day 9–10 tests passed.")
