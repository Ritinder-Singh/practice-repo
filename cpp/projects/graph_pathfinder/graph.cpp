#include <vector>
#include <queue>
#include <tuple>
#include <climits>
// Graph algorithms for the pathfinder project.

// TODO 1: Graph representation
//   // Grid stored externally; adjacency via 4-directional neighbors
//   const int dx[] = {0,0,1,-1};
//   const int dy[] = {1,-1,0,0};
//   bool inBounds(int x, int y, int rows, int cols);
//   bool isWall(const Grid &g, int x, int y);

// TODO 2: Dijkstra
//   // Returns {path, visited_count}
//   struct PathResult { std::vector<std::pair<int,int>> path; int visited; };
//   PathResult dijkstra(const Grid &g, int sx, int sy, int ex, int ey) {
//       // dist[x][y] = INT_MAX initially
//       // priority_queue<tuple<int,int,int>, ..., greater<>> pq
//       // push (0, sx, sy); relax neighbors
//       // reconstruct path via prev[x][y]
//   }

// TODO 3: A*
//   PathResult astar(const Grid &g, int sx, int sy, int ex, int ey) {
//       // h(x,y) = abs(x-ex) + abs(y-ey)  (Manhattan)
//       // pq holds (f=g+h, g, x, y)
//   }

// TODO 4: Path reconstruction helper
//   std::vector<std::pair<int,int>> reconstructPath(
//       const std::vector<std::vector<std::pair<int,int>>> &prev,
//       int sx, int sy, int ex, int ey);
