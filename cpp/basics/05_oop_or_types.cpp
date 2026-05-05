#include <iostream>
#include <memory>
#include <string>
#include <variant>
#include <optional>
// TOPIC: OOP & Type System | g++ -std=c++20 -o out 05_oop_or_types.cpp && ./out

int main() {
    // TODO 1: Class with RAII
    //   class Buffer {
    //       char *data; size_t sz;
    //   public:
    //       Buffer(size_t n) : data(new char[n]), sz(n) {}
    //       ~Buffer() { delete[] data; }
    //       Buffer(const Buffer &) = delete;             // no copy
    //       Buffer &operator=(const Buffer &) = delete;
    //       Buffer(Buffer &&o) noexcept : data(o.data), sz(o.sz) { o.data = nullptr; }
    //   };

    // TODO 2: Inheritance + virtual dispatch
    //   class Shape { public: virtual double area() const = 0; virtual ~Shape() = default; };
    //   class Circle : public Shape { double r; public: double area() const override { return 3.14*r*r; } };

    // TODO 3: Smart pointers
    //   auto p = std::make_unique<Circle>(5.0);   // unique ownership
    //   auto sp = std::make_shared<Circle>(3.0);  // shared ownership
    //   std::weak_ptr<Circle> wp = sp;            // non-owning observer

    // TODO 4: std::variant — type-safe tagged union (C++17)
    //   std::variant<int, double, std::string> v = 42;
    //   std::get<int>(v);                       // throws if wrong type
    //   std::visit([](auto &&val){ std::cout << val << "\n"; }, v);

    // TODO 5: std::optional — nullable value without pointer
    //   std::optional<int> parse(const std::string &s) {
    //       try { return std::stoi(s); } catch (...) { return std::nullopt; }
    //   }
    //   if (auto val = parse("42")) std::cout << *val << "\n";

    // TODO 6: Operator overloading
    //   struct Vec2 { double x, y; };
    //   Vec2 operator+(Vec2 a, Vec2 b) { return {a.x+b.x, a.y+b.y}; }
    //   bool operator==(Vec2 a, Vec2 b) { return a.x==b.x && a.y==b.y; }
    //   // C++20 spaceship: auto operator<=>(Vec2, Vec2) = default;

    // TODO 7: Class templates
    //   template<typename T>
    //   class Stack { std::vector<T> data; public: void push(T); T pop(); bool empty(); };

    // TODO 8: Concepts (C++20) — constrained templates
    //   template<typename T> concept Numeric = std::is_arithmetic_v<T>;
    //   template<Numeric T> T square(T x) { return x * x; }

    std::cout << "TODO: implement OOP exercises\n";
    return 0;
}
