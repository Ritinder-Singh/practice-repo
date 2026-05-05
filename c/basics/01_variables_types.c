#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>
// TOPIC: Variables & Types | gcc -o out 01_variables_types.c && ./out
// Docs: https://en.cppreference.com/w/c/language/declarations

int main(void) {
    // TODO 1: Primitive types
    //   int, long, unsigned int, char, float, double
    //   int8_t, uint32_t, int64_t from <stdint.h>
    //   size_t for sizes/indices
    //   bool from <stdbool.h>

    // TODO 2: Type sizes
    //   printf("int: %zu bytes\n", sizeof(int));
    //   printf("long: %zu bytes\n", sizeof(long));
    //   // sizeof returns size_t — use %zu format specifier

    // TODO 3: Constants
    //   const int MAX = 100;
    //   #define BUFFER_SIZE 1024   // preprocessor constant
    //   enum Color { RED=0, GREEN=1, BLUE=2 };

    // TODO 4: Strings as char arrays
    //   char name[32] = "Alice";
    //   char *msg = "hello";          // string literal (read-only)
    //   strlen(name)                  // length without null terminator
    //   strncpy(dst, src, sizeof(dst)); // safe copy

    // TODO 5: Pointers
    //   int x = 42;
    //   int *p = &x;     // address-of
    //   *p = 99;          // dereference
    //   printf("%p\n", (void*)p);  // print address

    // TODO 6: Arrays
    //   int nums[5] = {1, 2, 3, 4, 5};
    //   int matrix[3][3] = {{1,2,3},{4,5,6},{7,8,9}};
    //   // Array name decays to pointer: nums == &nums[0]

    // TODO 7: Structs
    //   typedef struct {
    //       char name[32];
    //       int age;
    //       float score;
    //   } Person;
    //   Person p = { .name = "Bob", .age = 30, .score = 9.5f };

    // TODO 8: Type casting
    //   int a = 7, b = 2;
    //   double result = (double)a / b;  // explicit cast avoids integer division
    //   int truncated = (int)3.99;      // truncates toward zero → 3

    printf("TODO: implement variables & types exercises\n");
    return 0;
}
