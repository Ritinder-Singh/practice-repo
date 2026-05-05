# =============================================================================
# Autodesk Prep — Trees & Graphs (Days 5–8)
# =============================================================================
# Run: python 03_trees_graphs.py
# Key Autodesk relevance: scene graphs, BIM model hierarchy, plugin dependency
# =============================================================================

from collections import deque, defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

def make_tree(vals: list) -> Optional[TreeNode]:
    """BFS-insert from level-order list (None = missing node)."""
    if not vals: return None
    root = TreeNode(vals[0])
    q = deque([root])
    i = 1
    while q and i < len(vals):
        node = q.popleft()
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i]); q.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i]); q.append(node.right)
        i += 1
    return root


# =============================================================================
# DAY 5 — BINARY TREES BASICS
# =============================================================================

# LC 543 — Diameter of Binary Tree  O(n)
def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    best = [0]
    def depth(node):
        if not node: return 0
        l, r = depth(node.left), depth(node.right)
        best[0] = max(best[0], l + r)
        return 1 + max(l, r)
    depth(root)
    return best[0]

# LC 102 — Level Order Traversal  O(n)
def level_order(root: Optional[TreeNode]) -> list[list[int]]:
    if not root: return []
    res, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:  q.append(node.left)
            if node.right: q.append(node.right)
        res.append(level)
    return res

# LC 199 — Right Side View  O(n)
def right_side_view(root: Optional[TreeNode]) -> list[int]:
    if not root: return []
    res, q = [], deque([root])
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if i == 0: res.append(node.val)  # rightmost = first popped if reversed... use last
            if node.left:  q.append(node.left)
            if node.right: q.append(node.right)
        res[-1] = node.val  # last node at level = rightmost
    return res

# LC 1448 — Count Good Nodes  O(n)
def good_nodes(root: TreeNode) -> int:
    def dfs(node, max_so_far):
        if not node: return 0
        good = 1 if node.val >= max_so_far else 0
        m = max(max_so_far, node.val)
        return good + dfs(node.left, m) + dfs(node.right, m)
    return dfs(root, root.val)


# =============================================================================
# DAY 6 — BINARY TREES ADVANCED + BST
# =============================================================================

# LC 105 — Construct from Preorder + Inorder  O(n)
# [Autodesk: scene graph reconstruction from serialized file]
def build_tree(preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
    if not preorder: return None
    root_val = preorder[0]
    mid = inorder.index(root_val)
    root = TreeNode(root_val)
    root.left  = build_tree(preorder[1: mid + 1], inorder[:mid])
    root.right = build_tree(preorder[mid + 1:], inorder[mid + 1:])
    return root

# LC 124 — Binary Tree Maximum Path Sum  O(n)
def max_path_sum(root: Optional[TreeNode]) -> int:
    best = [float("-inf")]
    def dfs(node):
        if not node: return 0
        l = max(dfs(node.left),  0)
        r = max(dfs(node.right), 0)
        best[0] = max(best[0], node.val + l + r)
        return node.val + max(l, r)
    dfs(root)
    return best[0]

# LC 297 — Serialize / Deserialize Binary Tree  O(n)
# [Autodesk: save/load 3D scene hierarchy to disk]
class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node):
            if not node: res.append("N"); return
            res.append(str(node.val))
            dfs(node.left); dfs(node.right)
        dfs(root)
        return ",".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = iter(data.split(","))
        def dfs():
            v = next(vals)
            if v == "N": return None
            node = TreeNode(int(v))
            node.left  = dfs()
            node.right = dfs()
            return node
        return dfs()

# LC 98 — Validate BST  O(n)
def is_valid_bst(root: Optional[TreeNode]) -> bool:
    def dfs(node, lo, hi):
        if not node: return True
        if not (lo < node.val < hi): return False
        return dfs(node.left, lo, node.val) and dfs(node.right, node.val, hi)
    return dfs(root, float("-inf"), float("inf"))

# LC 235 — LCA of BST  O(h)  [Autodesk: find shared ancestor in scene hierarchy]
def lowest_common_ancestor_bst(root, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root

# LC 230 — Kth Smallest in BST  O(h + k)
def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    stack, cur = [], root
    while stack or cur:
        while cur:
            stack.append(cur); cur = cur.left
        cur = stack.pop()
        k -= 1
        if k == 0: return cur.val
        cur = cur.right


# =============================================================================
# DAY 7 — GRAPHS: BFS / DFS
# =============================================================================

# LC 200 — Number of Islands  O(m*n)
def num_islands(grid: list[list[str]]) -> int:
    if not grid: return 0
    rows, cols = len(grid), len(grid[0])
    count = 0
    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != "1": return
        grid[r][c] = "0"
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            dfs(r + dr, c + dc)
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                dfs(r, c); count += 1
    return count

# LC 417 — Pacific Atlantic Water Flow  O(m*n)
def pacific_atlantic(heights: list[list[int]]) -> list[list[int]]:
    rows, cols = len(heights), len(heights[0])
    pac, atl = set(), set()
    def bfs(starts, visited):
        q = deque(starts)
        visited.update(starts)
        while q:
            r, c = q.popleft()
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited \
                   and heights[nr][nc] >= heights[r][c]:
                    visited.add((nr, nc)); q.append((nr, nc))
    bfs([(r, 0) for r in range(rows)] + [(0, c) for c in range(cols)], pac)
    bfs([(r, cols-1) for r in range(rows)] + [(rows-1, c) for c in range(cols)], atl)
    return [[r, c] for r, c in pac & atl]

# LC 994 — Rotting Oranges  O(m*n)  Multi-source BFS
def oranges_rotting(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    q = deque()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2: q.append((r, c, 0))
            elif grid[r][c] == 1: fresh += 1
    time = 0
    while q:
        r, c, t = q.popleft()
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2; fresh -= 1; time = t + 1
                q.append((nr, nc, t + 1))
    return time if fresh == 0 else -1


# =============================================================================
# DAY 8 — GRAPHS: TOPOLOGICAL SORT + UNION-FIND
# =============================================================================

# LC 207 — Course Schedule (cycle detection)  O(V+E)
# [Autodesk: plugin dependency validation in AutoCAD/Revit extension system]
def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    adj = defaultdict(list)
    for a, b in prerequisites:
        adj[b].append(a)
    # 0=unvisited, 1=visiting, 2=done
    state = [0] * num_courses
    def dfs(node):
        if state[node] == 1: return False  # cycle
        if state[node] == 2: return True
        state[node] = 1
        for nei in adj[node]:
            if not dfs(nei): return False
        state[node] = 2
        return True
    return all(dfs(i) for i in range(num_courses))

# LC 210 — Course Schedule II (topological order)  O(V+E)
def find_order(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    adj = defaultdict(list)
    indegree = [0] * num_courses
    for a, b in prerequisites:
        adj[b].append(a); indegree[a] += 1
    q = deque(i for i in range(num_courses) if indegree[i] == 0)
    order = []
    while q:
        node = q.popleft(); order.append(node)
        for nei in adj[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0: q.append(nei)
    return order if len(order) == num_courses else []

# LC 684 — Redundant Connection (Union-Find)  O(n * α(n))
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank   = [0] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # path compression
            x = self.parent[x]
        return x

    def union(self, x, y) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py: return False  # already connected → cycle
        if self.rank[px] < self.rank[py]: px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]: self.rank[px] += 1
        return True

def find_redundant_connection(edges: list[list[int]]) -> list[int]:
    uf = UnionFind(len(edges) + 1)
    for u, v in edges:
        if not uf.union(u, v):
            return [u, v]

# LC 323 — Number of Connected Components  O(n + e)
def count_components(n: int, edges: list[list[int]]) -> int:
    uf = UnionFind(n)
    for u, v in edges:
        uf.union(u, v)
    return len({uf.find(i) for i in range(n)})


# =============================================================================
# TEST
# =============================================================================

if __name__ == "__main__":
    # Day 5
    root = make_tree([1,2,3,4,5])
    assert diameter_of_binary_tree(root) == 3
    assert level_order(root) == [[1],[2,3],[4,5]]
    assert good_nodes(make_tree([3,1,4,3,None,1,5])) == 4

    # Day 6
    preorder = [3,9,20,15,7]; inorder = [9,3,15,20,7]
    tree = build_tree(preorder, inorder)
    assert level_order(tree) == [[3],[9,20],[15,7]]
    assert max_path_sum(make_tree([-3])) == -3
    assert max_path_sum(make_tree([1,2,3])) == 6
    codec = Codec()
    root = make_tree([1,2,3,None,None,4,5])
    assert codec.serialize(codec.deserialize(codec.serialize(root))) == codec.serialize(root)
    assert is_valid_bst(make_tree([2,1,3]))
    assert not is_valid_bst(make_tree([5,1,4,None,None,3,6]))
    assert kth_smallest(make_tree([3,1,4,None,2]), 1) == 1

    # Day 7
    grid = [["1","1","0"],["0","1","0"],["0","0","1"]]
    assert num_islands(grid) == 2
    assert oranges_rotting([[2,1,1],[1,1,0],[0,1,1]]) == 4
    assert oranges_rotting([[0,2]]) == 0

    # Day 8
    assert can_finish(2, [[1,0]])
    assert not can_finish(2, [[1,0],[0,1]])
    assert find_order(4, [[1,0],[2,0],[3,1],[3,2]]) in [[0,1,2,3],[0,2,1,3]]
    assert find_redundant_connection([[1,2],[1,3],[2,3]]) == [2,3]
    assert count_components(5, [[0,1],[1,2],[3,4]]) == 2

    print("All Day 5–8 tests passed.")
