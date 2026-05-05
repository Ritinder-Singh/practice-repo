#include <stdio.h>
// TOPIC: Loops & Control Flow | gcc -o out 03_loops_control_flow.c && ./out

int main(void) {
    // TODO 1: for, while, do-while loops
    //   for (int i = 0; i < 10; i++) printf("%d ", i);
    //   int n = 5; while (n > 0) { printf("%d ", n--); }
    //   do { printf("once at least\n"); } while (0);

    // TODO 2: break and continue
    //   // Print only odd numbers up to 20, stop at first multiple of 15
    //   for (int i = 1; i <= 20; i++) {
    //       if (i % 15 == 0) break;
    //       if (i % 2 == 0) continue;
    //       printf("%d\n", i);
    //   }

    // TODO 3: if / else if / else
    //   int grade = 85;
    //   if (grade >= 90) puts("A");
    //   else if (grade >= 80) puts("B");
    //   else if (grade >= 70) puts("C");
    //   else puts("F");

    // TODO 4: switch statement
    //   char op = '+';
    //   switch (op) {
    //       case '+': printf("add\n"); break;
    //       case '-': printf("sub\n"); break;
    //       default:  printf("unknown\n");
    //   }

    // TODO 5: Ternary operator
    //   int abs_val = x < 0 ? -x : x;

    // TODO 6: goto (valid use: error cleanup in C)
    //   FILE *f = fopen("file.txt", "r");
    //   if (!f) goto cleanup;
    //   // ... do work ...
    //   cleanup:
    //   if (f) fclose(f);

    // TODO 7: Nested loops — print multiplication table 1–10
    //   for (int i = 1; i <= 10; i++) {
    //       for (int j = 1; j <= 10; j++)
    //           printf("%4d", i * j);
    //       putchar('\n');
    //   }

    // TODO 8: Loop with pointer arithmetic
    //   int arr[] = {10, 20, 30, 40, 50};
    //   for (int *p = arr; p < arr + 5; p++) printf("%d\n", *p);

    printf("TODO: implement loop/control-flow exercises\n");
    return 0;
}
