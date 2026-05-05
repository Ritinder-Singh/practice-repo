#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
// TOPIC: Advanced C | gcc -o out 08_advanced.c && ./out

int main(void) {
    // TODO 1: Preprocessor macros with arguments
    //   #define MIN(a, b) ((a) < (b) ? (a) : (b))
    //   #define ARRAY_LEN(arr) (sizeof(arr) / sizeof((arr)[0]))
    //   #define CONTAINER_OF(ptr, type, member) \
    //       ((type *)((char *)(ptr) - offsetof(type, member)))

    // TODO 2: Memory layout — sizeof, offsetof, alignment
    //   #include <stddef.h>
    //   struct S { char a; int b; char c; double d; };
    //   printf("sizeof(S): %zu\n", sizeof(struct S));   // likely 24 (padding)
    //   printf("offsetof b: %zu\n", offsetof(struct S, b));  // likely 4

    // TODO 3: Bit manipulation
    //   uint32_t flags = 0;
    //   flags |= (1u << 3);           // set bit 3
    //   flags &= ~(1u << 3);          // clear bit 3
    //   flags ^= (1u << 3);           // toggle bit 3
    //   int set = (flags >> 3) & 1;   // test bit 3
    //   int lsb = flags & (-flags);   // isolate lowest set bit

    // TODO 4: restrict keyword — pointer aliasing hint
    //   void add_arrays(int * restrict dst, const int * restrict src, size_t n) {
    //       for (size_t i = 0; i < n; i++) dst[i] += src[i];
    //   }
    //   // Tells compiler dst and src don't overlap → enables SIMD auto-vectorization

    // TODO 5: volatile — prevent optimization of memory-mapped/shared vars
    //   volatile int signal_flag = 0;      // set by signal handler
    //   volatile uint32_t *reg = (uint32_t *)0xDEAD0000;  // MMIO register

    // TODO 6: Generic programming via void* and function pointers
    //   void qsort(void *base, size_t n, size_t size, int (*cmp)(const void*, const void*));
    //   int cmp_int(const void *a, const void *b) { return *(int*)a - *(int*)b; }
    //   int arr[] = {5,1,3,2,4}; qsort(arr, 5, sizeof(int), cmp_int);

    // TODO 7: Compile-time assertions
    //   _Static_assert(sizeof(int) == 4, "Expected 32-bit int");
    //   _Static_assert(sizeof(void*) >= 4, "Need at least 32-bit pointers");

    // TODO 8: setjmp / longjmp for error recovery (revisit from 06)
    //   // Build a try/catch-like macro:
    //   #define TRY if (setjmp(jbuf) == 0)
    //   #define CATCH else
    //   #define THROW longjmp(jbuf, 1)

    printf("TODO: implement advanced C exercises\n");
    return 0;
}
