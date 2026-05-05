#include <iostream>
#include <string>
#include <cstdint>
// TOPIC: Variables & Types | g++ -std=c++20 -o out 01_variables_types.cpp && ./out

int main() {
    // TODO 1: Primitive types and auto
    //   int, long, unsigned, char, float, double, bool, void
    //   auto x = 42;         // int
    //   auto y = 3.14;       // double
    //   auto z = "hello"s;   // std::string (with "" s literal)

    // TODO 2: Fixed-width types from <cstdint>
    //   int8_t, uint8_t, int32_t, uint64_t, size_t, ptrdiff_t

    // TODO 3: const vs constexpr
    //   const int MAX = 100;          // runtime const
    //   constexpr int SZ = 1 << 10;   // compile-time constant
    //   constexpr double PI = 3.14159265358979;

    // TODO 4: References
    //   int x = 5;
    //   int &ref = x;      // lvalue reference — alias for x
    //   ref = 10;          // x is now 10
    //   const int &cref = 42;  // const ref can bind to rvalue

    // TODO 5: std::string
    //   std::string s = "Hello, World!";
    //   s.size(); s.substr(0, 5); s.find("World"); s + "!";
    //   s[0]; s.at(0);   // at() bounds-checks

    // TODO 6: Structured bindings (C++17)
    //   auto [a, b] = std::pair{1, 2};
    //   auto [key, val] = *map.begin();

    // TODO 7: Type aliases
    //   using Byte = uint8_t;
    //   using Matrix = std::vector<std::vector<double>>;
    //   typedef int (*Comparator)(const void*, const void*);   // old style

    // TODO 8: nullptr vs NULL
    //   int *p = nullptr;   // type-safe null pointer
    //   if (p == nullptr) std::cout << "null\n";

    std::cout << "TODO: implement variables & types exercises\n";
    return 0;
}
