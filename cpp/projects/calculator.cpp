#include <iostream>
#include <string>
#include <unordered_map>
#include <stdexcept>
// PROJECT: Calculator REPL | g++ -std=c++20 -o calculator calculator.cpp && ./calculator
//
// TODO 1 (Mini): Basic REPL with std::stod
//   - Read line, split tokens by whitespace
//   - Evaluate left-to-right: 3 + 4 * 2 → not precedence-aware yet
//   - Handle +, -, *, / and ZeroDivisionError
//
// TODO 2 (Intermediate): Recursive descent parser
//   Grammar:
//     expr   → term (('+' | '-') term)*
//     term   → factor (('*' | '/') factor)*
//     factor → NUMBER | '(' expr ')' | '-' factor
//
//   class Parser {
//       std::string src; int pos;
//   public:
//       double parseExpr(); double parseTerm(); double parseFactor();
//       double parse(const std::string &s) { src = s; pos = 0; return parseExpr(); }
//   };
//
// TODO 3 (Advanced): Variables + history
//   std::unordered_map<std::string, double> vars;
//   vars["ans"] = result;   // always updated
//   // Support: x = 5 + 3   parse assignment before expression
//   // "history" command prints last 10 results

int main() {
    std::cout << "Calculator — TODO: implement\n";
    return 0;
}
