// =============================================================================
// PROJECT: TypeScript CLI Calculator
// =============================================================================
// TODO 1 (Mini): CLI calculator — node calculator.js "3 + 4 * 2"
//   - Tokenize and parse expression
//   - Respect operator precedence (PEMDAS)
//   - Handle division by zero
//
// TODO 2 (Intermediate): Interactive REPL
//   - Variable assignment: x = 5 + 3
//   - Built-ins: sqrt(16), abs(-5), floor(3.7)
//   - Commands: history, vars, quit
//
// TODO 3 (Advanced): Typed AST
//   type Expr = NumberLit | BinaryOp | UnaryOp | Variable | FunctionCall
//   parse(tokens:Token[]): Expr
//   evaluate(expr:Expr, env:Map<string,number>): number
//
// Run: npx ts-node calculator.ts
// =============================================================================

type TokenType = "number" | "op" | "lparen" | "rparen" | "ident";
interface Token { type: TokenType; value: string; }

function tokenize(input: string): Token[] {
  // TODO: scan input char-by-char, emit tokens
  return [];
}

function main() {
  const rl = require("readline").createInterface({ input: process.stdin, output: process.stdout });
  console.log("TypeScript Calculator — type 'quit' to exit");
  const ask = () => {
    rl.question("> ", (line: string) => {
      if (line.trim() === "quit") { rl.close(); return; }
      // TODO: evaluate and print
      console.log("(not implemented)");
      ask();
    });
  };
  ask();
}

main();
