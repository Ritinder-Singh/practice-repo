# =============================================================================
# PROJECT: Python Calculator
# =============================================================================
# TODO 1 (Mini): Basic REPL — accept expression strings, eval with operator module
#   Supported: +, -, *, /, **, %  |  Handle ZeroDivisionError + invalid input
#   Loop until "quit"
#
# TODO 2 (Intermediate): Recursive descent parser (no eval())
#   Grammar:
#     expr   → term (('+' | '-') term)*
#     term   → factor (('*' | '/' | '%') factor)*
#     factor → unary ('**' unary)*  (right-associative)
#     unary  → '-' unary | primary
#     primary → NUMBER | '(' expr ')'
#   Implement: tokenize(s) -> List[Token], then recursive descent parse/eval.
#
# TODO 3 (Advanced): Variables + history
#   x = 5 + 3       → store in variables dict, reference in later expressions
#   sqrt(16)        → built-in functions (math module)
#   history         → print last 10 expressions
#   vars            → print stored variables
#   Use readline for up-arrow history recall.
#
# Run: python calculator.py
# =============================================================================

import operator as op

OPERATORS = {"+": op.add, "-": op.sub, "*": op.mul,
             "/": op.truediv, "%": op.mod, "**": op.pow}

def main():
    print("Python Calculator — type 'quit' to exit")
    variables = {}
    history = []
    while True:
        try:
            expr = input("> ").strip()
            if not expr or expr.lower() == "quit":
                break
            # TODO: parse and evaluate expr
            # TODO: handle variable assignment (x = ...)
            # TODO: handle 'history' and 'vars' commands
            print("Result: (not implemented)")
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error: {e}")
        except EOFError:
            break

if __name__ == "__main__":
    main()
