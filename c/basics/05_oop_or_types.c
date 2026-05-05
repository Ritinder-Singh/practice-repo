#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// TOPIC: Structs, Unions & Type System | gcc -o out 05_oop_or_types.c && ./out
// C has no classes — simulate OOP with structs + function pointers.

int main(void) {
    // TODO 1: Struct with "methods" via function pointers
    //   typedef struct Animal Animal;
    //   struct Animal {
    //       char name[32];
    //       void (*speak)(const Animal *self);
    //   };
    //   void dog_speak(const Animal *self) { printf("%s says Woof!\n", self->name); }
    //   Animal dog = { .name = "Rex", .speak = dog_speak };
    //   dog.speak(&dog);

    // TODO 2: Opaque types (information hiding)
    //   // In header: typedef struct Counter Counter;
    //   // In .c only: struct Counter { int value; };
    //   // Users call counter_new(), counter_inc(), counter_get()

    // TODO 3: Union — shared memory for multiple types
    //   typedef union {
    //       int   i;
    //       float f;
    //       char  bytes[4];
    //   } FloatBits;
    //   FloatBits fb = { .f = 3.14f };
    //   printf("Bits: %08x\n", fb.i);  // inspect IEEE 754 bits

    // TODO 4: Tagged union (discriminated union / sum type)
    //   typedef enum { INT, FLOAT, STR } Tag;
    //   typedef struct { Tag tag; union { int i; float f; const char *s; } val; } Value;
    //   // switch on val.tag before accessing union field

    // TODO 5: Bit fields in struct
    //   typedef struct {
    //       unsigned int read    : 1;
    //       unsigned int write   : 1;
    //       unsigned int execute : 1;
    //       unsigned int _pad    : 5;
    //   } Permissions;
    //   Permissions p = { .read = 1, .write = 1, .execute = 0 };

    // TODO 6: Flexible array member
    //   typedef struct { size_t len; int data[]; } IntSlice;
    //   IntSlice *s = malloc(sizeof(IntSlice) + n * sizeof(int));

    // TODO 7: Function pointer table (vtable pattern)
    //   typedef struct { void (*draw)(void*); void (*resize)(void*, int); } ShapeVTable;
    //   typedef struct { ShapeVTable *vtable; /* shape data */ } Shape;
    //   // Circle and Rectangle each supply their own vtable

    // TODO 8: X-macro pattern — enum + string table without duplication
    //   #define COLORS(X) X(RED) X(GREEN) X(BLUE)
    //   typedef enum { COLORS(X_ENUM) } Color;    // X_ENUM(name) → name,
    //   const char *color_names[] = { COLORS(X_STR) };  // X_STR(name) → #name,

    printf("TODO: implement struct/union/type exercises\n");
    return 0;
}
