// PROJECT: Kotlin Calculator CLI | kotlinc calculator.kt -include-runtime -d calculator.jar && java -jar calculator.jar

// TODO 1 (Mini): readLine() REPL loop, split on whitespace, compute "3 + 4"
//   - Support +, -, *, /, % with when expression
//   - Handle ArithmeticException for division by zero
//
// TODO 2 (Intermediate): Tokenizer + recursive descent parser (no eval)
//   - sealed class Token: Num(val n: Double), Plus, Minus, Star, Slash, LParen, RParen
//   - fun tokenize(input: String): List<Token>
//   - fun parseExpr(tokens: ListIterator<Token>): Double
//
// TODO 3 (Advanced): AST with sealed class
//   - sealed class Expr
//   - data class Num(val value: Double) : Expr()
//   - data class BinOp(val op: Char, val left: Expr, val right: Expr) : Expr()
//   - fun eval(expr: Expr): Double = when(expr) { ... }
//
// TODO 4 (Expert): Variable assignment
//   - Parse "x = 5 + 3" → store in mutableMapOf<String, Double>()
//   - Reference variables in subsequent expressions

fun main() {
    println("TODO: implement Kotlin calculator")
}
