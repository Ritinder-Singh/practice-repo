#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
// TOPIC: Error Handling | gcc -o out 06_error_handling.c && ./out

int main(void) {
    // TODO 1: errno + perror + strerror
    //   FILE *f = fopen("nonexistent.txt", "r");
    //   if (!f) {
    //       perror("fopen");                    // prints "fopen: No such file or directory"
    //       fprintf(stderr, "errno=%d: %s\n", errno, strerror(errno));
    //   }

    // TODO 2: Return-code pattern (most common in C)
    //   typedef enum { OK=0, ERR_NULL=-1, ERR_OVERFLOW=-2 } Result;
    //   Result parse_int(const char *s, int *out) {
    //       if (!s || !out) return ERR_NULL;
    //       char *end;
    //       long val = strtol(s, &end, 10);
    //       if (*end != '\0') return ERR_OVERFLOW;
    //       *out = (int)val;
    //       return OK;
    //   }

    // TODO 3: Output-parameter style (out-param for result + return for error)
    //   int divide(int a, int b, int *result) {
    //       if (b == 0) return -1;  // error
    //       *result = a / b;
    //       return 0;               // ok
    //   }

    // TODO 4: Cleanup with goto on error
    //   int process_file(const char *path) {
    //       FILE *f = fopen(path, "r"); if (!f) goto err_open;
    //       char *buf = malloc(4096);  if (!buf) goto err_malloc;
    //       // ... do work ...
    //       free(buf);
    //       fclose(f);
    //       return 0;
    //   err_malloc: fclose(f);
    //   err_open:   return -1;
    //   }

    // TODO 5: assert for programmer errors (not user input)
    //   #include <assert.h>
    //   assert(ptr != NULL);   // aborts with message in Debug builds
    //   // Use NDEBUG to disable: gcc -DNDEBUG ...

    // TODO 6: Custom error type with message
    //   typedef struct { int code; char msg[128]; } Error;
    //   Error err = { .code = 42 };
    //   snprintf(err.msg, sizeof(err.msg), "File not found: %s", path);

    // TODO 7: setjmp / longjmp (non-local jump — exception-like)
    //   #include <setjmp.h>
    //   jmp_buf jb;
    //   if (setjmp(jb) != 0) { /* caught error */ }
    //   // ... deep in call stack:
    //   longjmp(jb, 1);  // unwinds stack — does NOT call destructors

    // TODO 8: Propagating errors through a call chain
    //   int a(void); int b(void) { return a(); } int c(void) { return b(); }
    //   // Each function checks return value and propagates non-zero upward

    printf("TODO: implement error handling exercises\n");
    return 0;
}
