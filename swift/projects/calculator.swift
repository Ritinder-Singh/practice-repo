// PROJECT: Swift CLI Calculator | swift calculator.swift
// Run: swift calculator.swift

// TODO 1 (Mini): readLine() REPL, parse simple "3 + 4" expressions, print result
//   - Support +, -, *, /, handle division by zero
//   - Loop until user types "quit" or "exit"
//   - Use components(separatedBy:) to split the input into tokens

// TODO 2 (Intermediate): Recursive descent parser, support parentheses and operator precedence
//   - Lexer: tokenize input into .number(Double), .plus, .minus, .star, .slash, .lparen, .rparen
//   - Parser: expr -> term (('+' | '-') term)*
//             term -> factor (('*' | '/') factor)*
//             factor -> NUMBER | '(' expr ')'
//   - Evaluate the resulting AST

// TODO 3 (Advanced): Add variable storage (x = 5+3), store in [String: Double] dict
//   - Detect assignment expressions with '=' token
//   - Allow variables in subsequent expressions: x + 2
//   - Print stored variables with a "vars" command
