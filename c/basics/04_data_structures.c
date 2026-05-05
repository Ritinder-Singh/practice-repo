#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// TOPIC: Data Structures | gcc -o out 04_data_structures.c && ./out

int main(void) {
    // TODO 1: Dynamic array (resizable)
    //   typedef struct { int *data; size_t len; size_t cap; } Vec;
    //   void vec_push(Vec *v, int val) {
    //       if (v->len == v->cap) {
    //           v->cap = v->cap ? v->cap * 2 : 4;
    //           v->data = realloc(v->data, v->cap * sizeof(int));
    //       }
    //       v->data[v->len++] = val;
    //   }
    //   void vec_free(Vec *v) { free(v->data); *v = (Vec){0}; }

    // TODO 2: Singly linked list
    //   typedef struct Node { int val; struct Node *next; } Node;
    //   Node *push_front(Node *head, int val) {
    //       Node *n = malloc(sizeof(Node));
    //       n->val = val; n->next = head; return n;
    //   }
    //   // Traverse: for (Node *p = head; p; p = p->next)
    //   // Free all: while (head) { Node *t = head->next; free(head); head = t; }

    // TODO 3: Stack using dynamic array
    //   Push: vec_push; Pop: return v->data[--v->len]; Peek: v->data[v->len-1]

    // TODO 4: Queue using circular buffer
    //   typedef struct { int *buf; size_t head, tail, cap; } Queue;
    //   Enqueue at tail, dequeue from head; use modulo for wrap-around.

    // TODO 5: Hash table with separate chaining
    //   #define TABLE_SIZE 64
    //   typedef struct Entry { char *key; int val; struct Entry *next; } Entry;
    //   Entry *table[TABLE_SIZE] = {0};
    //   size_t hash(const char *key) { ... djb2 ... }

    // TODO 6: Binary search tree
    //   typedef struct BST { int val; struct BST *left, *right; } BST;
    //   BST *bst_insert(BST *root, int val);
    //   bool bst_search(BST *root, int val);
    //   void bst_inorder(BST *root);   // prints sorted
    //   void bst_free(BST *root);

    // TODO 7: Doubly linked list
    //   typedef struct DNode { int val; struct DNode *prev, *next; } DNode;
    //   // insert_after, remove, traverse forward and backward

    // TODO 8: Min-heap (priority queue) using array
    //   parent = (i-1)/2; left = 2*i+1; right = 2*i+2
    //   sift_up after insert; sift_down after extract_min

    printf("TODO: implement data structure exercises\n");
    return 0;
}
