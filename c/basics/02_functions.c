#include <stdio.h>
#include <stdlib.h>
// TOPIC: Functions | gcc -o out 02_functions.c && ./out

int main(void) {
    // TODO 1: Basic functions — declaration, definition, call
    //   int add(int a, int b) { return a + b; }
    //   void greet(const char *name) { printf("Hello, %s\n", name); }
    //   // Forward declare if used before definition:
    //   // int add(int, int);

    // TODO 2: Passing by pointer (C's "pass by reference")
    //   void swap(int *a, int *b) { int t = *a; *a = *b; *b = t; }
    //   int x = 1, y = 2;
    //   swap(&x, &y);  // x=2, y=1

    // TODO 3: Returning pointers — heap allocation
    //   int *createArray(size_t n) {
    //       int *arr = malloc(n * sizeof(int));
    //       if (!arr) return NULL;
    //       return arr;    // caller must free()
    //   }

    // TODO 4: Function pointers
    //   int (*op)(int, int);   // declare function pointer
    //   op = add;              // assign
    //   printf("%d\n", op(3, 4));
    //   // Typedef for clarity:
    //   typedef int (*BinaryOp)(int, int);

    // TODO 5: Variadic functions
    //   #include <stdarg.h>
    //   int sum(int count, ...) {
    //       va_list args; va_start(args, count);
    //       int total = 0;
    //       for (int i = 0; i < count; i++) total += va_arg(args, int);
    //       va_end(args);
    //       return total;
    //   }

    // TODO 6: Recursive functions — factorial and Fibonacci
    //   unsigned long factorial(unsigned int n) {
    //       return n <= 1 ? 1 : n * factorial(n - 1);
    //   }

    // TODO 7: Inline functions
    //   static inline int max(int a, int b) { return a > b ? a : b; }
    //   // Hint to compiler to expand inline; avoids function-call overhead

    // TODO 8: Static functions — file-scope linkage
    //   static int helper(int x) { return x * 2; }  // not visible outside this .c file

    printf("TODO: implement function exercises\n");
    return 0;
}
