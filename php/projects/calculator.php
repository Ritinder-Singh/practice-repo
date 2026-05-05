<?php
declare(strict_types=1);
// PROJECT: PHP Calculator CLI | php calculator.php

// TODO 1 (Mini): REPL using readline() or fgets(STDIN)
//   while (true) {
//       $input = readline(">> ");
//       if ($input === "exit" || $input === false) break;
//       if (preg_match('/^(-?\d+\.?\d*)\s*([+\-*\/%])\s*(-?\d+\.?\d*)$/', trim($input), $m)) {
//           [$_, $a, $op, $b] = $m;
//           $a = (float)$a; $b = (float)$b;
//           $result = match($op) {
//               "+" => $a + $b,
//               "-" => $a - $b,
//               "*" => $a * $b,
//               "/" => $b == 0 ? throw new DivisionByZeroError("Division by zero") : $a / $b,
//               "%" => (int)$a % (int)$b,
//           };
//           echo $result . "\n";
//       } else {
//           echo "Invalid expression\n";
//       }
//   }

// TODO 2 (Intermediate): Tokenizer + recursive descent parser
//   // Tokenize: preg_match_all('/\d+\.?\d*|[+\-*\/()%]/', $input, $matches)
//   // Token types: NUM, PLUS, MINUS, STAR, SLASH, PERCENT, LPAREN, RPAREN
//   // Parser functions: parseExpr(), parseTerm(), parseFactor()
//   // Grammar:
//   //   expr   → term (('+' | '-') term)*
//   //   term   → factor (('*' | '/') factor)*
//   //   factor → '-' factor | NUM | '(' expr ')'

// TODO 3 (Advanced): Variable assignment
//   // Parse "$x = 5 + 3" (PHP vars start with $) → store in $vars array
//   // Allow "$x * 2" referencing previously stored vars
