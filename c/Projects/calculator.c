#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
// PROJECT: Calculator REPL | gcc -o calculator calculator.c && ./calculator
//
// TODO 1 (Mini): Basic REPL with strtod and simple evaluation
//   - Parse lines like "3 + 4 * 2"
//   - Evaluate left-to-right (no precedence), handle +, -, *, /
//   - Print result; quit on "q" or EOF
//
// TODO 2 (Intermediate): Recursive descent parser (proper precedence)
//   Grammar:
//     expr   → term (('+' | '-') term)*
//     term   → factor (('*' | '/') factor)*
//     factor → NUMBER | '(' expr ')' | '-' factor
//
//   typedef struct { const char *src; int pos; } Parser;
//   double parseExpr(Parser *p);
//   double parseTerm(Parser *p);
//   double parseFactor(Parser *p);
//
// TODO 3 (Advanced): Variables + history
//   - Assignment: x = 5 + 3  (store in char*→double hash table)
//   - Reference vars in subsequent expressions
//   - "ans" always holds the last result
//   - "history" command prints last N results

int main(void) {
    printf("Calculator — TODO: implement\n");
    return 0;
}
