#include <iostream>
#include <vector>
#include <algorithm>
// TOPIC: Loops & Control Flow | g++ -std=c++20 -o out 03_loops_control_flow.cpp && ./out

int main() {
    // TODO 1: Range-based for loop
    //   std::vector<int> v = {1, 2, 3, 4, 5};
    //   for (int x : v) std::cout << x << " ";
    //   for (auto &x : v) x *= 2;  // mutate in place

    // TODO 2: Traditional for / while / do-while
    //   for (int i = 0; i < 10; ++i) { ... }
    //   int n = 5; while (n-- > 0) { ... }
    //   do { ... } while (condition);

    // TODO 3: if with initializer (C++17)
    //   if (auto it = m.find(key); it != m.end()) {
    //       std::cout << it->second << "\n";
    //   }

    // TODO 4: switch with structured binding (C++17)
    //   switch (auto [code, msg] = getStatus(); code) {
    //       case 200: std::cout << "OK: " << msg << "\n"; break;
    //       case 404: std::cout << "Not Found\n"; break;
    //       default:  std::cout << "Error\n";
    //   }

    // TODO 5: std::for_each + lambda
    //   std::for_each(v.begin(), v.end(), [](int x){ std::cout << x << "\n"; });

    // TODO 6: Algorithm alternatives to manual loops
    //   std::ranges::sort(v);
    //   auto it = std::find(v.begin(), v.end(), 3);
    //   bool any = std::any_of(v.begin(), v.end(), [](int x){ return x > 4; });

    // TODO 7: Early return vs. nested if — flatten control flow
    //   // Prefer early return over deeply nested else chains
    //   int process(int x) {
    //       if (x < 0) return -1;
    //       if (x == 0) return 0;
    //       return x * 2;
    //   }

    // TODO 8: Compile-time branching with if constexpr
    //   template<typename T>
    //   void describe(T val) {
    //       if constexpr (std::is_integral_v<T>) std::cout << "int: " << val << "\n";
    //       else std::cout << "other: " << val << "\n";
    //   }

    std::cout << "TODO: implement loop/control-flow exercises\n";
    return 0;
}
