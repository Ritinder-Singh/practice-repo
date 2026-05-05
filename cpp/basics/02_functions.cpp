#include <iostream>
#include <functional>
#include <vector>
// TOPIC: Functions | g++ -std=c++20 -o out 02_functions.cpp && ./out

int main() {
    // TODO 1: Function overloading
    //   void print(int x)    { std::cout << "int: "    << x << "\n"; }
    //   void print(double x) { std::cout << "double: " << x << "\n"; }
    //   void print(const std::string &s) { std::cout << "str: " << s << "\n"; }

    // TODO 2: Default parameters
    //   void greet(const std::string &name, const std::string &msg = "Hello") {
    //       std::cout << msg << ", " << name << "\n";
    //   }

    // TODO 3: Lambda expressions
    //   auto add = [](int a, int b) { return a + b; };
    //   auto capture = [x](int y) { return x + y; };  // capture x by value
    //   auto mutable_cap = [x]() mutable { return ++x; };  // can modify copy

    // TODO 4: std::function — type-erase callable
    //   std::function<int(int, int)> op = add;
    //   op = [](int a, int b) { return a - b; };  // reassignable

    // TODO 5: Templates (function templates)
    //   template<typename T>
    //   T max(T a, T b) { return a > b ? a : b; }
    //   // Instantiated at compile time for each T used

    // TODO 6: Fold expressions (C++17) — variadic template sum
    //   template<typename... Args>
    //   auto sum(Args... args) { return (args + ...); }

    // TODO 7: Passing by value / reference / const-ref / move
    //   void byVal(std::string s);         // copies
    //   void byRef(std::string &s);        // mutates original
    //   void byCRef(const std::string &s); // read-only, no copy
    //   void byMove(std::string &&s);      // takes ownership

    // TODO 8: Recursive lambda (C++23 deducing this; C++20 workaround)
    //   std::function<int(int)> fib = [&](int n) {
    //       return n <= 1 ? n : fib(n-1) + fib(n-2);
    //   };

    std::cout << "TODO: implement function exercises\n";
    return 0;
}
