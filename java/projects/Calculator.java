package projects;
// PROJECT: Java Calculator CLI | javac Calculator.java && java projects.Calculator
// Build a command-line calculator supporting +, -, *, /, ** (power), % (modulo) and parentheses.

public class Calculator {

    // TODO 1 (Mini): Basic REPL — Scanner reads expressions like "3 + 4", compute and print
    //   - Use Scanner(System.in), loop until "exit"
    //   - Split on space: tokens[0]=left, tokens[1]=op, tokens[2]=right
    //   - Handle: +, -, *, /, % — throw ArithmeticException on division by zero
    //
    // TODO 2 (Intermediate): Recursive descent parser (no eval)
    //   - Tokenize input into List<Token> with types: NUMBER, PLUS, MINUS, STAR, SLASH, LPAREN, RPAREN
    //   - Grammar:
    //       expr   → term (('+' | '-') term)*
    //       term   → factor (('*' | '/') factor)*
    //       factor → NUMBER | '(' expr ')' | '-' factor
    //   - Build an AST and evaluate it
    //
    // TODO 3 (Advanced): Variable assignment
    //   - Parse "x = 5 + 3" → store in HashMap<String, Double>
    //   - Reference variables in subsequent expressions: "x * 2"
    //   - Add readline history with jline library or manual up-arrow simulation

    public static void main(String[] args) {
        System.out.println("TODO: implement calculator");
    }
}
