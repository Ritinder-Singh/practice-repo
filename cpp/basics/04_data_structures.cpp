#include <iostream>
#include <vector>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>
// TOPIC: STL Data Structures | g++ -std=c++20 -o out 04_data_structures.cpp && ./out

int main() {
    // TODO 1: std::vector — dynamic array
    //   std::vector<int> v = {1, 2, 3};
    //   v.push_back(4); v.emplace_back(5);
    //   v.pop_back(); v.insert(v.begin()+1, 99); v.erase(v.begin());
    //   v.reserve(100); v.size(); v.capacity();

    // TODO 2: std::unordered_map — O(1) avg hash map
    //   std::unordered_map<std::string, int> freq;
    //   freq["hello"]++;
    //   if (freq.count("hello")) { ... }
    //   for (auto &[k, v] : freq) std::cout << k << ": " << v << "\n";

    // TODO 3: std::unordered_set — O(1) avg hash set
    //   std::unordered_set<int> seen;
    //   seen.insert(42); seen.contains(42); seen.erase(42);

    // TODO 4: std::stack (LIFO) and std::queue (FIFO)
    //   std::stack<int> st;  st.push(1); st.top(); st.pop();
    //   std::queue<int> q;   q.push(1); q.front(); q.pop();

    // TODO 5: std::priority_queue — max-heap by default
    //   std::priority_queue<int> maxH;
    //   std::priority_queue<int, std::vector<int>, std::greater<int>> minH;

    // TODO 6: std::map / std::set — ordered (red-black tree, O(log n))
    //   std::map<std::string, int> m;  // sorted by key
    //   m["z"] = 1; m["a"] = 2;       // iterates a → z
    //   std::set<int> s = {3, 1, 2};  // sorted: {1, 2, 3}

    // TODO 7: std::deque — O(1) push/pop at both ends
    //   std::deque<int> dq;
    //   dq.push_front(0); dq.push_back(1); dq.pop_front(); dq.pop_back();

    // TODO 8: Custom hash for unordered_map with pair key
    //   struct PairHash {
    //       size_t operator()(const std::pair<int,int> &p) const {
    //           return std::hash<int>{}(p.first) ^ (std::hash<int>{}(p.second) << 32);
    //       }
    //   };
    //   std::unordered_map<std::pair<int,int>, int, PairHash> dp;

    std::cout << "TODO: implement data structure exercises\n";
    return 0;
}
