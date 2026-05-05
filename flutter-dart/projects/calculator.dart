// PROJECT: Pure Dart CLI Calculator | dart calculator.dart

import 'dart:io';

// TODO 1 (Mini): stdin REPL, tokenize "3 + 4", compute and print
//   void main() {
//     while (true) {
//       stdout.write(">> ");
//       final line = stdin.readLineSync();
//       if (line == null || line == "exit") break;
//       try {
//         final tokens = line.trim().split(RegExp(r'\s+'));
//         final a = double.parse(tokens[0]);
//         final op = tokens[1];
//         final b = double.parse(tokens[2]);
//         final result = switch (op) {
//           "+" => a + b,
//           "-" => a - b,
//           "*" => a * b,
//           "/" => b == 0 ? throw Exception("Division by zero") : a / b,
//           "%" => a % b,
//           _ => throw Exception("Unknown operator: $op"),
//         };
//         print(result);
//       } catch (e) {
//         print("Error: $e");
//       }
//     }
//   }

// TODO 2 (Intermediate): Tokenizer + recursive descent parser
//   - Use RegExp to scan: r'\d+\.?\d*|[+\-*\/()%]'
//   - Token types: Num, Plus, Minus, Star, Slash, Percent, LParen, RParen
//   - Grammar:
//       expr   → term (('+' | '-') term)*
//       term   → factor (('*' | '/') factor)*
//       factor → '-' factor | NUMBER | '(' expr ')'

// TODO 3 (Advanced): Variable assignment
//   - Parse "x = 5 + 3" → store in Map<String, double>
//   - Allow referencing variables in subsequent expressions

void main() {
  print("TODO: implement Dart calculator");
}
