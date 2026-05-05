#include <iostream>
// PROJECT: Graph Pathfinder | g++ -std=c++20 -o pathfinder main.cpp graph.cpp visualizer.cpp
// Dijkstra + A* visualizer on a 2D grid.
//
// TODO 1: Grid setup
//   - Parse grid from stdin: '.' = open, '#' = wall, 'S' = start, 'E' = end
//   - Store as vector<vector<char>>
//
// TODO 2: Dijkstra's algorithm (see graph.cpp)
//   - Min-heap over (cost, x, y)
//   - No heuristic; guaranteed shortest path
//
// TODO 3: A* algorithm (see graph.cpp)
//   - f(n) = g(n) + h(n)  where h = Manhattan distance to end
//   - priority_queue<tuple<int,int,int,int>> (f, g, x, y)
//
// TODO 4: Visualizer (see visualizer.cpp)
//   - Print grid to terminal; mark visited cells, path with colors (ANSI)
//   - Optional: animate step-by-step with usleep()
//
// TODO 5: Benchmark comparison
//   - Run both algorithms on same grid; print steps explored, path length, time

int main() {
    std::cout << "Graph Pathfinder — TODO: implement\n";
    return 0;
}
