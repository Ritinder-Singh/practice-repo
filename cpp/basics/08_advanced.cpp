#include <iostream>
#include <type_traits>
#include <concepts>
#include <ranges>
#include <coroutine>
// TOPIC: Advanced C++ | g++ -std=c++20 -o out 08_advanced.cpp && ./out

int main() {
    // TODO 1: Template metaprogramming — compile-time fibonacci
    //   template<int N> struct Fib { static constexpr int val = Fib<N-1>::val + Fib<N-2>::val; };
    //   template<> struct Fib<0> { static constexpr int val = 0; };
    //   template<> struct Fib<1> { static constexpr int val = 1; };
    //   static_assert(Fib<10>::val == 55);

    // TODO 2: consteval and constexpr functions
    //   consteval int factorial(int n) { return n <= 1 ? 1 : n * factorial(n-1); }
    //   static_assert(factorial(5) == 120);

    // TODO 3: CRTP — Curiously Recurring Template Pattern
    //   template<typename Derived>
    //   class Printable { public: void print() { static_cast<Derived*>(this)->toString(); } };
    //   class Point : public Printable<Point> { public: void toString() { std::cout << "Point\n"; } };

    // TODO 4: std::ranges (C++20)
    //   std::vector<int> v = {5,1,3,2,4};
    //   auto even_sq = v | std::views::filter([](int x){ return x%2==0; })
    //                    | std::views::transform([](int x){ return x*x; });
    //   for (int x : even_sq) std::cout << x << " ";  // 4 16

    // TODO 5: Coroutines (C++20) — generator pattern
    //   // Requires implementing promise_type; complex boilerplate.
    //   // Generator<int> range(int from, int to) {
    //   //     for (int i = from; i < to; i++) co_yield i;
    //   // }

    // TODO 6: Perfect forwarding + universal references
    //   template<typename T>
    //   void wrapper(T &&arg) { target(std::forward<T>(arg)); }
    //   // std::forward preserves lvalue/rvalue category

    // TODO 7: Move semantics — implement Rule of Five
    //   class MyVec {
    //       int *data; size_t n;
    //   public:
    //       MyVec(MyVec &&o) noexcept : data(std::exchange(o.data, nullptr)), n(o.n) {}
    //       MyVec &operator=(MyVec &&o) noexcept { ... }
    //       // + copy ctor, copy assign, destructor
    //   };

    // TODO 8: Fold expressions (C++17) — generic print all args
    //   template<typename... Args>
    //   void println(Args&&... args) { (std::cout << ... << args) << "\n"; }

    std::cout << "TODO: implement advanced C++ exercises\n";
    return 0;
}
