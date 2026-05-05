#include <iostream>
#include <stdexcept>
#include <expected>
#include <string>
// TOPIC: Error Handling | g++ -std=c++23 -o out 06_error_handling.cpp && ./out
// (use -std=c++20 if expected unavailable; see TODO 4 alternative)

int main() {
    // TODO 1: try / catch / throw
    //   try {
    //       throw std::runtime_error("something went wrong");
    //   } catch (const std::runtime_error &e) {
    //       std::cerr << "Error: " << e.what() << "\n";
    //   } catch (...) {
    //       std::cerr << "Unknown error\n";
    //   }

    // TODO 2: Standard exception hierarchy
    //   std::exception → std::logic_error → std::invalid_argument, std::out_of_range
    //                  → std::runtime_error → std::overflow_error, std::system_error
    //   Prefer std::logic_error for programming errors, runtime_error for external.

    // TODO 3: Custom exception class
    //   class AppError : public std::runtime_error {
    //       int code_;
    //   public:
    //       AppError(int code, const std::string &msg)
    //           : std::runtime_error(msg), code_(code) {}
    //       int code() const { return code_; }
    //   };

    // TODO 4: std::expected<T,E> (C++23) — error-as-value, no exceptions
    //   std::expected<int, std::string> parse(const std::string &s) {
    //       try { return std::stoi(s); }
    //       catch (...) { return std::unexpected("not a number: " + s); }
    //   }
    //   auto r = parse("42");
    //   if (r) std::cout << *r << "\n"; else std::cerr << r.error() << "\n";

    // TODO 5: RAII + exceptions — guarantee cleanup
    //   // Use unique_ptr, lock_guard — they clean up even if exception thrown.
    //   {
    //       std::lock_guard lock(mu);  // released even if body throws
    //       riskyOp();
    //   }

    // TODO 6: noexcept specification
    //   void swap(int &a, int &b) noexcept { int t = a; a = b; b = t; }
    //   // Tells compiler no exception possible → enables move optimizations

    // TODO 7: Exception safety levels
    //   // No-throw guarantee: never throws (noexcept)
    //   // Strong guarantee: operation either completes or leaves state unchanged
    //   // Basic guarantee: no leak, but state may change on exception
    //   // Implement strong guarantee using copy-and-swap idiom

    // TODO 8: std::terminate and std::set_terminate
    //   std::set_terminate([]{ std::cerr << "Unhandled exception\n"; std::abort(); });
    //   // Called when exception escapes main or noexcept function

    std::cout << "TODO: implement error handling exercises\n";
    return 0;
}
