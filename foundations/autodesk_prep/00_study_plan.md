# Autodesk Apprenticeship — 15-Day DSA Interview Prep

## Why Autodesk is Different
Autodesk builds CAD, 3D modeling, BIM, and animation software (AutoCAD, Maya, Revit, Fusion 360).
This means they weight problems related to:
- **Geometry & spatial reasoning** — coordinate math, transformations, point clouds
- **Graph traversal** — scene graphs, dependency trees (Revit BIM model hierarchy)
- **Intervals & scheduling** — construction project timelines (Revit/BIM use case)
- **Topological sort** — plugin/build dependency resolution
- **Tree operations** — scene hierarchies, file system (cloud Drive)
- **Matrix operations** — 2D/3D transformations in CAD

## Schedule Overview (Long Hours — 6–8 hrs/day)
| Day | Topic | # Problems | Files |
|-----|-------|------------|-------|
| 1 | Arrays & Two Pointers | 8 | 01_arrays_strings.py |
| 2 | Sliding Window + Intervals | 7 | 01_arrays_strings.py |
| 3 | Strings + Hashing | 7 | 01_arrays_strings.py |
| 4 | Linked Lists + Stack/Queue | 8 | 02_linked_lists_stack.py |
| 5 | Binary Trees (basics + traversal) | 8 | 03_trees_graphs.py |
| 6 | Binary Trees (advanced) + BST | 7 | 03_trees_graphs.py |
| 7 | Graphs — BFS/DFS | 7 | 03_trees_graphs.py |
| 8 | Graphs — Topological Sort + Union-Find | 6 | 03_trees_graphs.py |
| 9 | DP — 1D | 7 | 04_dp.py |
| 10 | DP — 2D + Grid | 7 | 04_dp.py |
| 11 | Geometry + Math (Autodesk-specific) | 6 | 05_geometry_math.py |
| 12 | Heaps + Greedy | 7 | 06_heaps_greedy.py |
| 13 | Backtracking + Hard Mix | 6 | 07_hard_mix.py |
| 14 | Mock Interview Day | 3 full mocks | — |
| 15 | Weak spots review + final mock | — | — |

---

## Day-by-Day Problem List

### DAY 1 — Arrays & Two Pointers
| # | Problem | LC | Difficulty | Autodesk Relevance |
|---|---------|-----|------------|-------------------|
| 1 | Two Sum | 1 | Easy | Hash map fundamentals |
| 2 | Best Time to Buy and Sell Stock | 121 | Easy | Sliding min pattern |
| 3 | Product of Array Except Self | 238 | Medium | Prefix/suffix arrays |
| 4 | Maximum Subarray (Kadane's) | 53 | Medium | Max gain in time-series data |
| 5 | 3Sum | 15 | Medium | Sorted two-pointer |
| 6 | Container With Most Water | 11 | Medium | Two-pointer geometry |
| 7 | Trapping Rain Water | 42 | Hard | 2D surface area — CAD terrain |
| 8 | Rotate Image | 48 | Medium | **Matrix rotation — core CAD transform** |

### DAY 2 — Sliding Window + Intervals
| # | Problem | LC | Difficulty | Autodesk Relevance |
|---|---------|-----|------------|-------------------|
| 1 | Longest Substring Without Repeating | 3 | Medium | Sliding window |
| 2 | Minimum Window Substring | 76 | Hard | Sliding window hard |
| 3 | Merge Intervals | 56 | Medium | **Construction scheduling — BIM/Revit** |
| 4 | Insert Interval | 57 | Medium | Interval insertion |
| 5 | Non-overlapping Intervals | 435 | Medium | Greedy + intervals |
| 6 | Meeting Rooms II | 253 | Medium | **Resource allocation — Autodesk cloud** |
| 7 | Employee Free Time | 759 | Hard | Multi-schedule merge |

### DAY 3 — Strings + Hashing
| # | Problem | LC | Difficulty | Autodesk Relevance |
|---|---------|-----|------------|-------------------|
| 1 | Valid Anagram | 242 | Easy | Frequency counting |
| 2 | Group Anagrams | 49 | Medium | Hashing by signature |
| 3 | Longest Repeating Character Replacement | 424 | Medium | Sliding window + freq |
| 4 | Find All Anagrams in a String | 438 | Medium | Pattern matching |
| 5 | Encode and Decode Strings | 271 | Medium | Serialization — scene/file format |
| 6 | Longest Palindromic Substring | 5 | Medium | String expand |
| 7 | Decode String | 394 | Medium | **Stack-based parsing — script/macro parsing in AutoCAD** |

### DAY 4 — Linked Lists + Stack/Queue
| # | Problem | LC | Difficulty | Autodesk Relevance |
|---|---------|-----|------------|-------------------|
| 1 | Reverse Linked List | 206 | Easy | Pointer manipulation |
| 2 | Merge Two Sorted Lists | 21 | Easy | Merge pattern |
| 3 | Linked List Cycle | 141 | Easy | Floyd's cycle detection |
| 4 | Reorder List | 143 | Medium | Find mid + reverse + merge |
| 5 | LRU Cache | 146 | Medium | **Cache for 3D asset loading — critical for Autodesk** |
| 6 | Valid Parentheses | 20 | Easy | Stack — expression parsing |
| 7 | Min Stack | 155 | Medium | Stack design |
| 8 | Daily Temperatures | 739 | Medium | Monotonic stack |

### DAY 5 — Binary Trees Basics + Traversal
| # | Problem | LC | Difficulty | Autodesk Relevance |
|---|---------|-----|------------|-------------------|
| 1 | Invert Binary Tree | 226 | Easy | Tree mutation |
| 2 | Maximum Depth of Binary Tree | 104 | Easy | DFS depth |
| 3 | Balanced Binary Tree | 110 | Easy | Height recursion |
| 4 | Diameter of Binary Tree | 543 | Easy | Longest path — scene graph diameter |
| 5 | Binary Tree Level Order Traversal | 102 | Medium | BFS on tree |
| 6 | Binary Tree Right Side View | 199 | Medium | BFS level-by-level |
| 7 | Count Good Nodes in Binary Tree | 1448 | Medium | DFS with state |
| 8 | Path Sum II | 113 | Medium | Backtracking on tree |

### DAY 6 — Binary Trees Advanced + BST
| # | Problem | LC | Difficulty | Autodesk Relevance |
|---|---------|-----|------------|-------------------|
| 1 | Construct Tree from Preorder+Inorder | 105 | Medium | **Tree reconstruction — scene deserialization** |
| 2 | Binary Tree Maximum Path Sum | 124 | Hard | DFS with global max |
| 3 | Serialize and Deserialize Binary Tree | 297 | Hard | **Scene graph save/load — Autodesk file formats** |
| 4 | Validate BST | 98 | Medium | Inorder + bounds |
| 5 | Kth Smallest in BST | 230 | Medium | Inorder traversal |
| 6 | Lowest Common Ancestor BST | 235 | Medium | **Scene hierarchy — find shared parent node** |
| 7 | Insert into BST | 701 | Medium | BST mutation |

### DAY 7 — Graphs: BFS/DFS
| # | Problem | LC | Difficulty | Autodesk Relevance |
|---|---------|-----|------------|-------------------|
| 1 | Number of Islands | 200 | Medium | DFS on 2D grid |
| 2 | Clone Graph | 133 | Medium | **Graph copy — deep clone 3D scene** |
| 3 | Pacific Atlantic Water Flow | 417 | Medium | Multi-source BFS |
| 4 | Surrounded Regions | 130 | Medium | BFS boundary flood-fill |
| 5 | Word Ladder | 127 | Hard | BFS shortest path |
| 6 | Rotting Oranges | 994 | Medium | Multi-source BFS |
| 7 | Max Area of Island | 695 | Medium | DFS + area counting |

### DAY 8 — Graphs: Topological Sort + Union-Find
| # | Problem | LC | Difficulty | Autodesk Relevance |
|---|---------|-----|------------|-------------------|
| 1 | Course Schedule | 207 | Medium | **Topo sort — plugin dependency check in AutoCAD** |
| 2 | Course Schedule II | 210 | Medium | Topo sort with order |
| 3 | Alien Dictionary | 269 | Hard | Topo sort from constraints |
| 4 | Number of Connected Components | 323 | Medium | Union-Find |
| 5 | Graph Valid Tree | 261 | Medium | Cycle detect + connectivity |
| 6 | Redundant Connection | 684 | Medium | Union-Find cycle detect |

### DAY 9 — DP: 1D
| # | Problem | LC | Difficulty | Autodesk Relevance |
|---|---------|-----|------------|-------------------|
| 1 | Climbing Stairs | 70 | Easy | Base DP |
| 2 | House Robber | 198 | Medium | DP with constraint |
| 3 | House Robber II | 213 | Medium | Circular DP |
| 4 | Longest Increasing Subsequence | 300 | Medium | Classic LIS |
| 5 | Word Break | 139 | Medium | **String parsing — command/script tokenizing in AutoCAD** |
| 6 | Decode Ways | 91 | Medium | DP on string |
| 7 | Coin Change | 322 | Medium | Unbounded knapsack |

### DAY 10 — DP: 2D + Grid
| # | Problem | LC | Difficulty | Autodesk Relevance |
|---|---------|-----|------------|-------------------|
| 1 | Unique Paths | 62 | Medium | **2D grid DP — CAD grid navigation** |
| 2 | Minimum Path Sum | 64 | Medium | Grid DP with cost |
| 3 | Longest Common Subsequence | 1143 | Medium | Classic 2D DP |
| 4 | Edit Distance | 72 | Hard | String diff — version control (Autodesk Docs) |
| 5 | Maximal Square | 221 | Medium | **2D rectangle search — region detection in CAD** |
| 6 | Interleaving String | 97 | Hard | 2D DP |
| 7 | Burst Balloons | 312 | Hard | Interval DP |

### DAY 11 — Geometry & Math (Autodesk-Specific)
| # | Problem | LC | Difficulty | Autodesk Relevance |
|---|---------|-----|------------|-------------------|
| 1 | K Closest Points to Origin | 973 | Medium | **3D spatial query — point cloud nearest neighbor** |
| 2 | Max Points on a Line | 149 | Hard | **Slope calculation — line detection in CAD** |
| 3 | Valid Square | 593 | Medium | Geometry validation |
| 4 | Minimum Area Rectangle | 939 | Medium | **Rectangle detection in point sets — 2D CAD** |
| 5 | Spiral Matrix | 54 | Medium | **Matrix traversal pattern — raster/grid operations** |
| 6 | Search a 2D Matrix | 74 | Medium | Binary search on matrix |

### DAY 12 — Heaps + Greedy
| # | Problem | LC | Difficulty | Autodesk Relevance |
|---|---------|-----|------------|-------------------|
| 1 | Kth Largest Element in Array | 215 | Medium | Quickselect / heap |
| 2 | Top K Frequent Elements | 347 | Medium | Bucket sort / heap |
| 3 | Find Median from Data Stream | 295 | Hard | **Two heaps — real-time analytics** |
| 4 | Task Scheduler | 621 | Medium | **Process scheduling — render farm queue** |
| 5 | Jump Game II | 45 | Medium | Greedy BFS |
| 6 | Gas Station | 134 | Medium | Greedy circular scan |
| 7 | Hand of Straights | 846 | Medium | Greedy + ordered map |

### DAY 13 — Backtracking + Hard Mix
| # | Problem | LC | Difficulty | Autodesk Relevance |
|---|---------|-----|------------|-------------------|
| 1 | Combination Sum | 39 | Medium | Backtrack with pruning |
| 2 | Subsets II | 90 | Medium | Backtrack with dedup |
| 3 | Word Search | 79 | Medium | **2D grid backtrack — CAD path search** |
| 4 | N-Queens | 51 | Hard | Classic backtrack |
| 5 | Largest Rectangle in Histogram | 84 | Hard | **Area under profile — CAD cross-section** |
| 6 | Median of Two Sorted Arrays | 4 | Hard | Binary search |

### DAY 14 — Mock Interview Day
Do 3 full 45-minute mock interviews:
- Mock 1: Pick 2 random problems from Days 1–5 (fundamentals)
- Mock 2: Pick 2 random problems from Days 6–10 (graphs + DP)
- Mock 3: Pick 1 geometry + 1 hard problem (Autodesk specialty)

Rules: No hints, timer on, talk out loud, write complexity at end.

### DAY 15 — Targeted Review
- Re-do every problem you got wrong or needed hints on
- Review all TIME/SPACE complexities
- Practice explaining your approach out loud for top 5 hardest problems

---

## Key Patterns to Master (in priority order)
1. **Two pointer / sliding window** — ~20% of array problems
2. **DFS/BFS template** — works for trees, graphs, 2D grids
3. **Topological sort (Kahn's + DFS)** — dependency problems everywhere at Autodesk
4. **Union-Find template** — connectivity in 3D scenes
5. **Monotonic stack** — histograms, temperatures, next greater element
6. **DP state design** — define state clearly before coding
7. **Heap/Priority Queue** — K-th element, scheduling, streaming
8. **Slope calculation with fractions** — geometry problems (gcd normalization)

## Interview Behavior Tips (Autodesk-specific)
- **Always mention Autodesk context**: "This reminds me of a scene graph — the 3D objects in Maya have exactly this parent-child relationship"
- **Talk about trade-offs**: memory vs time, exact vs approximate (spatial hashing)
- **Mention your PixelPod/SecondBrain work** when relevant (graph search, RAG retrieval, concurrent pipelines)
- Clarify: single vs multi-threaded? In-memory or persistent? Approximate ok?
