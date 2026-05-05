# =============================================================================
# Autodesk Prep — Geometry & Math (Day 11)
# =============================================================================
# Run: python 05_geometry_math.py
# Autodesk makes AutoCAD, Maya, Fusion 360 — geometry problems are on-brand
# =============================================================================

from math import gcd, sqrt, inf
import heapq


# =============================================================================
# LC 973 — K Closest Points to Origin  O(n log k)
# [Autodesk: 3D spatial query — find k nearest control points in a CAD model]
# =============================================================================
def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    # Max-heap of size k (negate distance for max-heap behavior)
    heap = []
    for x, y in points:
        dist = -(x*x + y*y)
        if len(heap) < k:
            heapq.heappush(heap, (dist, x, y))
        elif dist > heap[0][0]:
            heapq.heapreplace(heap, (dist, x, y))
    return [[x, y] for _, x, y in heap]


# =============================================================================
# LC 149 — Max Points on a Line  O(n²)
# [Autodesk: line detection in 2D/3D CAD point sets]
# Key insight: represent slope as reduced fraction (dy/gcd, dx/gcd) to avoid float errors
# =============================================================================
def max_points_on_line(points: list[list[int]]) -> int:
    if len(points) <= 2: return len(points)
    best = 0
    for i in range(len(points)):
        slopes = {}
        for j in range(i + 1, len(points)):
            dx = points[j][0] - points[i][0]
            dy = points[j][1] - points[i][1]
            if dx == 0:
                key = (0, 1)      # vertical line
            else:
                g = gcd(abs(dx), abs(dy))
                # Normalize sign to dx positive
                if dx < 0: dx, dy = -dx, -dy
                key = (dx // g, dy // g)
            slopes[key] = slopes.get(key, 0) + 1
            best = max(best, slopes[key] + 1)  # +1 for point i itself
    return best


# =============================================================================
# LC 593 — Valid Square  O(1)
# [Autodesk: validate rectangular constraints in 2D CAD shapes]
# =============================================================================
def valid_square(p1, p2, p3, p4) -> bool:
    def dist_sq(a, b):
        return (a[0]-b[0])**2 + (a[1]-b[1])**2

    pts = [p1, p2, p3, p4]
    dists = sorted(
        dist_sq(pts[i], pts[j])
        for i in range(4) for j in range(i+1, 4)
    )
    # Valid square: 4 equal sides + 2 equal diagonals, all > 0
    return (dists[0] > 0 and
            dists[0] == dists[1] == dists[2] == dists[3] and
            dists[4] == dists[5])


# =============================================================================
# LC 939 — Minimum Area Rectangle  O(n²)
# [Autodesk: find bounding rectangles in 2D floor plan point sets]
# Key insight: for each pair of points as diagonal, check if other 2 corners exist
# =============================================================================
def min_area_rect(points: list[list[int]]) -> int:
    point_set = {(x, y) for x, y in points}
    min_area = inf
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]
            if x1 != x2 and y1 != y2:  # not same row/col (would be degenerate)
                if (x1, y2) in point_set and (x2, y1) in point_set:
                    area = abs(x2 - x1) * abs(y2 - y1)
                    min_area = min(min_area, area)
    return 0 if min_area == inf else min_area


# =============================================================================
# LC 54 — Spiral Matrix  O(m*n)
# [Autodesk: raster scan order for image/texture processing in 3D rendering]
# =============================================================================
def spiral_order(matrix: list[list[int]]) -> list[int]:
    res = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for c in range(left, right + 1): res.append(matrix[top][c])
        top += 1
        for r in range(top, bottom + 1): res.append(matrix[r][right])
        right -= 1
        if top <= bottom:
            for c in range(right, left - 1, -1): res.append(matrix[bottom][c])
            bottom -= 1
        if left <= right:
            for r in range(bottom, top - 1, -1): res.append(matrix[r][left])
            left += 1
    return res


# =============================================================================
# LC 74 — Search a 2D Matrix  O(log(m*n))
# [Autodesk: binary search in sorted 2D CAD lookup table / material DB]
# =============================================================================
def search_matrix(matrix: list[list[int]], target: int) -> bool:
    rows, cols = len(matrix), len(matrix[0])
    lo, hi = 0, rows * cols - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        val = matrix[mid // cols][mid % cols]
        if val == target: return True
        if val < target: lo = mid + 1
        else: hi = mid - 1
    return False


# =============================================================================
# BONUS — Geometry Utilities (useful for Autodesk geometry discussions)
# =============================================================================

def cross_product_2d(o, a, b) -> float:
    """Cross product of vectors OA and OB. + = left turn, - = right turn, 0 = collinear."""
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def convex_hull(points: list[list[int]]) -> list[list[int]]:
    """Andrew's monotone chain — O(n log n). Returns hull in CCW order."""
    points = sorted(map(tuple, points))
    def build(pts):
        hull = []
        for p in pts:
            while len(hull) >= 2 and cross_product_2d(hull[-2], hull[-1], p) <= 0:
                hull.pop()
            hull.append(p)
        return hull
    lower = build(points)
    upper = build(reversed(points))
    return [list(p) for p in lower[:-1] + upper[:-1]]

def point_in_triangle(p, a, b, c) -> bool:
    """Check if point p is inside triangle ABC using cross products."""
    d1 = cross_product_2d(a, b, p)
    d2 = cross_product_2d(b, c, p)
    d3 = cross_product_2d(c, a, p)
    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
    return not (has_neg and has_pos)

def euclidean_distance(p1: list[int], p2: list[int]) -> float:
    return sqrt(sum((a - b)**2 for a, b in zip(p1, p2)))

def manhattan_distance(p1: list[int], p2: list[int]) -> int:
    return sum(abs(a - b) for a, b in zip(p1, p2))


# =============================================================================
# TEST
# =============================================================================

if __name__ == "__main__":
    # K Closest
    result = k_closest([[1,3],[-2,2]], 1)
    assert result == [[-2,2]]
    result = set(map(tuple, k_closest([[3,3],[5,-1],[-2,4]], 2)))
    assert result == {(3,3),(-2,4)}

    # Max points on line
    assert max_points_on_line([[1,1],[2,2],[3,3]]) == 3
    assert max_points_on_line([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]) == 4

    # Valid square
    assert valid_square([0,0],[1,1],[1,0],[0,1])
    assert not valid_square([0,0],[1,1],[1,0],[0,12])

    # Min area rectangle
    assert min_area_rect([[1,1],[1,3],[3,1],[3,3],[2,2]]) == 4
    assert min_area_rect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]) == 2

    # Spiral matrix
    assert spiral_order([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
    assert spiral_order([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]

    # Search 2D matrix
    assert search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)
    assert not search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)

    # Geometry utils
    hull = convex_hull([[0,0],[1,1],[2,2],[0,2],[2,0]])
    assert len(hull) == 4  # square corners
    assert point_in_triangle([1,1],[0,0],[2,0],[0,2])
    assert not point_in_triangle([3,3],[0,0],[2,0],[0,2])

    print("All Day 11 geometry tests passed.")
